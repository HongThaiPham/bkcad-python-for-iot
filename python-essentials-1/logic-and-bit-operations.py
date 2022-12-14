i = 15
j = 22

log = i and j
print(log)

bit = i & j
print(bit)

logneg = not i
print(logneg)

bitneg = ~i
print(bitneg)

print(i | j)
print(i ^ j)

x = 1
y = 0

z = ((x == y) and (x == y)) or not (x == y)
print(not (z))

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
