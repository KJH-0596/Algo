n = int(input())
 
for _ in range(n):
    str = input()
 
    while True:
        if str == '':
            print('YES')
            break
        elif '()' not in str:
            print('NO')
            break
        else:
            str = str.replace('()', '')
