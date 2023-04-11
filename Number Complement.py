class Solution:
    def findComplement(self, num: int) -> int:
        p = 2
        temp = num
        while(temp>>1):
            temp >>= 1
            p <<= 1
        return p - num - 1
