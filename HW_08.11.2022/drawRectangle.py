fill = "██"
nofill = "  "
height = input("Введите длину прямоугольника: ")

if height.isdigit():
    height = int(height)
else:
    print('The variable is not a number')
    exit()

width = input("Введите ширину прямоугольника: ")
if width.isdigit():
    width = int(width)
else:
    print('The variable is not a number')
    exit()

isFill = input("Закрасить [Y/N] ").lower() == "y"

for i in range (width):
    for j in range(height):
        if isFill or i == 0 or i == width - 1 or j == 0 or j == height - 1:
            print(fill, end="")
        else:
            print(nofill, end="")

    print()