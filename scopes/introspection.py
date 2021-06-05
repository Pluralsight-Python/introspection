#!/usr/bin/python3
"""
    Example file for demonstrating tools for scope introspection
"""
print()
print("Global Scope:")
print()
print(f"{globals() = }")
print()
print(f"{locals() = }")
print()


def dummy_func(*args, **kwargs):
    from pprint import pp
    local_var = 42
    print("\nLocal scope of func dummy_func:\n")
    if args:
        pp(f"{args = }")
    if kwargs:
        pp(f"{kwargs = }")
    print(f"{locals() = }")


def enclosing_scope(some_func, *e_args, **e_kwargs):
    import functools
    @functools.wraps(some_func)
    def wrapper(*f_args, **f_kwargs):
        nonlocal functools, e_args, e_kwargs
        some_local_var = "Hello World!!"
        print("Enclosing Scope: ")
        print()
        print(f"{locals()}")
        return some_func(*f_args, **f_kwargs)
    return wrapper


dummy_func()
print()
enclosing_scope(dummy_func)("arg1", arg2="dummy")
print()

print(f"{globals() = }")
print()

