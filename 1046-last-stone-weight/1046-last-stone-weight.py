class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        if(len(stones) == 1):
            return stones[0]
        elif(len(stones) >= 2):
            heaviestTwo = stones[-1] - stones[-2]
            stones = stones[:len(stones)-2]
            stones.append(heaviestTwo)
        return self.lastStoneWeight(stones)    