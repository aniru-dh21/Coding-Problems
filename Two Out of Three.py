class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        L = []
        for i in nums1:
            if i in nums2 or i in nums3:
                if i not in L:
                    L.append(i)
        for j in nums2:
            if j in nums3 or j in nums1:
                if j not in L:
                    L.append(j)
        return L
