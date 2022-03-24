# many positional arguments (* argument_name) (args work as tuple)
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3,4,5,6,7,8))

# many keyword arguments (** argument_name) (kwargs work as dictionary)
