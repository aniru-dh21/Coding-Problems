class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        sum1 = 0
        sum2 = sum(nums)
        L = []
        for i in nums:
            sum1 += i
            L.append(abs(sum1 - sum2))
            sum2 -= i
        return L
