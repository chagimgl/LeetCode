from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if (citations[i] >= i + 1):
                h += 1
                continue
            else:
                break
        return h

solution = Solution()



citations = [3,0,6,1,5]
citations = [1,3,1]
citations = [1]
solution.hIndex(citations)