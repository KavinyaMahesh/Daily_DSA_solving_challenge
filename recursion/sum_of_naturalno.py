def sum_of_n(n):
    if n==1:
        return 1
    
    return n+sum_of_n(n-1)

if __name__=="__main__":
    n=5
    print(sum_of_n(n))