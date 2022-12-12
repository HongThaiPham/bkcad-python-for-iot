print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

print("Hello\nworld")
# \n: new line
print("Hello\tworld")
# \t: \tab

# In ra dòng sau:  Hello world, welcome to "Python"
# Trong do: s1 = Hello world ; s2 = welcome to "Python"

print("Hello world", "welcome to \"Python\"", sep=", ")

n = 5
s = "s"
print("You have {1} apple{0}".format(n, s))


hoTen = "Pham Hong Thai"
noiLamViec = "LHU"
print("Toi ten la {}; dang lam viec tai \'{}\'".format(hoTen, noiLamViec))


price = 5000
print("{:0,.2f} vnd".format(price))
