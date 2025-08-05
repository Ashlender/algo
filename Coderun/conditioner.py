# https://coderun.yandex.ru/problem/conditioner

t_room, t_cond = map(int, input().split())
mode = input()

if mode == "heat":
    print(max(t_room, t_cond))
elif mode == "freeze":
    print(min(t_room, t_cond))
elif mode == "auto":
    print(t_cond)
elif mode == "fan":
    print(t_room)