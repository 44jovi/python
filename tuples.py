# Tuples are immutable. One way to update a tuple:
x = ("apple", "banana", "cherry")
print(x) # => ('apple', 'kiwi', 'cherry')
y = list(x)
y[2] = 'not cherry anymore'
x = tuple(y)
print(x) # => ('apple', 'kiwi', 'not cherry anymore')
