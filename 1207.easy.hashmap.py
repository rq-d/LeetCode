class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        def numOccurences(anum,alist):
            ctr = 0
            for a in alist:
                if a == anum:
                    ctr+=1
            return ctr

        occDict = {}

        for number in arr:
            if number in occDict:
                continue
            else:
                occDict[number] = numOccurences(number,arr)

        # check if values in occDict are unique
        aSet = set()
        for val in occDict.values():
            if val not in aSet:
                aSet.add(val)
            else:
                return False
        return True
    
 # [1,2,2,1,1,3]