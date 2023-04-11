class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        count = 0
        for i in nums:
            if (i + diff) in s and (i + diff * 2) in s:
                count += 1
        return count
