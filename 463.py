class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        p = 0
        for rl in range(len(grid)):
            for cl in range(len(grid[0])):
                if (grid[rl][cl] == 1):
                    n = 0
                    if (rl-1>=0 and grid[rl-1][cl] == 1):
                        n+=1
                    if (rl+1<len(grid) and grid[rl+1][cl] == 1):
                        n+=1
                    if (cl-1>=0 and grid[rl][cl-1] == 1):
                        n+=1
                    if (cl+1<len(grid[0]) and grid[rl][cl+1] == 1):
                        n+=1
                    
                    p+=(4-n)
        return p
                    
