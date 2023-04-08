class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = 0
        for i in range(len(s)):
            n ^=  ord(s[i]) ^ ord(t[i])
        n ^= ord(t[-1])
        return chr(n)
