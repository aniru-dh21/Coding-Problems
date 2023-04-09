class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[len(nums)-1]
        else:
            return nums[len(nums)-3]
