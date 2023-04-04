class Solution:
    def isPalindrome(self, s):

        string=s.lower()
        output=""
        for i in string:
            if ord(i)>=97 and ord(i)<=122 or ord(i)>=48 and ord(i)<=57:
                output=output+i
        print(output)
        palindrome=""
        for i in range (len(output)-1,-1,-1):
            palindrome=palindrome+output[i]
        print(palindrome)
        if output==palindrome:
            return True
        else:
            return False


s=Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))

