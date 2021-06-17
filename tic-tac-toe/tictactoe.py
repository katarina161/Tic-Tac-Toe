# write your code here
# def print_grid(cells):
#     print("-" * 9)
#     i = 0
#     while i < len(cells):
#         print(f"| {' '.join(cells[i:i + 3]).replace('_', ' ')} |")
#         i += 3
#     print("-" * 9)


def print_grid(cells):
    if isinstance(cells, str):
        game_grid = [[cells[j] for j in range(i, i + 3)] for i in range(0, len(cells), 3)]
    else:
        game_grid = cells
    print("-" * 9)
    for row in game_grid:
        print(f"| {' '.join(row).replace('_', ' ')} |")
    print("-" * 9)
    return game_grid


def print_grid_nested_list(cells):
    print("-" * 9)
    rows = [[cells[j] for j in range(i, i + 3)] for i in range(0, len(cells), 3)]
    for row in rows:
        print(f"| {' '.join(row)} |")
    print("-" * 9)


def make_a_move(game_grid: list, coordinate: tuple, player: str):
    row, col = coordinate
    if game_grid[row][col] not in " _":
        print("This cell is occupied! Choose another one!")
    else:
        game_grid[row][col] = player
        return game_grid


def player_won(cells, player):
    if isinstance(cells, str):
        rows = [[cells[j] for j in range(i, i + 3)] for i in range(0, len(cells), 3)]
    else:
        rows = cells
    columns = [list(col) for col in zip(rows[0], rows[1], rows[2])]
    diag = [rows[i][i] for i in range(len(rows))]
    sec_diag = [rows[len(rows) - 1 - i][i] for i in range(len(rows) - 1, -1, -1)]

    if any([all([el == player for el in row]) for row in rows]) or \
       any([all([el == player for el in col]) for col in columns]) or \
       all([el == player for el in diag]) or \
       all([el == player for el in sec_diag]):
        return True

    return False


def current_game_status(cells):
    # if isinstance(cells, str):
    #     num_of_x = cells.count("X")
    #     num_of_o = cells.count("O")
    # else:
    #     num_of_x = sum((cell for row in cells for cell in row if cell == "X"))
    #     num_of_o = sum((cell for row in cells for cell in row if cell == "O"))

    # if abs(num_of_x - num_of_o) > 1 or \
    #         (player_won(cells, "X") and player_won(cells, "O")):
    #     print("Impossible")
    #     return

    if player_won(cells, "X"):
        return "X"
    elif player_won(cells, "O"):
        return "O"


if __name__ == "__main__":
    # symbols = input("Enter cells: ")
    first_p = "X"
    second_p = "O"
    fp_turn = True
    winner = None

    game_grid = print_grid(" " * 9)
    while True:
        winner = current_game_status(game_grid)
        if not winner and all([cell not in " _" for row in game_grid for cell in row]):
            print("Draw")
            break

        if winner:
            print(f"{winner} wins")
            break

        if fp_turn:
            symbol = first_p
        else:
            symbol = second_p

        played = False
        while not played:
            try:
                row, col = [int(s.strip()) - 1 for s in input("Enter the coordinates: ").split()]
                if not (0 <= row <= 2) or not (0 <= col <= 2):
                    print("Coordinates should be from 1 to 3!")
                else:
                    gg = make_a_move(game_grid, (row, col), symbol)
                    if gg:
                        game_grid = gg
                        played = True
            except ValueError:
                print("You should enter numbers!")
        fp_turn = not fp_turn
        print_grid(game_grid)

    # current_game_status(symbols)
