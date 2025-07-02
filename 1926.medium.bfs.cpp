#include <deque>

class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        
        int rows = maze.size();
        int cols = maze[0].size();
        std::vector<std::pair<int, int>> dirs = {{-1,0}, {1,0}, {0,1}, {0,-1}};

        // First place in the queue
        std::queue<std::array<int, 3>> dq; // row, col, dist from start
        dq.push({entrance[0], entrance[1], 0});  // adds element to the back of the queue

        maze[entrance[0]][entrance[1]] = '+';

        while(!dq.empty()){
            auto [currRow, currCol, currDist] = dq.front(); //returns front element of queue but does not remove it
            dq.pop(); // removes the frontmst element (BFS)

            // move in whichever direction exists and has been unvisited
            for(auto dir : dirs){
                int nextRow = dir.first + currRow;
                int nextCol = dir.second + currCol;
                
                // if this is a valid move its within bounds and marked with . in the maze
                if(nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols && maze[nextRow][nextCol] == '.'){
                    // check if this is the exit
                    if(nextRow == 0 || nextRow == rows-1 || nextCol == 0 || nextCol == cols-1){
                        return currDist + 1;
                    }
                    // otherwise add this to the que and mark as visited
                    dq.push({nextRow, nextCol, currDist+1}); // adds to the back of the queue
                    maze[nextRow][nextCol] = '+';   // 
                }
            }
        }
        return -1;
    }
};