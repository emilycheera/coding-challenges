# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        
        y = cols - 1
        x = 0
        most_left_col = None
        
        while y >= 0 and 0 <= x < rows:
            if binaryMatrix.get(x, y) == 1:
                most_left_col = y
                y -= 1
            else:
                x += 1
        
        if most_left_col == None:
            return -1
        return most_left_col