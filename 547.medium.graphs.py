class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:


        # traverse the matrix from top to bottom,

        # go directly to the first connected nodes, and keep track of visited

        # everytime we start a new traversal at the outer loop, that s a new province

        self.visited = set()

        def traverse(i):
            for j in range(len(isConnected[i])):     # traverse this column
                if (isConnected[i][j]) and (j not in self.visited):   
                    self.visited.add(j)
                    traverse(j)

        providences = 0
        for i in range(len(isConnected)): # i is a node

            # find nodes connected to i by traversing each element in this row
            if i not in self.visited:
                self.visited.add(i)
                providences +=1 
                traverse(i)

        return providences