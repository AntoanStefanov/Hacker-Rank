l = []

n = int(input())

for _ in range(n):
    data = input().split()
    command = data[0]
    if command == 'insert':
        element = int(data[2])
        index = int(data[1])
        l.insert(index, element)
    elif command == 'print':
        print(l)
    elif command == 'remove':
        element = int(data[1])
        l.remove(element)
    elif command == 'append':
        element = int(data[1])
        l.append(element)
    elif command == 'sort':
        l.sort()
    elif command == 'pop':
        l.pop()
    elif command == 'reverse':
        l.reverse()
