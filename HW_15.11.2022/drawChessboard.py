Pawn = "\u2659" # Пешка
Rook = "\u2656" # Тура
Khignt = "\u2658" # Конь
Bishop = "\u2657" # Офицер
Queen = "\u2655" # Ферзь
King = "\u2654" # Король

def drawFigure(code, isWhiteFig, isWhiteSquare):
    if isWhiteFig:
        if isWhiteSquare:
            print("\033[0;37;47m {}  \033[0m".format(code), end="") # Белый на белом
        else:
            print("\033[0;37;40m {}  \033[0m".format(code), end="") # Белый на черном
    else:
        if isWhiteSquare:
            print("\033[0;30;47m {}  \033[0m".format(code), end="") # Черный на белом
        else:
            print("\033[0;30;40m {}  \033[0m".format(code), end="") # Черный на черном

    

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            color = j % 2 == 0
        else:
            color = j % 2 == 1
        if i == 0:
            if j == 0 or j == 7:
                drawFigure(Rook, False, color)
            elif j == 1 or j == 6:
                drawFigure(Khignt, False, color)
            elif j == 2 or j == 5:
                drawFigure(Bishop, False, color)
            elif j == 3:
                drawFigure(Queen, False, color)
            else:
                drawFigure(King, False, color)
        elif i == 1:
            drawFigure(Pawn, False, color)
        elif i == 6:
            drawFigure(Pawn, True, color)
        elif i == 7:
            if j == 0 or j == 7:
                drawFigure(Rook, True, color)
            elif j == 1 or j == 6:
                drawFigure(Khignt, True, color)
            elif j == 2 or j == 5:
                drawFigure(Bishop, True, color)
            elif j == 3:
                drawFigure(Queen, True, color)
            else:
                drawFigure(King, True, color)
        else:
            drawFigure(" ", False, color)
    print()