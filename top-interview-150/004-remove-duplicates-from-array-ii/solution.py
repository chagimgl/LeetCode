from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        
        while index < len(nums) - 2:
            if (nums[index] == nums[index + 1] and nums[index + 1] == nums[index + 2]):
                del nums[index]
            else:
                index += 1

solution = Solution()

nums = [1,1,1,2,2,3]
solution.removeDuplicates(nums)