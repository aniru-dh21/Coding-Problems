class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        L = []
        for i in range(n):
            L.append(start + 2 * i)
        r = 0
        for i in L:
            r ^= i
        return r
