class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        output = [None]*len(arr)
        output[len(arr)-1] = -1 
        # for i in range(0, len(arr)-1):
        #     greatest_right = 0
        #     for j in range(i+1, len(arr)):
        #         if arr[j] > greatest_right:
        #             greatest_right = arr[j]
        #     output[i] = greatest_right 
        # return output
        for i in range(len(arr)-1, 0, -1):
            if arr[i] > output[i]:
                output[i-1] = arr[i]
            else:
                output[i-1] = output[i]      
        print(output)
            

s = Solution()
arr = [17,18,5,4,6,1]
s.replaceElements(arr)  