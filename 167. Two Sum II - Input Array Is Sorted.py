class Solution:
    def twoSum(self, numbers, target):
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                
                return [l,r]
            elif numbers[l]+numbers[r]<target:
                l=l+1
            elif numbers[l]+numbers[r]>target:
                r=r-1
        

s=Solution()
print(s.twoSum([2,7,11,15],9))
       