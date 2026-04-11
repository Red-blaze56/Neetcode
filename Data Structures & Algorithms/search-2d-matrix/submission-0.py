class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for rows in matrix:
            if target in rows:
                return True
        return False