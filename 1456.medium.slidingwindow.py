class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        def numVowels(l):
            num = 0
            for i in range(k):
                thisletter = s[l+i]
                if thisletter in ('a', 'e', 'i', 'o', 'u'):
                    num+=1

            return num

        l = 0
        res = 0
    

        while l <= len(s) - k:
            res = max(res, numVowels(l))
            l+=1
        return res
    

sol = Solution()

print(sol.maxVowels("weallloveyou",7))