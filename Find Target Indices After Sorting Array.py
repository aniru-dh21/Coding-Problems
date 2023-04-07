class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        L = []
        for i in range(len(nums)):
            if nums[i] == target:
                L.append(i)
        return L
