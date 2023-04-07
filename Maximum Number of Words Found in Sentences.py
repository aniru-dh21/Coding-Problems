class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for i in sentences:
            l = len(i.split())
            count = max(l,count)
        return count
