import copy
import random

number_of_mines = 5
field = None
player_field = None
field_x = 5
field_y = 5


def create_field():
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
                    neighbors.append(field[i-1][j-1])
                if i > 0: 
                    neighbors.append(field[i-1][j])
                if i > 0 and j < (field_x - 1): 
                    neighbors.append(field[i-1][j+1])
                if j > 0: 
                    neighbors.append(field[i][j-1])
                if j < (field_x - 1): 
                    neighbors.append(field[i][j+1])
                if i < (field_y - 1) and j > 0: 
                    neighbors.append(field[i+1][j-1])
                if i < (field_y - 1): 
                    neighbors.append(field[i+1][j])
                if i < (field_y - 1) and j < (field_x - 1): 
                    neighbors.append(field[i+1][j+1])
                
                weight = 0
                for neighbor in neighbors:
                    if neighbor == "m":
                        weight += 1

                field[i][j] = weight


def print_field():
    for i in range(0, field_x):
        for j in range(0, field_y):
            print(player_field[i][j], end="")
            
        print()


def print_classified_field():
    for i in range(0, field_x):
        for j in range(0, field_y):
            print(field[i][j], end="")
            
        print()


create_field()
print_classified_field()
print("-------")
print_field()
