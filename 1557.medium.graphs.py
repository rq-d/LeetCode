class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # indegree 0, have to be included bc they are otherwise unreachable

        # outdegree >0

        # identify nodes with 0 indegree
        
        # unnecessary step for this problem:
        # for each of those nodes, traverse the graph and mark places visited
        # if len(visited) == n then all nodes were visited when we started at those two so we are successeful, return those two nodes


        # get indegrees
        indegrees = [0 for _ in range(n)]
        for edge in edges:
            indegrees[edge[1]] += 1

        q = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)    # these are nodes with indegree 0, aka cannot be reached
    
        
        

        return q
# n=6 
# edges=[[0,1],[0,2],[2,5],[3,4],[4,2]]