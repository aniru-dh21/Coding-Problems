class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = pref[0]
        for i in range(1, len(pref)):
            pref[i], n = n ^ pref[i], pref[i]
        return pref
