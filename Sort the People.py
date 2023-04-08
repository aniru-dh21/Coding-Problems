class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        L = []
        for i in sorted(heights)[::-1]:
            L.append(names[heights.index(i)])
        return L
