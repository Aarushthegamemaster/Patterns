print("The Half Pyramid Character is (*)")
a = int(input("Enter the number of rows you want to be:"))

for i in range(a):
    for j in range(i+1):
        print("*", end="")
    print()