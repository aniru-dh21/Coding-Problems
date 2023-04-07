class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        L = []
        for i in range(len(prices)):
            while L and (prices[L[-1]] >= prices[i]):
                prices[L.pop()] -= prices[i]
            L.append(i)
        return prices
