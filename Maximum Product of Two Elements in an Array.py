class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        L = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    L.append((nums[i]-1) * (nums[j]-1))
        return max(L)
