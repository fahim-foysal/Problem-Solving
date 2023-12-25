class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # result_list= [None]*(m+n)
        # for digit in nums2:
        #     for i in range (0, m):
        #         if 
        nums3 = [0] * (m+n)
        i=0
        j=0
        k=0

        if m==0:
            nums1 = nums2
            return nums1

        while (i<m and j<n):
            if(nums1[i] < nums2[j]):
                nums3[k]= nums1[i]
                i+=1
                k+=1
            elif nums1[i] == nums2[j]:
                nums3[k] = nums1[i]
                i+=1
                k+=1
            else:
                nums3[k]= nums2[j]
                j+=1
                k+=1

        if i != m-1:
            for l in range(i, m):
                nums3[k] = nums1[l]
                k += 1

        if j != n-1:
            for l in range(j, n):
                nums3[k] = nums1[l]
                k += 1

        nums1 = nums3
        print(nums1)
        return nums1
s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)