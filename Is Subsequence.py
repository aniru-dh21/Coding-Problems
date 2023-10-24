class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        L = [{} for _ in range(len(t) + 1)]
        for i in range(len(t) - 1, -1, -1):
            L[i] = L[i+1].copy()
            L[i][t[i]] = i + 1
        i = 0
        for j in s:
            if j in L[i]:
                i = L[i][j]
            else:
                return False
        return True
