class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = []
        for i in range(1,n+1):
            if(26 < k - n + i):
                s.append('z')
                k = k -26
            else:
                a = k - n + i
                s.append(chr(96+ a))
                k = k -a
        return ''.join(s[::-1])        