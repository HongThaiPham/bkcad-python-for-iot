# inra day 1*5*7*9....*101

# for i in range(1, 102, 2):
#     print(i, end="")
#     if i < 101:
#         print('*', end="")


# in ra so nguyen chan trong doan va tinh tong
# sum = 0
# for j in range(2, 1001, 2):
#     if j % 3 == 0 and j % 7 == 0:
#         sum += j
#         print(j, end="\t")

# print("\nSUM = {}".format(sum))

# a,b nhap tu ban phim
# a, b = map(int, input(" Nhap a, b:").split(','))
# if a % 2 != 0:
#     a += 1

# sum = 0
# for j in range(a, b, 2):
#     if j % 3 == 0 and j % 7 == 0:
#         sum += j
#         print(j, end="\t")

# print("\nSUM = {}".format(sum))

for i in range(13, 501, 2):
    if i % 11 == 0 and i % 13 == 0:
        print(i)
        break
else:
    print(None)
