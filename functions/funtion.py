def abc(a,b=10,c=30):
    print(a,b,c)
    print(a+b+c)

abc(a=10,c=40)

def vararg(a,*args, **argskey):
    print(a)
    for i in args:
        print(i)
    for key, val in argskey.items():
        print(key,val)

vararg(1,2,3,4,5, abc=20, xyz=40)

lambdaA = lambda a : a*a

b = lambdaA(12)

print(b)

def lambda_inside(n):
    return lambda a: a+n 

temp = lambda_inside(10)
print(temp(10))

def multiple_return(a,b):
    """ 
    function which return multiple values
    :param a:
    :param b:
    :return a+b, a*b:
    """
    return a+b,a*b

c= multiple_return(10,20)
print("docstring multiple_return")
print(multiple_return.__doc__)
print(c)
