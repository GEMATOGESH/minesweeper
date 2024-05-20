import copy
import random

# Параметры игры
number_of_mines = 5
field_x = 5
field_y = 5

# Глобальные переменные
field = None
player_field = None
revealed_tiles = 0


def create_field():
    """Создание игрового поля, заполнение его минами и числами
    """
    
    global field, player_field
    
    field = [None] * field_x
    for i in range(field_x):
        field[i] = [None] * field_x
    
    player_field = copy.deepcopy(field)

    indxs = []
    for _ in range(number_of_mines):
        while True:
            pretendent = random.randint(0, field_x * field_y - 1)
            if pretendent not in indxs:
                indxs.append(pretendent)
                break

    for i in range(0, field_x):
        for j in range(0, field_y):
            pos = i * field_y + j
            
            if pos in indxs:
                field[i][j] = "m" 
                
            player_field[i][j] = "?"
                
    for i in range(0, field_x):
        for j in range(0, field_y):
            if field[i][j] != "m":
                neighbors = []
                if i > 0 and j > 0: 
                    neighbors.append(field[i-1][j-1]) #NW
                if i > 0: 
                    neighbors.append(field[i-1][j]) #N
                if i > 0 and j < (field_x - 1): 
                    neighbors.append(field[i-1][j+1]) #NE
                if j > 0: 
                    neighbors.append(field[i][j-1]) #W
                if j < (field_x - 1): 
                    neighbors.append(field[i][j+1]) #E
                if i < (field_y - 1) and j > 0: 
                    neighbors.append(field[i+1][j-1]) #SW
                if i < (field_y - 1): 
                    neighbors.append(field[i+1][j]) #S
                if i < (field_y - 1) and j < (field_x - 1): 
                    neighbors.append(field[i+1][j+1]) #SE
                
                weight = 0
                for neighbor in neighbors:
                    if neighbor == "m":
                        weight += 1

                field[i][j] = weight


def reveal(i: int, j: int):
    """Рекурсивное открытие клетки по координатам (i, j)

    Параметры
    ----------
    i : int
        Позиция по оси Х на поле
    j : int
        Позиция по оси Y на поле

    Возвращает
    -------
    bool
        Безопасна ли клетка, False в случае открытия мины
    """
    global revealed_tiles
    
    if player_field[i][j] == "?":
        if field[i][j] == "m":
            return False
        
        player_field[i][j] = field[i][j]
        revealed_tiles += 1
        
        if field[i][j] == 0:
            if i > 0 and j > 0: 
                reveal(i-1, j-1) #NW
            if i > 0: 
                reveal(i-1, j) #N
            if i > 0 and j < (field_x - 1): 
                reveal(i-1, j+1) #E
            if j > 0: 
                reveal(i, j-1) #W
            if j < (field_x - 1): 
                reveal(i, j+1) #E
            if i < (field_y - 1) and j > 0: 
                reveal(i+1, j-1) #SW
            if i < (field_y - 1): 
                reveal(i+1, j) #S
            if i < (field_y - 1) and j < (field_x - 1): 
                reveal(i+1, j+1) #SE
        return True
    
    if player_field[i][j] != "?" and player_field[i][j] != "m":
        return True
    

def print_field():
    """Отображение текущего игрового поля
    """
    
    for i in range(0, field_x):
        for j in range(0, field_y):
            print(player_field[i][j], end="")
            
        print()


def print_classified_field():
    """Отображение всего игрового поля, включая мины, используется
    только для дебага!
    """
    
    for i in range(0, field_x):
        for j in range(0, field_y):
            print(field[i][j], end="")
            
        print()
        
        
def game_loop():
    """Основной игровой луп
    """
    
    create_field()
    print_field()

    while True:
        print("Enter i: ", end="")
        i = int(input())
        print("Enter j: ", end="")
        j = int(input())
        
        if (i > field_x) or (j > field_y) or (i < 1) or (j < 1):
            print("Wrong move!")
            continue
        
        res = reveal(i - 1, j - 1)
        
        if not res:
            print("BOOM!")
            break
        
        if revealed_tiles == field_x * field_y - number_of_mines:
            print("WIN!")
            break
        
        print_field()
        

game_loop()