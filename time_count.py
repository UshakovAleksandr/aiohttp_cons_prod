from time import time


def time_count(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print("Выполнено за {:.2F} сек".format(time() - start))
        return result

    return wrapper


def async_time_count(func):
    async def wrapper(*args, **kwargs):
        start = time()
        result = await func(*args, **kwargs)
        print("Выполнено за {:.2F} сек".format(time() - start))
        return result

    return wrapper