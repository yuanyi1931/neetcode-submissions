from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for n in s:
            if n - 1 not in s:          # n starts a streak
                cur, length = n, 1
                while cur + 1 in s:
                    cur += 1
                    length += 1
                best = max(best, length)
        return best