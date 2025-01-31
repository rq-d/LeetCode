
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rows = {}
        cols = {}

        # save each row into a dict
        for row in grid:
            rowStr = '_'.join(map(str, row))
            if rowStr not in rows.keys():
                rows[rowStr] = 1
            else: # if this key exists then iterate
                rows[rowStr] += 1

        for col in zip(*grid):
            colStr = '_'.join(map(str, col))
            if colStr not in cols.keys():
                cols[colStr] = 1
            else: # if this key exists then iterate
                cols[colStr] += 1

        print(rows)
        print(cols)

        ctr = 0
        for row in rows.keys():
            for col in cols.keys():
                if row == col:
                    ctr+= rows[row]*cols[col]

        return ctr
·