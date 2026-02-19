n = int(input())
balloon = list(map(int, input().split(" ")))
balloonList = [0 for i in range(1000001)]

result = 0
for i in balloon:
    if balloonList[i] == 0:
        balloonList[i-1] += 1
        result += 1
    else:
        balloonList[i] -= 1
        balloonList[i-1] += 1

print(result)