class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        L = []
        for i in range(len(arr)-2):
            if arr[i+1] - arr[i] == arr[i+2] - arr[i+1]:
                L.append('true')
            else:
                L.append('false')
        if 'false' in L:
            return False
        else:
            return True
