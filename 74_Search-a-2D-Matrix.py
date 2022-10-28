class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        rt, rb = 0, ROWS-1
        
        while rt<=rb: 
            rm = (rt + rb) // 2 
            if target < matrix[rm][0]:
                rb = rm - 1
            elif target > matrix[rm][-1]:
                rt = rm + 1
            else: 
                break
        
        l, r = 0, COLS -1
        while l<=r:
            m = (l+r) // 2 
            if target < matrix[rm][m]:
                r = m -1 
            elif target > matrix[rm][m]: 
                l = m + 1
            else:
                return True 
        return False
