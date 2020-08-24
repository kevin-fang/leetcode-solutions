class Solution(object):
    def dfsHelper(self, x, y, grid):
        done = []
        stack = []
        stack.append((x, y))
        while len(stack) > 0:
            x, y = stack.pop()
            if (x, y) in done or grid[y][x] == '0':
                continue
            done.append((x, y))
            if (x - 1 >= 0):
                stack.append((x - 1, y))
            if (x + 1 < len(grid[0])):
                stack.append((x + 1, y))
            if (y - 1 >= 0):
                stack.append((x, y - 1))
            if (y + 1 < len(grid)):
                stack.append((x, y + 1))
            grid[y][x] = '0'

    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_bodies = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    self.dfsHelper(x, y, grid)
                    num_bodies += 1

        return num_bodies
