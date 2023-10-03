from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        appendix = nums[k + 1:]
        for i in range(k):
            el = nums[-1]
            nums.pop()
            nums.insert(0, el)
            print(nums)
        
        
solution = Solution()

nums = [1,2,3,4,5,6,7]
k = 3
solution.rotate(nums, k)
# [5,6,7,1,2,3,4]

# nums = [-1,-100,3,99]
# k = 2
# solution.rotate(nums, k)