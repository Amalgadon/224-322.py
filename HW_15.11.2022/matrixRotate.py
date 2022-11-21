import random

mat = []
HEIGHT = input("Введите длину массива: ")

if HEIGHT.isdigit():
    HEIGHT = int(HEIGHT)
else:
    print('The variable is not a number')
    exit()

WIDTH = input("Введите ширину массива: ")
if WIDTH.isdigit():
    WIDTH = int(WIDTH)
else:
    print('The variable is not a number')
    exit()


def Fill():
    global mat
    for _ in range(HEIGHT):
        row = []
        for _ in range(WIDTH):
            row.append(random.randint(10, 99))
        mat.append(row)

def Print():
    global mat
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(mat[x][y], end=' ')
        print()

def Left():
    global mat
    h, w = len(mat), len(mat[0])
    new_array = [[None] * h for _ in range(w)]
    for c in range(w - 1, -1, -1):
        for r in range(h):
            new_array[c][h - r - 1] = mat[r][c]
    mat = new_array.copy()


def Right():
    global mat
    h, w = len(mat), len(mat[0])
    new_array = [[None] * h for _ in range(w)]
    for c in range(w):
        for r in range(h - 1, -1, -1):
            new_array[w - c - 1][r] = mat[r][c]
    mat = new_array.copy()


def Mirror():
    global mat
    h, w = len(mat), len(mat[0])
    new_array = [[None] * h for _ in range(w)]
    for c in range(w):
        for r in range(h):
            new_array[r][c] = mat[w - r - 1][c]
    mat = new_array.copy()


Fill()
Print()

while True:
    command = input("Введите команду (a - повернуть налево, d - повернуть направо, s - отзеркалить): ").lower()

    if command == 'a':
        Left()
        Print()
    elif command == 'd':
        Right()
        Print()
    elif command == 's':
        Mirror()
        Print()