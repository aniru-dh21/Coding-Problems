class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m = min(nums)
        n = max(nums)
        r = 1
        for i in range(2,m+1):
            if m%i == 0 and n%i == 0:
                r = i
        return r 
