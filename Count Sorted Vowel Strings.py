class Solution:
    def countVowelStrings(self, n: int) -> int:
        L = [[i for i in range(5,0,-1)] for _ in range(n)]
        for i in range(1, n):
            for j in range(3,-1,-1):
                L[i][j] = L[i-1][j] + L[i][j+1]
        return L[n-1][0]
