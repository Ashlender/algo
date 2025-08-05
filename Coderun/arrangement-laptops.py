# https://coderun.yandex.ru/problem/arrangement-laptops

a, b, c, d = map(int, input().split())

options = [
    (max(a, c), b + d),
    (max(a, d), b + c),
    (max(b, c), a + d),
    (max(b, d), a + c),
]

w, h = min(options, key=lambda x: x[0] * x[1])

print(w, h)