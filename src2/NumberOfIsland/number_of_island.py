class Solution:

    def traverseIsland(self, grid, col, line):
        if (line < 0 or self.lineNum <= line or col < 0 or self.colNum <= col or grid[line][col] == '0'):
            return

        grid[line][col] = '0'
        self.traverseIsland(grid, col, line + 1)
        self.traverseIsland(grid, col, line - 1)
        self.traverseIsland(grid, col + 1, line)
        self.traverseIsland(grid, col - 1, line)

    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        islandNum = 0
        self.lineNum = len(grid)
        if (self.lineNum == 0):
            return 0
        self.colNum = len(grid[0])

        for j in range(self.lineNum):
            grid[j] = list(grid[j])

        for j in range(self.lineNum):
            line = grid[j]
            for i in range(self.colNum):
                if (line[i] == '1'):
                    islandNum += 1
                    self.traverseIsland(grid, i, j)
        return islandNum

if __name__ == '__main__':
    print Solution().numIslands(["1011"])