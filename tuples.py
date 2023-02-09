# Tuples are immutable. One way to update a tuple:
x = ('apple', 'banana', 'cherry')
print(x) # => ('apple', 'kiwi', 'cherry')
y = list(x)
y[2] = 'not cherry anymore'
x = tuple(y)
print(x) # => ('apple', 'kiwi', 'not cherry anymore')

# But mutable items within a tuple can be reassigned:
t1 = (1, 2, 3, [4, 5])
t1[3][1] = 'no longer integer 5!'
print(t1) # => (1, 2, 3, [4, 'no longer integer 5!'])
