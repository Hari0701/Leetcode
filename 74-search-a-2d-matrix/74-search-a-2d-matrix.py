class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0,len(matrix)):
            if(matrix[i][-1]) < target:
                continue
            else:
                low = 0
                high = len(matrix[i]) - 1
                while(low <= high):
                    mid = (low-high)//2 + high
                    if(matrix[i][mid] > target):
                        high = mid - 1
                    elif(matrix[i][mid] < target):
                        low = low + 1
                    elif(matrix[i][mid]  == target):
                        return True
                    else:
                        return False