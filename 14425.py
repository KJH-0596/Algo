n, m = map(int, input("").split(" "))

wordset = []
words = []
for x in range(n):
    wordset.append(input())
for m in range(m):
    words.append(input())

cnt = 0
for word in words:
    if word in wordset:
        cnt += 1
    else:
        continue

print(cnt)