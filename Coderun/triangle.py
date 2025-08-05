# https://coderun.yandex.ru/problem/triangle

a = int(input())
b = int(input())
c = int(input())

if (a + b) > c and (c + b) > a and (a + c) > b:
    print('YES')
else:
    print('NO')