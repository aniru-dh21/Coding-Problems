class Solution:
    def decodeString(self, s: str) -> str:
        L = []
        for i in s:
            if i != ']':
                L.append(i)
            else:
                result = ''
                while L[-1] != '[':
                    result += L.pop()
                L.pop()
                n = ''
                while len(L) != 0 and L[-1].isdigit() == True:
                    n += L.pop()
                L.append(result*int(n[::-1]))
        return ''.join([j[::-1] for j in L])
