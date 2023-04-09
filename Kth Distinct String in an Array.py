class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        L = []
        for key, value in d.items():
            if d.get(key) == 1:
                L.append(key)
        if k > len(L):
            return ""
        else:
            return L[k-1]
