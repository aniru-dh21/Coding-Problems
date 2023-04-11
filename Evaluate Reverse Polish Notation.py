class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        L = []
        for i in tokens:
            if i == '+':
                m = int(L.pop())
                n = int(L.pop())
                L.append(n+m)
            elif i == '-':
                m = int(L.pop())
                n = int(L.pop())
                L.append(n-m)
            elif i == '*':
                m = int(L.pop())
                n = int(L.pop())
                L.append(n*m)
            elif i == '/':
                m = int(L.pop())
                n = int(L.pop())
                L.append(int(n/m))
            else:
                L.append(int(i))
        return L[0]
