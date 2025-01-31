class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        

        def instring(a,str):
            
            for ch in str:
                if ch == a:
                    return True
            return False

        res = [[],[]]
        set1= set()
        set2 = set()
        for num in nums1:
            if not instring(num,nums2):
                set1.add(num)
            
        for num in nums2:
            if not instring(num,nums1):
                set2.add(num)
        
        for num in set1:
            res[0].append(num)

        for num in set2:
            res[1].append(num)

        return res

