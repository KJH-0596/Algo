import heapq

n = int(input())
    
left = []
right = []

for x in range(n):
    number = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -number)
    else:
        heapq.heappush(right, number)
    
    if right and right[0] < -left[0]:
        leftValue = heapq.heappop(left)
        rightValue = heapq.heappop(right)

        heapq.heappush(left, -rightValue)
        heapq.heappush(right, -leftValue)
    
    print(-left[0])