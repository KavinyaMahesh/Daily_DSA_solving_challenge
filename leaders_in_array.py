# Example:
# Input:
#  arr = [10, 22, 12, 3, 0, 6]  
# Output:
#  22 12 6  
# Explanation:
#  6 is a leader because there are no elements after it.  
# 12 is greater than all the elements to its right (3, 0, 6), and 22 is greater than 12, 3, 0, 6, making them leaders as well.


def find_leaders(arr):
    n=len(arr)

    leaders=[]
    max_el=arr[-1]

    leaders.append(max_el)

    for i in range(n-2, -1, -1):
        if arr[i]>max_el:
            leaders.append(arr[i])
            max_el=arr[i]

    leaders.reverse()

    return leaders

if __name__=="__main__":
    arr = [10, 22, 12, 3, 0, 6] 

    res=find_leaders(arr)
    print(res)

