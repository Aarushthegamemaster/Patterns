a = int(input("Enter how many rows you want in the triangle:"))
b = 1

for i in range(1,a+1):
    for j in range(1,i+1):
        print(b, end='')
        b = b+1
    print()