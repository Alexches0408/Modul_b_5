# При запуске в PyCharm запустить эмуляцию терминала в консоли для успешного очищения поля при запуске новой игры

import os


# Очищаем консоль при запуске новой игры
def clear_screen():
    os.system('cls')


# Функция для проверки, чтобы имена не совпадали
def check_name(gamer1):
    gamer_check = str(input("Введите имя второго игрока и нажмите Enter: \n-->")) or "gamer 2"
    if gamer_check == gamer1:
        print("\nИмя второго игрока совпадает с именем первого\n")
        return check_name(gamer1)
    else:
        return gamer_check


# Создаем имена игроков
def create_gamer():
    gamer_name1 = str(input("Введите имя первого игрока и нажмите Enter: \n-->")) or "gamer 1"
    print(f"Имя первого игрока {gamer_name1}")

    # Проверяем имена, чтобы не совпадали
    gamer_name2 = check_name(gamer_name1)
    print(f"Имя второго игрока {gamer_name2}")
    return [gamer_name1, gamer_name2]

# Проверяем что введенное значение не выходит за пределы диапазона поля
def check_input(alias):
    caption = input(f"Введите номер {alias}:")
    if str(caption) == "1" or str(caption) == "2" or str(caption) == "3":
        return int(caption)
    else:
        print("Введенное значение выходит за границы диапазона!!!\n")
        return check_input(alias)

# функция для вывода на печать текущих значений матрицы
def field_dec(field):
    return f"   1 2 3\n 1 {' '.join(field[0])}\n 2 {' '.join(field[1])}\n 3 {' '.join(field[2])}"

# Функция, проверяющая победителя. Проверяем, определился ли победитель или поле заполнено и вышла ничья
def check_final(field_fin):
    # заполняем массив булевыми значениями, являются ли элементы символами "-"
    massiv = []
    [[massiv.append(x != "-") for x in row] for row in field_fin]
    # Проверка по строкам
    for i in field_fin:
        if all([x == "X" for x in i]) or all([x == "0" for x in i]):
            return "Победа"
    # Проверка по столбцам
    for j in range(3):
        if field_fin[0][j] == field_fin[1][j] == field_fin[2][j] != "-":
            return "Победа"
    # Проверка по диагоналям
    if field_fin[0][0] == field_fin[1][1] == field_fin[2][2] != "-" or field_fin[0][2] == field_fin[1][1] == \
            field_fin[2][0] != "-":
        return "Победа"
    # Свободные ячейки кончились, ничья
    if all(massiv):
        return "Ничья"

# Вписываем в клетку крестик или нолик, или выводим сообщение что клетка занята
def mark(row_in, col_in, gamer_val, field_mark, gamer1):
    if str(field_mark[row_in - 1][col_in - 1]) == "-":
        if gamer_val == gamer1:
            field_mark[row_in - 1][col_in - 1] = "X"
            return field_mark
        else:
            field_mark[row_in - 1][col_in - 1] = "0"
            return field_mark
    else:
        return "Данная клетка занята"

def step(field):
    # Имя игрока должно выводиться с помощью функции генератора
    gamer_in = gamers.copy()
    gamer1 = gamer_in[0]
    field_step = field.copy()
    while True:
        print(field_dec(field_step))

        gamer_val = gamer_in[0]
        print(f'Ход игрока под именем "{gamer_val}" \n -----------')

        row_ = check_input("строки")
        col_ = check_input("столбца")

        mark_ = mark(row_, col_, gamer_val, field_step, gamer1)
        if mark_ == "Данная клетка занята":
            print("\nДанная клетка занята\nВведите другие значения")
            step()
        else:
            field_step = mark_
            if check_final(field_step) == "Победа":
                yield gamer_val
            if check_final(field_step) == "Ничья":
                yield "Ничья"
            gamer_val = gamer_in.pop(0)
            gamer_in.append(gamer_val)
            yield "Cледующий ход"

def game(gamers):
    # Надпись при победе
    winner = "----------------------------------------------------------------\n" \
             "-----X---X---X-----X----X-----X----X-----X----XXXXX----XXXX-----\n" \
             "-----X--X-X--X-----X----X-X---X----X-X---X----X--------X--X-----\n" \
             "-----X--X-X--X-----X----X--X--X----X--X--X----XXXXX----XXX------\n" \
             "-----X-X---X-X-----X----X---X-X----X---X-X----X--------X--X-----\n" \
             "------X-----X------X----X-----X----X-----X----XXXXX----X--X-----\n" \
             "----------------------------------------------------------------"

    # создали матрицу, хранящую введенные значения
    field = [["-" for i in range(3)] for j in range(3)]

    for i in step(field):
        if str(i) in gamers:
            print(winner)
            print(f"Победил игрок {i}")
            break
        if str(i) == "Ничья":
            print(f"\nПобедила дружба\n")
            break

    cont = input("Введите X для завершения игры, R для реванша или введите любой символ для новой игры\n-->")
    if cont == "x" or cont == "X":
        return
    elif cont == "r" or cont == "R":
        clear_screen()
        game(gamers)
    else:
        clear_screen()
        create_gamer()
        game(gamers)


gamers = create_gamer()
game(gamers)
