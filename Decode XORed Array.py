class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        L = []
        L.append(first)
        for i in range(len(encoded)):
            L.append(L[i]^encoded[i])
        return L
