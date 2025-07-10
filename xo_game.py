from operator import truediv


def check_rows(step, field):
    for i in range(len(field)):
        k = 0
        for j in range(len(field)):
            if field[i][i] == field[i][j] == step:
                k += 1
        if k == len(field):
            return True
        k = 0
    return False

def check_columns(step, field):
    k = 0
    for i in range(len(field)):
        for j in range(len(field)):
            if field[j][i] == step:
                k += 1
        if k == len(field):
            return True
        k = 0
    return False

def check_secondary_diagonal(step, field):
    check = False
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][len(field) - 1 - i] == step:
                check = True
            else:
                return False
    return check == True

def check_main_diagonal(step, field):
    check = False
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][i] == step:
                check = True
            else:
                return False
    return check == True


def make_field(field):
    for i in range(len(field)):
        for j in range(len(field)):
            print(field[i][j], end='\t')
        print('\n')

n = int(input('Enter size  = '))

field_t = [['_' for i in range(n)] for j in range(n)]

winnerX = False
winnerO = False

def check_winner(step, fld):
    if check_rows(step, fld):
        print('rows')
        return True
    elif check_columns(step, fld):
        print('columns')
        return True
    elif check_main_diagonal(step, fld):
        print('main_diagonal')
        return True
    elif check_secondary_diagonal(step, fld):
        print('secondary_diagonal')
        return True
    else:
        return False


while winnerX != True or winnerO != True:
    x = input('Enter x = ')
    if x == 's':
        print('GAME OVER')
        break
    field_t[int(x[0])][int(x[1])] = 'x'
    make_field(field_t)

    o = input('Enter o = ')
    if o == 's':
        print('GAME OVER')
        break
    field_t[int(o[0])][int(o[1])] = 'o'
    make_field(field_t)

    winnerX = check_winner('x', field_t)
    winnerO = check_winner('o', field_t)

    if winnerX == True and winnerO == True:
        print('You both are winners!!!')
        break
    elif winnerO == True:
        print('O is winner')
        break
    elif winnerX:
        print('X is winner')
        break




