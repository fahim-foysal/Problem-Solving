
class Solution:
    def isAnagram(self,s,t):
        s_dict={}
        t_dict={}
        for i in s:
            s_dict[i]=0
        for j in t:
            t_dict[j]=0


        for key in s_dict.keys():
            for i in s:
                if key==i:
                    s_dict[key]=s_dict[key]+1

        for key in t_dict.keys():
            if i in t:
                if key==i:
                    t_dict[key]=t_dict[key]+1
        key_val= s_dict.keys()
        if len(s_dict)==len(t_dict):
            for i in key_val:
                if s_dict[i]!=t_dict[i]:
                    return False
            return True
        return False

b='anagram'
c='nagaram'
a=Solution
a.isAnagram(a,b,c)

        
