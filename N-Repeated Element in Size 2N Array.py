class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for key, value in d.items():
            if d.get(key) == len(nums)//2:
                return key
