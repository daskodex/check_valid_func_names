import timeit

MAX_LENGTH = 1024 * 1024 #about 1mb

def function_speed(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        func(*args, **kwargs)
        delta = timeit.default_timer() - start_time
        print(f'Speed of {func.__name__} is: {delta}')

    return wrapper


@function_speed
def random_set(do_search=0, size_in_mb=1) -> None:
    test_set = [None]
    for i in range(MAX_LENGTH * size_in_mb):
        test_set.append(i)

    if do_search == 1:
        if (MAX_LENGTH * size_in_mb)-1 in test_set:
            print(f'Yes, we find it, data size {size_in_mb}MB -> ', end='')
        else:
            print('No, we not find it', end='')

    return None


@function_speed
def random_list(do_search=0, size_in_mb=1) -> None:
    test_list = [None]
    for i in range(MAX_LENGTH * size_in_mb):
        test_list.append(i)

    if do_search == 1:
        if (MAX_LENGTH * size_in_mb)-1 in test_list:
            print(f'Yes, we find it, data size {size_in_mb}MB -> ', end='')
        else:
            print('No, we not find it ', end='')

    return None


random_list()
random_set()

random_list(1)
random_set(1)

random_list(1, 10)
random_set(1, 10)

random_list(1, 50)
random_set(1, 50)

random_list(1, 100)
random_set(1, 100)

random_list(1, 200)
random_set(1, 200)