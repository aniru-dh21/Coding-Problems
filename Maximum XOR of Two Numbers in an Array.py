class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        m = 0
        for i in range(31, -1, -1):
            n = m | (1 << i)
            s = set(n & j for j in nums)
            if any(j ^ n in s for j in s):
                m = n
        return m
