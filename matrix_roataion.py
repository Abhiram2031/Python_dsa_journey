today i solved leetcode codes daily challenge problem
i learned about matrix transformation with neat and clean code
#code
class Solution:
    def findRotation(self, mat, target):
        n = len(mat)
        
        def rotate(matrix)
            return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
        
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False
