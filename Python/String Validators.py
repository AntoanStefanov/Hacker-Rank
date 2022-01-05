s = input()
# x = (c.isalnum() for c in s)
# could be done with generator expressions
# any(c.isalnum() for c in s), no [], but ()
print(any([c.isalnum() for c in s]))
print(any([c.isalpha() for c in s]))
print(any([c.isdigit() for c in s]))
print(any([c.islower() for c in s]))
print(any([c.isupper() for c in s]))