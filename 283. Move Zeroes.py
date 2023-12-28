class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        index = 0
        while index < len(nums):
            if nums[index] != 0:
                nums[i], nums[index] = nums[index], nums[i]
                i += 1
            index += 1
