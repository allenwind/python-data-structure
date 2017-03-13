def zero(f):
    def wrapper(x):
        return x
    return wrapper

def one(f):
    def wrapper(x):
        return f(x)
    return wrapper

def add(n, m):
    def wrapper(f):
        def inner(x):
            return m(f)(n(f)(x))
        return inner
    return wrapper
