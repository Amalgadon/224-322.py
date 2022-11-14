fill = "██"
nofill = "  "
height = input("Введите длину: ")

if height.isdigit():
    height = int(height)
else:
    print('The variable is not a number')
    exit()

width = input("Введите ширину: ")
if width.isdigit():
    width = int(width)
else:
    print('The variable is not a number')
    exit()

for i in range (width):
    for j in range(height):
        if (i % 2 == 0 or (j == height - 1 and i % 4 == 1) or (j == 0 and i % 4 == 3)):
            print(fill, end="")
        else:
            print(nofill, end="")

    print()