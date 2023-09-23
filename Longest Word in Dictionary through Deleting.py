class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for i in dictionary:
            j = 0
            for k in s:
                if j < len(i) and k == i[j]:
                    j += 1
                    if j == len(i):
                        break
            if j == len(i):
                return i
        return ""
