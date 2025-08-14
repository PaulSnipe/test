# Игровое поле 3x3
desk = [[' ' for _ in range(3)] for _ in range(3)]

def print_desk(b):
    """Текущее состояние поля игры"""
    for i, row in enumerate(b):
        # Склеиваем ячейки через " | "
        print(' | '.join(row))
        # Разделитель строк, кроме последней
        if  i < len(b) - 1:
            print('-' * 9)

def check_winner(b):
    """
    Проверяет, есть ли победитель или ничья
    Возвращает:
    - "X", если победил крестик
    - "O", если победил нолик
    - "Draw", если ничья
    - None, если игра ещё не окончена
    """
    # Проверка строк и столбцов
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != ' ':
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != ' ':
            return b[0][i]
    # Проверка диагоналей
    if b[0][0] == b[1][1] == b[2][2] != ' ':
            return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != ' ':
            return b[0][2]
    # Проверка ничьи
    if all(cell != ' ' for row in b for cell in row):
            return 'Draw'
    return None

def get_move(player):
    """
    Запрашивает у игрока координаты хода и делает ход
    """
    while True:
        try:
            move = input(f'Игрок {player} введите строку и столбец (через пробел, от 1 до 3): ').split()
            # Проверка на ввод 2 чисел
            if len(move) != 2:
                raise ValueError
            # Превращаем в целые
            x, y = map(int, move)
            # Проверяем диапазон 1..3
            if not (1 <= x <= 3 and 1 <= y <= 3):
                raise ValueError
            # Проверяем, что клетка свободна
            if desk[x-1][y-1] != " ":
                print("Эта клетка уже занята!")
                continue
                # Возвращаем индексы 0-based (x-1, y-1), т.к. массивы нумеруются с нуля
            return x-1, y-1
        # Просим ввести заново при любой ошибке
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")

# Основной игровой цикл
current_player = "X"
winner = None

while not winner:
    print_desk(desk)
    x, y = get_move(current_player)
    desk[x][y] = current_player
    winner = check_winner(desk)
    if winner:
        break
    # Смена игрока
    current_player = "O" if current_player == "X" else "X"

print_desk(desk)
if winner == "Draw":
    print("Ничья!")
else:
    print(f"Игрок {winner} победил!")