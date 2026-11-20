class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        max_size = 0

        counter = collections.Counter()
        l = 0

        for r in range(n):
            counter[s[r]] += 1
            while len(counter) > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            max_size = max(max_size, r - l + 1)
        return max_size
 
