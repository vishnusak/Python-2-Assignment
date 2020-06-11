# Create a Python Generators to generate the vowels. This should be a cyclic generators and will generate infinte list of vowels.

def vowels():
    v = ['a', 'e', 'i', 'o', 'u']
    idx = 0
    while True:
        yield v[idx]
        idx = idx + 1 if idx < 4 else 0

a = vowels()
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))