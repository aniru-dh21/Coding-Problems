class Solution:
    def maxDepth(self, s: str) -> int:
        L = []
        depth = 0
        for i in s:
            if i == '(':
                L.append(i)
                depth = max(depth, len(L))
            elif i == ')':
                L.pop()
        return depth
