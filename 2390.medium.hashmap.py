class Solution:
    def removeStars(self, s: str) -> str:
        
        a = [ch for ch in s]
       

        i=0
        while i < len(a):

            popped = 0

            if a[i] == '*':
                a.pop(i)
                popped+=1
                if a[i-1] != '*':
                    a.pop(i-1)
                    popped+=1
                
                i -= popped # move cursor to the correct character
                

            i+=1
        print(a)
        return "".join(a) 