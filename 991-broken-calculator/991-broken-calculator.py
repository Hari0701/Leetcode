class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        counter = 0
        while( target > startValue):
            counter += 1
            if(target % 2):
                target += 1
            else:
                target = target//2
        return counter + startValue - target       