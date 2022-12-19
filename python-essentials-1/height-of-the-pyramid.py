blocks = int(input("Number of blocks: "))

height = 0

block_used = 1
while block_used <= blocks:
    blocks -= block_used
    block_used += 1
    height += 1

print("The height of the pyramid: ", height)
