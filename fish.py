class Solution:


    def findMaxFish(self, grid: List[List[int]]) -> int:

        # Depth First Search
        def dfs(r,c):
            if(r < 0 or c<0 or # out of bounds
            r==ROWS or c == COLS or # out of bounds
            grid[r][c] == 0 or visit[r][c]):    # land or been visited
                return 0

            visit[r][c] = True
            res = grid[r][c] # this is a local in scope
            print("res: ",res)
            neighbors = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]

            # unpack neighbor row and neighbor columns
            for nr, nc in neighbors:
                res += dfs(nr, nc) # recursive call (the above if statement will protect us in the subsequent calls)
                print("res after recursive sum ", res)

            print("res returned: ", res)
            return res




        ROWS, COLS = len(grid), len(grid[0])
        visit = [[False for row in range(ROWS)] for col in range(COLS)]
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and not(visit[r][c]):  # if nonzero grid location and coordinate has not been visited
                    print("called dfs on row col: ", r,c)

                    res = max(res,dfs(r,c))

        return res