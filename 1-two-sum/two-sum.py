class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, num in enumerate(nums):
            val = target - num
            if val not in hmap:
                hmap[num] = i
            else:
                return [hmap[val],i]
