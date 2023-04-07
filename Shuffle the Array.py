class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        L = nums[:n]
        L1 = nums[n:]
        L2 = []
        for i in range(n):
            L2 += [L[i]] + [L1[i]]
        return L2
