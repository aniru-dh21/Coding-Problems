class Solution:
    def calPoints(self, operations: List[str]) -> int:
        L = []
        for i in operations:
            if i != 'D' and i != 'C' and i != '+':
                L.append(int(i))
            elif i == 'C':
                L.pop()
            elif i == 'D':
                n = len(L)
                L.append(L[n-1]*2)
            else:
                m = len(L)
                L.append(L[m-1] + L[m-2])
        return sum(L)
