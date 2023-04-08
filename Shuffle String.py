class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = ''
        for i in range(len(indices)):
            t += s[indices.index(i)]
        return t
