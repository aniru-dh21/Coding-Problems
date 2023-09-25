class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        L, res = [], [0] * n
        for i in range(n-1, -1, -1):
            while L and L[-1] <= heights[i]:
                L.pop()
                res[i] += 1
            if L:
                res[i] += 1
            L.append(heights[i])
        return res
