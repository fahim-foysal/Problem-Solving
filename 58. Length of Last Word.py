class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        count = 0
        flag = 0
        while length-1 >= 0:
            if s[length-1] != ' ':   
                count += 1
                flag = 1
            if s[length-1] == ' ' and flag == 1:
                break
            length -= 1
        print(count)
        
        """ first solution with bit less efficiency"""
        # word_list = s.split()
        # return len(word_list[(len(word_list)-1)])
s = Solution()
s.lengthOfLastWord("a")