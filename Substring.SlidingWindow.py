# 3. Longest Substring Without Repeating Characters

s = "pwwkew"

# sliding window
charSet = set()
l = 0
r=0
res = 0

for r in range(len(s)):

  while s[r] in charSet: # we found a repeated character, so remove the left most character from the substring
    charSet.remove(s[l])
    l+=1  # shift the window


  charSet.add(s[r]) # now add the new character
  res = max(res, r-l+1) # count the number of characters in the substring and compare to previous result

print (res)