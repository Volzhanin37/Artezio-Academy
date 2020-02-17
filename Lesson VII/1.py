from time import sleep, time
from functools import wraps


def average_time(n=2):
    def inner_decorator(function):
        times = []
        counter = 0

        @wraps(function)
        def wrapper(*args, **kwargs):
            nonlocal counter
            current_time = time()
            res = function(*args, **kwargs)
            if len(times) < n:
                times.append(time() - current_time)
            else:
                times[counter] = time() - current_time
                counter += 1
                if counter == n:
                    counter = 0

            print(('Среднее время работы: ',
                  round((sum(times) * 1000 / len(times))), 'мс'))
            return res

        return wrapper

    return inner_decorator


@average_time(n=2)
def foo(a):
    sleep(a)
    return a

foo(3)
foo(7)
foo(1)
