class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = {}
        mat1 =[]
        for i in range(0,len(mat)):
            soldiers[i] = sum(mat[i])
        soldiers = dict(sorted(soldiers.items(), key = lambda x: x[1]))
        return([*soldiers][0:k])