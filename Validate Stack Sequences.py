class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        while(i<len(pushed)):
            if i>-1 and pushed[i] == popped[j]:
                pushed.pop(i)
                i-=1
                j+=1
            else:
                i+=1
        i = len(pushed)-1
        while(j<len(popped)):
            if pushed[i]!=popped[j]:
                return False
            j+=1
            i-=1
        return True
