class Solution:
    def countBits(self, n: int) -> List[int]:
        L = []
        for i in range(n+1):
            s = bin(i)[2:]
            r = s.count('1')
            L.append(r)
        return L
