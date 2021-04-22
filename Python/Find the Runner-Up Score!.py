n = int(input())
arr = list(map(int, input().split()))

max_num = max(arr)
arr.remove(max(arr))
while max_num in arr:
    arr.remove(max(arr))

print(max(arr))
