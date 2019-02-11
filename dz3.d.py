import sys
words = {}
text = sys.stdin.read()
for i in text.split():
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

max_word = None
max_number = 0
for word, n in sorted(words.items()):
    if n > max_number:
        max_number = n
        max_word = word


print(max_word)