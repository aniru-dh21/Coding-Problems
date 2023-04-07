class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        L = [0] * len(nums)
        for i in range(len(nums)):
            L[i] = nums[nums[i]]
        return L
