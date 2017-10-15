# https://leetcode.com/problems/island-perimeter/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        p = 0
        x = len(grid[0])
        y = len(grid)
        grid_new = []
        for i in range(y+2):
            grid_new.append([0]*(x+2))
        
        for i in range(y):
            for j in range(x):
                grid_new[i+1][j+1] = grid[i][j]
                
        for y in range(len(grid_new)):
            for x in range(len(grid_new[0])):
                if grid_new[y][x]:
                    if not grid_new[y-1][x]:
                        p += 1
                    if not grid_new[y][x-1]:
                        p += 1
                    if not grid_new[y][x+1]:
                        p += 1
                    if not grid_new[y+1][x]:
                        p += 1
        return p
