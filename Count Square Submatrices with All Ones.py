class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        L = [[0] * (n+1) for _ in range(m+1)]
        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    L[i+1][j+1] = min(L[i][j+1], L[i+1][j], L[i][j]) + 1
                    result += L[i+1][j+1]
        return result
