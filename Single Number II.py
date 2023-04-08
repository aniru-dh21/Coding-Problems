class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m, n = 0, 0
        for i in nums:
            n = (n ^ i) & ~m
            m = (m ^ i) & ~n
        return n
