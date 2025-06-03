class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        

        color = {}


        for node in range(len(graph)):  # do dfs on every node
            if node not in color:   # check if this node has been visited and colored
                q = [node]
                color[node]=0   # color it something arbitrary, color its freinds something else
                while q:
                    node = q.pop()  # take the right most element (dfs)

                    # visit its neighbors
                    for nei in graph[node]:
                        if nei not in color:
                            q.append(nei)
                            color[nei] = color[node] ^ 1    # this is an XOR operator on 0 or 1, basically ensures that color[nei] is opposite color of color[node]
                            print(color[nei])
                        elif color[nei] == color[node]:
                            return False


        return True