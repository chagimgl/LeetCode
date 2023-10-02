from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Boyer-Moore Majority Voting Algorithms
        
        votes = 0
        candidate = -1
        
        for item in nums:
            if votes == 0:
                candidate = item
            else:
                if item == candidate:
                    votes += 1
                else:
                    votes -= 1
        return candidate
        
        
solution = Solution()

nums = [3,2,3]
solution.majorityElement(nums)