class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        L = []
        for i in num:
            while(L and int(L[-1]) > int(i) and k):
                L.pop()
                k -= 1
            L.append(str(i))
        while(k):
            L.pop()
            k -= 1
        i = 0
        while(i<len(L) and L[i] == "0"):
            i += 1
        return ''.join(L[i:]) if (len(L[i:]) > 0) else "0"
