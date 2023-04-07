class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        L = []
        sum = 0
        for i in accounts:
            for j in range(len(i)):
                sum += i[j]
                L.append(sum)
            sum = 0
        L.sort(reverse=True)
        return L[0]
