class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i, j, k = 0, 0, 0
        for l in range(1, len(arr)):
            if (j and arr[l-1] < arr[l]) or arr[l-1] == arr[l]:
                i, j = 0, 0
            i += arr[l-1] < arr[l]
            j += arr[l-1] > arr[l]
            if i and j:
                k = max(k, i + j + 1)
        return k
