from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        
        while index < len(nums) - 1:
            if (nums[index] == nums[index + 1]):
                del nums[index]
            else:
                index += 1        

solution = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
solution.removeDuplicates(nums)
