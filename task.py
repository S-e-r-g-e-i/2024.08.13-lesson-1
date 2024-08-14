# Крестики-нолики
area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Добро пожаловать в крестики-нолики!')
print('___________________________________')


def draw_area():
    for i in area:
        print(*i)
    print()


def check_win():
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0] == ['X', 'X', 'X'] or area[1] == ['X', 'X', 'X'] or area[2] == ['X', 'X', 'X']:
        return 'X'
    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X':
        return 'X'

    if area[0][0] == 'O' and area[1][1] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[0][2] == 'O' and area[1][1] == 'O' and area[2][0] == 'O':
        return 'O'
    if area[0] == ['O', 'O', 'O'] or area[1] == ['O', 'O', 'O'] or area[2] == ['O', 'O', 'O']:
        return 'O'
    if area[0][0] == 'O' and area[1][0] == 'O' and area[2][0] == 'O':
        return 'O'
    if area[0][1] == 'O' and area[1][1] == 'O' and area[2][1] == 'O':
        return 'O'
    if area[0][2] == 'O' and area[1][2] == 'O' and area[2][2] == 'O':
        return 'O'
    return '*'


draw_area()

for j in range(1, 10, 1):
    if j % 2 == 0:
        print("Ходят нолики!")
    else:
        print("Ходят кркстики")
    row = int(input('Введите номер строки (1,2,3): ')) - 1
    column = int(input('Введите номер столбца (1,2,3): ')) - 1
    if column > 3 or row > 3:
        print()
        print('Переход хода, введены несуществующие в игре номера!!!')
        print()
        continue
    if area[row][column] != '*':
        print()
        print('Переход хода, ячейка занята!!!')
        print()
        continue
    if j % 2 == 0:
        area[row][column] = 'O'
    else:
        area[row][column] = 'X'
    if check_win() == 'X':
        draw_area()
        print('==============================')
        print('Поздравляем, победили крестики!')
        print('==============================')
        break
    if check_win() == 'O':
        draw_area()
        print('==============================')
        print('Поздравляем, победили нолики!')
        print('==============================')
        break
    else:
        draw_area()
