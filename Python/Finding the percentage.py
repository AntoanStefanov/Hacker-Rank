n = int(input())
diary = {}
for _ in range(n):
    info = input().split()
    name = info[0]
    marks = [float(x) for x in info[1:]]
    diary[name] = marks
query_name = input()

print(f'{sum(diary[query_name]) / len(diary[query_name]):.2f}')
