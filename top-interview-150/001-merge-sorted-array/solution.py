from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # merged = nums1 + nums2        
        # max_num = max(merged)
        # aux = [0] * (max_num + 1)
        
        # for i in range(len(merged)):
        #     if (merged[i] > 0):
        #         aux[merged[i]] += 1
        # f = []
        # for i in range(len(aux)):
        #     if aux[i] > 0:
        #         f = f + ([i] * aux[i])

        
        a = m - 1    # index of nums1
        b = n - 1    # index of nums2
        write_index = m + n - 1
        
        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1
            write_index -= 1
            
solution = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution.merge(nums1, m, nums2, n)

nums1 = [1]
m = 1
nums2 = []
n = 0
solution.merge(nums1, m, nums2, n)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution.merge(nums1, m, nums2, n)