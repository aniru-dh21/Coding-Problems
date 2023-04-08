class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        L = []
        L.append(0)
        for i in range(len(gain)):
            L.append(L[i]+gain[i])
        print(L)
        return max(L)
