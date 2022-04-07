class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
#         sort the stones 
        stones = sorted(stones)
    
        if(len(stones) == 1):
            return stones[0]
        
        elif(len(stones) >= 2):
            y = stones[-1]
            stones.pop()
            x = stones[-1]
            stones.pop()
            stones.append(y - x)
            
        return self.lastStoneWeight(stones)    