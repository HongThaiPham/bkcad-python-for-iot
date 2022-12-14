# phep toan voi so phuc

# a = 2+3j
# b = 1+5j
# print("a + b = {}".format(a+b))
# print("a - b = {}".format(a-b))
# print("a * b = {}".format(a*b))
# print("a / b = {}".format(a/b))

# nhap du lieu tu ban phim
# f = float(input("Nhap so thuc: "))
# f *= 5
# print("f = {}".format(f))
# print("type of f = {}".format(type(f)))


# j1 = complex(input("Nhap so phuc thu nhat: "))
# j2 = complex(input("Nhap so phuc thu hai: "))

# print("AVG = {}".format((j1+j2)/2))


# nhap nhieu so
# inp = input("Nhap a, b, c: ")
# print(inp)
# a, b, c = inp.split(',')
# print(a, b, c, type(a), type(b), type(c))

# a, b, c = map(int, inp.split(','))
# print(a, b, c, type(a), type(b), type(c))


# nhap 3 chuoi cach nhau boi dau ;
str = input("nhap 3 chuoi cach nhau boi dau ; ")
# in ra cac chuoi vua nhap
str1, str2, str3 = str.split(';')
print("Cac chuoi vua nhap: ")
print(str1)
print(str2)
print(str3)
# chuoi thu 2 viet hoa toan bo
print("chuoi thu 2 viet hoa toan bo: {}".format(str2.upper()))
# chiue dai chuoi 2
print("chieu dai chuoi 2: {}".format(len(str1)))

sothuc = input("nhap 2 so thuc cach nhau boi dau phay: ")
f1, f2 = map(float, sothuc.split(','))
# trung binh cong
print("Trung binh cong = {}".format((f1+f2)/2))
print("Trung binh nhan = {:0,.2f}".format((f1*f2)**(1/2)))
