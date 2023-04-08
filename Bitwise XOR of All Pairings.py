class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = 0, 0
        for i in range(len(nums1)):
            s1 ^= nums1[i]
        for i in range(len(nums2)):
            s2 ^= nums2[i]
        if len(nums1)%2 == 0 and len(nums2)%2 == 0:
            return 0
        elif len(nums1)%2 == 1 and len(nums2)%2 == 0:
            return s2
        elif len(nums1)%2 == 0 and len(nums2)%2 == 1:
            return s1
        else:
            return s1^s2
