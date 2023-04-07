class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s1 = '../'
        s2 = './'
        L = []
        for i in logs:
            if i == s1:
                if len(L) > 0:
                    L.pop()
            elif i == s2:
                continue
            else:
                L.append(i)
        return len(L)
