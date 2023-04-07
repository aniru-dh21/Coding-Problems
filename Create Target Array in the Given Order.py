class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        L = []
        for i in range(len(nums)):
            if index[i] == len(L):
                L.append(nums[i])
            else:
                L = L[:index[i]] + [nums[i]] + L[index[i]:]
        return L
