N, M = [int(x) for x in input().split(' ')]
# M = 3 * N


msg = 'WELCOME'.center(M, '-')
pattern = []
for i in range(N//2):
    pattern.append(('.|.' * (2 * i + 1)).center(M, '-'))
print('\n'.join(pattern))
print(msg)
print('\n'.join(pattern[::-1]))
