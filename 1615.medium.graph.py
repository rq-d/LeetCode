# my solution!
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
  
        degree = [0 for _ in range(n)]  # index is node and value is degree of that node

        # get the degree of each node
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1

        print(degree)

        # network rank between two cities
        def rank(cityA, cityB):
            r = degree[cityA] + degree[cityB]
            if ([cityA, cityB] in roads) or ([cityB, cityA] in roads):
                r -= 1
            return r
        best = 0

        # need to compare every combination from 0 to n-1, to get max network rank
        for i in range(n):
            for j in range(n):
                if i!=j:
                    r=rank(i,j)
                    best = max(best,r)
        return best