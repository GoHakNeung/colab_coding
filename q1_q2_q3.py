from learntools.core.multiproblem import MultipartProblem

def backtickify(s):
    return '`{}`'.format(s)

# This is an artifact of when we had extra credit questions and wanted an option for
# a scoring mechanism that's no longer necessary
quantum_of_bonus = 1/37

def instantiate_probview(prob_cls, value_per_problem):   #problem을 인스턴스로 만든다는 함수인가? 매개변수가 첫번째는 클래스, 두번째는 ...  변수?
    # TODO: Bleh, circular import...
    from learntools.core import problem_view as pv
    from learntools.core.globals_binder import binder
    # NB: May eventually have some subclasses for this?
    viewer_cls = pv.ProblemView        # problemview의 객체가 viewer_cls임
    prob = prob_cls()                  # 받아온 클래스에서 __call__을 실행시킴.
    if prob._counts_for_points:        # problem 모듈에서 Problem 클래스에 있는 변수
        if prob._bonus:                # problem 모듈에서 Problem 클래스에 있는 변수
            prob.point_value = quantum_of_bonus   # 새로운 point_value를 만듬
        else:
            prob.point_value = value_per_problem   #아래 bind_exercise함수에서 사용됨.
    else:
        prob.point_value = 0
    view = viewer_cls(prob, binder.readonly_globals())  #매개변수 1번은 problem 이고 매개변수 2번은 globals 임
    # XXX: Circular reference. :/
    # Consider using weakref (https://docs.python.org/3/library/weakref.html)
    # Also, would just have preferred a cleaner separation between these abstractions...
    prob._view = view
    return view


def bind_exercises(g, exercises, start=1, var_format='q{n}'):                         #exercise는 문제 모듈에서 문제 클래스 변수임.
    """Given the globals() dict of an exercise module, and an ordered list of
    Problem subclasses, create a sequence of variables (by default q1, q2, q3...
    but customizable via the start and var_format kwargs) referring to instantiations
    of the Problem subclasses (well, technically wrapped in ProblemView instances).
    Embed those variable assignments in the given namespace, and yield the names of
    all the new variables.

    Elements of exercises may also be None as a placeholder, in which case the 
    corresponding variable in the sequence is skipped over. e.g. [SpamProblem, None,
    EggsProblem], will generate variables q1 and q3.
    """
    denom = sum( 
            (getattr(prob, '_counts_for_points', False) and not prob._bonus) 
            for prob in exercises
            )
    try:
        value_per_problem = 1 / denom
    except ZeroDivisionError:
        value_per_problem = 1.0

    for i, prob_cls in enumerate(exercises):
        # A value of None is a placeholder. Reserve the corresponding question number, but don't create any corresponding Problem obj.
        if prob_cls is None:
            continue
        qno = i + start
        varname = var_format.format(n=qno)
        assert varname not in g                                                            # g는 globals()로 생각됨 >> bind 모듈 확인해봐야함.
        # TODO: Probably cleaner to just pass these as sublists, rather than having
        # the MultipartProblem class start in some nascent state and get 'activated' here
        if isinstance(prob_cls, MultipartProblem):      #prob_cls가 multipartproblem 의 클래스인지 확인
            mpp = prob_cls
            g[varname] = mpp
            mpp._varname = varname
            for j, prob_cls in enumerate(mpp.problems):
                prob = instantiate_probview(prob_cls, value_per_problem)
                # Bleh, more properties tacked on ad-hoc outside the class.
                prob._order = '{}.{}'.format(qno, j+1)
                letter = chr(ord('a')+j)
                setattr(mpp, letter, prob)
                mpp._prob_map[letter] = prob
        else:
            pv = instantiate_probview(prob_cls, value_per_problem)
            pv._order = str(qno)
            g[varname] = pv
        yield varname
    # Bad sep of concerns, but anyways, have exercise modules also export quad alias
    # variable as alias for special Placeholder value (if it exists in their namespace
    # i.e. if they imported * from learntools.core)
    if '____' in g:
        yield '____'

def format_args(fn, args):
    c = fn.__code__
    params = c.co_varnames[:c.co_argcount]
    #assert len(args) == len(params)
    return ', '.join(['`{}={}`'.format(param, repr(arg))
        for (param, arg) in zip(params, args)])
