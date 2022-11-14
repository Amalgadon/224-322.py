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

mat = [[nofill]*height for i in range(width)]

h = 0
w = 0
for i in range(0, width, 2):
    if i == 0:
        for j in range(h, height):
            mat[w][j] = fill
        h = height - 1

        for j in range(w, width):
            mat[j][h] = fill
        w = width - 1

        for j in range(h, -1, -1):
            mat[w][j] = fill
        h = 0
    else:
        if i < width // 2 + 1:
            for j in range(w, i-1, -1):
                mat[j][h] = fill
            w = i

            for j in range(h, height - i):
                mat[w][j] = fill
            h = height - i - 1

            for j in range(i, width - i):
                mat[j][h] = fill
            w = width - i - 1

            for j in range(h, i - 1, -1):
                mat[w][j] = fill
            h = i


#Вывод результата на экран
for i in range(width):
    for j in range(height): 
        print(mat[i][j], end="")
    print()



