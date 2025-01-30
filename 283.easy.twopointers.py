class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = len(nums)-1
        while (r-l)>0:
            if nums[l] == 0:
                nums.pop(l)
                nums.append(0)
                r=r-1   # move the right pointer to the left
            elif nums[r] == 0:
                r=r-1
            else:
                l+=1
        print(nums)
        return nums

sol = Solution()  
sol.moveZeroes([1,0,0,2,3,0,5,12,0])

