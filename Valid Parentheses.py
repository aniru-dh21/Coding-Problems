class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','{':'}','[':']'}
        L = []
        for i in s:
            if i in d:
                L.append(i)
            elif len(L) == 0 or d[L.pop()] != i:
                return False
        return len(L) == 0
