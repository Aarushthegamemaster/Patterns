print("The mirrored right triangle will be made out of '*'")
rows = int(input("How many rows do you want in the triangle:"))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * i)
