import random

board = []
for i in range(6):
    board.append(["O"] * 6)

# создаем поле бота
bot_board = []
for i in range(6):
    bot_board.append(["O"] * 6)


# функция для отображения поля
def print_board(board):
    for row in board:
        print(" ".join(row))

    # случайное размещение кораблей на поле бота


def place_ships(bot_board):
    ship_sizes = [5, 4, 3, 3, 2]  # размеры кораблей
    for size in ship_sizes:
        placed = False
        while not placed:

            x = random.randint(0, 6)
            y = random.randint(0, 6)
            orientation = random.choice(["horizontal", "vertical"])

            if orientation == "horizontal" and x + size <= 6:
                valid = True
                for i in range(size):
                    if bot_board[y][x + i] != "O":
                        valid = False
                        break
                if valid:
                    for i in range(size):
                        bot_board[y][x + i] = "X"
                    placed = True
            elif orientation == "vertical" and y + size <=6:
                valid = True
                for i in range(size):
                    if bot_board[y + i][x] != "O":
                        valid = False
                        break
                if valid:
                    for i in range(size):
                        bot_board[y + i][x] = "X"
                    placed = True

                # размещаем корабли на поле бота


place_ships(bot_board)

# выводим поле бота
print("Bot's board:")
print_board(bot_board)

# начинаем игру
while True:
    # вводим координаты выстрела
    print("Your turn!")
    guess_x = int(input("Guess X (0-6): "))
    guess_y = int(input("Guess Y (0-6): "))
    # проверяем попал ли игрок в корабль
    if bot_board[guess_y][guess_x] == "S":
        print("Hit!")
        bot_board[guess_y][guess_x] = "X"
    else:
        print("Miss!")
        bot_board[guess_y][guess_x] = "-"
        # проверяем, остались ли на поле бота корабли
    if "S" not in [item for sublist in bot_board for item in sublist]:
        print("You win!")
        break
        # бот делает выстрел
    print("Bot's turn!")
    guess_x = random.randomand