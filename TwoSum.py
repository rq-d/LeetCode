class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        length = len(nums)
        print("length", length)
        for i in range(length): # iterate through every character
            thisNum = nums[i]

            # compare against every other number
            for j in range(1,length):
                print("i,j ",i,j)
                nextIdx = (i+j) % (length)
                print("next index ", nextIdx)
                sum=thisNum+nums[nextIdx]
                print("sum ",sum)
                if(sum==target):
                    return i,nextIdx


          return 0,0