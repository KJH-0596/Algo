def cal(a, b, c):
    if b == 1:
        return a % c
    else:
        k = cal(a, b//2, c)
        if b % 2 == 0: # b가 짝수일때
            return (k*k)%c
        else: # b가 홀수일때
            return (k*k*a)%c
        
a, b, c = map(int, input().split(" "))
print(cal(a, b, c))