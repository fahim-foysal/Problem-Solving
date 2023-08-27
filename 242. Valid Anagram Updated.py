class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        for i in s:
            if s_dict.get(i): 
                s_dict[i] = s_dict[i] + 1
            else:
                s_dict[i] = 1
        for i in t:
            if t_dict.get(i): 
                t_dict[i] = t_dict[i] + 1
            else:
                t_dict[i] = 1
        if s_dict == t_dict:
            return True
        else:
            return False
s = Solution()
print(s.isAnagram('aa','a'))