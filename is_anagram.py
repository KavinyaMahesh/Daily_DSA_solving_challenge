class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1={}
        mp2={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in mp1:
                mp1[i]+=1
            else:    
                mp1[i]=1

        for j in t:
            if j in mp2:
                mp2[j]+=1
            else:    
                mp2[j]=1


        return mp1==mp2
    

if __name__=="__main__":
    solution = Solution()
    result = solution.isAnagram("anagram", "nagaram")
    print("Is anagram:", result) 