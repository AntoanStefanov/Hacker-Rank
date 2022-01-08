def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        binary = bin(i)
        print(f'{str(i).rjust(width)} {str(oct(i))[2:].rjust(width)} {str(hex(i))[2:].upper().rjust(width)} {str(binary)[2:].rjust(width)}')

n = int(input())
print_formatted(n)
