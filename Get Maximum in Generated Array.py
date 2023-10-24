class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        L = [0] * (n+2)
        L[1] = 1
        for i in range(1, (n//2)+1):
            L[i*2] = L[i]
            L[2*i+1] = L[i] + L[i+1]
        return max(L[:n+1])
