class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            val = nums[i] + nums[j]
            if val < target:
                i += 1
            elif val > target:
                j -= 1
            else:
                return [i+1, j+1]
        