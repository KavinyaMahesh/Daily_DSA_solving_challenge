def sum_of_int(a: int, b: int) -> int:
    """
    Returns the sum of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers without using + or - operators.
    """
    while b!=0:
        sum=a^b
        carry=(a&b)<<1

        a=sum
        b=carry
    return a

if __name__=="__main__":
    result = sum_of_int(15, 32)
    print("Sum is:", result)
    