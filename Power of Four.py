class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n.bit_length() & 1 and not(n & (n-1))
