
def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None
    return wrapper


@safe_function
def divide(x, y):
    return x / y


if __name__ == "__main__":
    print(divide(10, 0))
