class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0]*n for i in range(n)]
        left,right=0,n
        top,bottom=0,n
        counter=1

        
        while left<right and top<bottom:
            for i in range(left,right):
                res[top][i]=counter
                counter+=1
            top+=1
            
            for i in range(top,bottom):
                res[i][right-1]=counter
                counter+=1
            right-=1
            
            if not (left<right and top<bottom):
                break
            
            for i in reversed(range(left,right)):
                res[bottom-1][i]=counter
                counter+=1
            bottom-=1
            
            for i in reversed(range(top,bottom)):
                res[i][left]=counter
                counter+=1
            left+=1
        
        return res
            