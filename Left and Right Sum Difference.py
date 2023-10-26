class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum = []
        rsum = []
        answer = []
        nums1 = nums[::-1]
        for i in range(len(nums)):
            if i == 0:
                lsum.append(0)
                rsum.append(0)
            else:
                lsum.append(lsum[i-1]+nums[i-1])
                rsum.append(rsum[i-1]+nums1[i-1])
        rsum = rsum[::-1]
        for i in range(len(nums)):
            answer.append(abs(lsum[i] - rsum[i]))
        return answer
