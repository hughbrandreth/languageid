import timeit
from functools import wraps

TimeLogsDict = dict()


def Timelogger(func):
    '''
    Wraps a function with a timer which times the running of the function.
    The time taken is appended to a list in a dictionary keyed by the name of the function being timed.

    :param func:
    :return: TimeFunc wrapped function
    '''
    @wraps(func)
    def TimeFunc(*args, **kwargs):
        Start = timeit.default_timer()
        Result = func(*args, **kwargs)
        End = timeit.default_timer()
        if func.__name__ not in TimeLogsDict:
            TimeLogsDict[func.__name__] = []
        TimeLogsDict[func.__name__].append(End-Start)
        return Result
    return TimeFunc

