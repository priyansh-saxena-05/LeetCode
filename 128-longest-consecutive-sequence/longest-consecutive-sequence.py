class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        ans = 0
        for num in values:
            if num - 1 not in values:
                length = 0
                while num + length in values:
                    length += 1
                    ans = max(length, ans)
        return ans

