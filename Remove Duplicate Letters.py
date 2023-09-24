class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        L = []
        seen = set()
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        for i, char in enumerate(s):
            if( char in seen):
                continue
            else:
                while( L and L[-1] > char and d[L[-1]] > i):
                    removed = L.pop()
                    seen.remove(removed)
                seen.add(char)
                L.append(char)
        return ''.join(L)
