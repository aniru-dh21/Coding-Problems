class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = len(nums) * (len(nums) + 1)//2
        m = sum(nums) - sum(set(nums))
        n = s - sum(set(nums))
        return [m,n]
