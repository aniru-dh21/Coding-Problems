class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compare(s):
            L = []
            for i in range(len(s)):
                if not len(L) and s[i] == '#':
                    continue
                elif s[i] == "#":
                    L.pop(0)
                else:
                    L.insert(0, s[i])
            return L
        s1 = compare(s)
        s2 = compare(t)
        return s1 == s2
