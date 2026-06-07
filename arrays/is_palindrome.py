def is_palindrome(num):
    revnum=0
    dup=num
    while num>0:
        ld=num%10
        revnum=revnum*10+ld
        num=num//10

    if revnum==dup:
        return True
    else:
        return False

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")        
