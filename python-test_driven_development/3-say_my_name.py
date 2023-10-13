def add_integer(a, b=98):
    """ function to add two integers """
    try:
        result = a + b
        return int(result)
    except TypeError as e:
        if type(a) is not int:
            raise TypeError("a must be an integer")
        elif type(b) is not int:
            raise TypeError("b must be an integer")
        else:
            raise e
