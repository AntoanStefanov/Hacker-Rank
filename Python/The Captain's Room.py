size_of_group = int(input())
rooms = input().split()

unique_rooms = set(rooms)
for num in unique_rooms:
    count = 0
    for member in rooms:
        if num == member:
            count += 1
            if count > 1:
                break
    else:
        print(num)
        break
