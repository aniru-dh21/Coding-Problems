class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        m = 0
        for i in nums:
            m ^= i
        n = m & -m
        p, q = 0, 0
        for i in nums:
            if i & n:
                p ^= i
            else:
                q ^= i
        return [p, q]
