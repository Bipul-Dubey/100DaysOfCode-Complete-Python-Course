def logging_decorator(function):
    def wrapper(*args):
        print(f"you called a function {function.__name__}{args}")
        result=args[0]+args[1]+args[2]
        print(f"it returned: {result}")
    return wrapper


@logging_decorator
def Sum(a,b,c):
    return a+b+c


Sum(10,20,30)
# just write args instead of (args[0],args[1],args[2])  because args pass as tuple so its automatically like that
