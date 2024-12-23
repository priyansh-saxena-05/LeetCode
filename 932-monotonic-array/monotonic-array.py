class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] < nums[len(nums) - 1]:
            prev = nums[0]
            for num in nums:
                if num >= prev:
                    prev = num
                else:
                    return False
        else:
            prev = nums[0]
            for num in nums:
                if num <= prev:
                    prev = num
                else:
                    return False
        return True

