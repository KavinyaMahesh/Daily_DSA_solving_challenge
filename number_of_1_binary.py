def number_of_set_bits(n):
    cnt=0
    while n!=0:
        a=n%2
        if a==1:
            cnt+=1
        n=n//2

    return cnt

if __name__=="__main__":
    result = number_of_set_bits(29)
    print("Number of 1 bits is:", result)    