class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        nums.sort()
        count = 0
        i = 0
        j = 1
        while j < len(nums) and i < j:
            if j < len(nums) - 1 and nums[j+1] == nums[j]:
                j += 1
            elif nums[j] == nums[i] + k:
                count += 1
                i += 1
                j += 1
            elif nums[i] + k < nums[j]:
                i += 1
            elif nums[i] + k > nums[j]:
                j += 1
            j = max(j, i+1)
        return count
