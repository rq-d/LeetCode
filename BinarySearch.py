class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # binary search
        l = 0
        r = len(nums)-1

        while l <= r:
            # get mid index
            mid = (l+r) // 2 # round down to whole number

         
            if(nums[mid] < target): # target is to the right
                l = mid + 1
            elif(nums[mid] > target): # target is to the left
                r = mid - 1
            else: # must be equal to the target
                return mid

        return l