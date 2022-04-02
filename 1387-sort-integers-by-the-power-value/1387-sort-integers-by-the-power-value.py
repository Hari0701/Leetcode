class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        val = {}
        for i in range(lo, hi + 1):
            lo = i
            count = 0
            while i != 1:
                count +=1
                i = i / 2 if i % 2 == 0 else 3*i + 1
            val[lo] = count
        return sorted(val.items(), key = lambda x: x[1])[k-1][0]      
                        
        