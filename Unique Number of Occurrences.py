class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        L = []
        for key, value in d.items():
            L.append(d.get(key))
        return len(L) == len(set(L))
