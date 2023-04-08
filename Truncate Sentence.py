class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        L = s.split()[:k]
        return ' '.join(L)
