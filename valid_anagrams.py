def abc(str1,str2):
    if len(str1)!=len(str2):
        return False
    
    # count1=[0]*26
    # count2=[0]*26

    # for i in range(len(str1)):
    #     count1[ord(str1[i])-ord('a')]+=1
    #     count2[ord(str2[i])-ord('a')]+=1

    # for i in range(26):
    #     if count1[i]!=count2[i]:
    #         return False
    # return True

    if sorted(str1)==sorted(str2):
        return True
    return False

if __name__=="__main__":
    str1="listen"
    str2="silent"
    print(abc(str1,str2))
    