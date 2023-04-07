lass Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels = sorted(jewels)
        for i in jewels:
            if i in stones:
                count += stones.count(i)
        return count
