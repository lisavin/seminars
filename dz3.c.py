import sys
n = 0
words = {}
text = sys.stdin.read()
for i in text.split():
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

print(len(words))
