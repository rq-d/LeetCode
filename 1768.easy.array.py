class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        newstr = ""

        if len(word1) > len(word2):
            for i in range(len(word2)):
                newstr += word1[i]
                newstr += word2[i]
            
            newstr += word1[len(word2):]

        elif len(word1) < len(word2):
            for i in range(len(word1)):
                newstr += word1[i]
                newstr += word2[i]

            newstr += word2[len(word1):]

        else:
            for i in range(len(word1)):
                newstr += word1[i]
                newstr += word2[i]
        return newstr