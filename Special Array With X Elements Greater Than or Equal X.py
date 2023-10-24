class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = 0
        h = 1000
        while l <= h:
            m = (l+h)//2
            count = 0
            for i in nums:
                if i >= m:
                    count += 1
            if m == count:
                return m
            elif m < count:
                l = m + 1
            elif m > count:
                h = m - 1
        return - 1
