size = int(input("Enter the size of the pattern: "))
row = size

while row > 0:
    for symbol in range(0, size):
        print("*", end="")
    print("")
    row-=1
        