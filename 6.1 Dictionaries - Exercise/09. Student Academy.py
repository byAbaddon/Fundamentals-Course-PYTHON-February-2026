di = {}

for _ in range(int(input())):
    n, g = input(), float(input())
    di.setdefault(n, []).append(g)

for k, v in di.items():
    ave = sum(v) / len(di[k])
    if ave >= 4.5:
        print(f'{k} -> {ave:.2f}')
