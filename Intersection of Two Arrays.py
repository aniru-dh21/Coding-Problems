class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        L = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1:
                    L.append(i)
        else:
            for i in nums1:
                if i in nums2:
                    L.append(i)
        return list(set(L))
