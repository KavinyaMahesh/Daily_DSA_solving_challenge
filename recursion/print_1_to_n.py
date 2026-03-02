def print1toN(n,count):
    if n==0:
        return
    #base case
    if count>n:
        return 
    
    print(count,end=" ")
    
    print1toN(n,count+1)

if __name__=="__main__":
    n=10
    print1toN(n,1)      
    

    