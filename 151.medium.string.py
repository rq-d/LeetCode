
s = "a good   example"
words = []
word = ""
for chr in s:

    if chr==" ":
        words.append(word)
        word = ""
        continue

    word += chr
words.append(word)

res = ""
for el in words:
    if el != '':
      res = el + " " + res

# edge cases
while res[-1] == " ":
    res = res[:-1]

while res[0] == " ":
    res = res[1:]
    