class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]
        CurrSum = 0
        
        for n in nums:
            print(CurrSum)
            if CurrSum < 0:
                CurrSum = 0
            CurrSum= CurrSum + n
            print(maxSum)
            if CurrSum > maxSum:
                maxSum = CurrSum
        return maxSum
        """
        :type nums: List[int]
        :rtype: int
        """
f = Solution()
f.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])