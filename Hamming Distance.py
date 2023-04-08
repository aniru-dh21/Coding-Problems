class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        hd = 0
        while z:
            z &= z - 1
            hd += 1
        return hd
