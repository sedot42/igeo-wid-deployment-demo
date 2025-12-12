import datetime


def logger(func):
    def wrapper():
        result = func()
        print(f"{datetime.datetime.now()}: {func.__name__}(): {result}")
        return result

    return wrapper


@logger
def hallo_welt():
    return "Hallo Welt"


hallo_welt()

# 2025-11-18 19:43:41.004214: hallo_welt(): Hallo Welt
