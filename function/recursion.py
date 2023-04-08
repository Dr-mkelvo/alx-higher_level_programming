def fact(num):
    """ This is a function which finds the factorial of a positive integer

    """
    if num == 1:
        return 1

    else:
        return num * fact(num - 1)
    
print(fact(9))