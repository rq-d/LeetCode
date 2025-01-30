class Solution:
    def maxArea(self, height) -> int:
        
        # two pointer
        l = 0
        r = len(height) - 1
        area = 0

        while (r-l) > 0:
            
            if height[l] < height[r]:
                area = max(area, height[l] * (r-l) ) # calc area using lower height and use max(old,new)
                l += 1 # move the left pointer
            
            elif height[l] > height[r]:
                area = max(area, height[r] * (r-l) )
                r -= 1 # move the right pointer toward the left

            else: # if heights are equal move either one
                area = max(area,height[r] * (r-l))
                r -= 1
        
        return area
    
sol = Solution()

print(sol.maxArea([1,8,6,2,5,4,8,3,7]))

print(sol.maxArea([1,1]))
