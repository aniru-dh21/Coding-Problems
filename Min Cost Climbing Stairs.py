class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return 0
        L = [0] * (n+1)
        for i in range(2, n+1):
            L[i] = min(cost[i-1] + L[i-1], cost[i-2] + L[i-2])
        return L[n] 
