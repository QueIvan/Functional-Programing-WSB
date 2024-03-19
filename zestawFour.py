import time


def timeit(method):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        end = time.time()
        print(f"Funkcja {method.__name__} wykonanała się w {end - start} sekund.")

    return wrapper


@timeit
def dummy_func():
    time.sleep(1)


if __name__ == '__main__':
    dummy_func()
