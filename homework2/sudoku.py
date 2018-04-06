import random
import time
import multiprocessing

def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values, n):
    grouped = []
    i = 0
    while (i < len(values)):
        temp_list = []
        for j in range(i, i + n):
            temp_list.append(values[j])
        grouped.append(temp_list)
        i = j + 1
    return grouped


def get_row(values, pos):
    row, col = pos
    return values[row]


def get_col(values, pos):
    row, col = pos
    column = []
    for i in range(len(values)):
        column.append(values[i][col])
    return column


def get_block(values, pos):
    block = []
    row, col = pos
    if (row < 3 and col < 3):
        for i in range(3):
            for j in range(3):
                block.append(values[i][j])
        return block

    if (row < 3 and col < 6):
        for i in range(3):
            for j in range(3, 6):
                block.append(values[i][j])
        return block

    if (row < 3 and col < 9):
        for i in range(3):
            for j in range(6, 9):
                block.append(values[i][j])
        return block

    if (row < 6 and col < 3):
        for i in range(3, 6):
            for j in range(3):
                block.append(values[i][j])
        return block

    if (row < 6 and col < 6):
        for i in range(3, 6):
            for j in range(3, 6):
                block.append(values[i][j])
        return block

    if (row < 6 and col < 9):
        for i in range(3, 6):
            for j in range(6, 9):
                block.append(values[i][j])
        return block

    if (row < 9 and col < 3):
        for i in range(6, 9):
            for j in range(3):
                block.append(values[i][j])
        return block

    if (row < 9 and col < 6):
        for i in range(6, 9):
            for j in range(3, 6):
                block.append(values[i][j])
        return block

    if (row < 9 and col < 9):
        for i in range(6, 9):
            for j in range(6, 9):
                block.append(values[i][j])
        return block


def find_empty_positions(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == "."):
                return i, j
    return False


def find_possible_values(grid, pos):
    """ Вернуть все возможные значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> set(values) == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> set(values) == {'2', '5', '9'}
    True
    """

    possible_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    row = get_row(grid, pos)
    col = get_col(grid, pos)
    block = get_block(grid, pos)
    i = 0
    while (i < len(possible_values)):
        if (row.count(possible_values[i]) > 0 or col.count(possible_values[i]) > 0 or block.count(
                possible_values[i]) > 0):
            possible_values.remove(possible_values[i])
        else:
            i += 1
    return possible_values


def solve(grid):
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    def solve_recursive(grid):
        if (find_empty_positions(grid) == False):
            return True
        row, col = find_empty_positions(grid)
        possible_values = find_possible_values(grid, (row, col))
        for possible_value in possible_values:
            grid[row][col] = possible_value
            if solve_recursive(grid):
                return True
            grid[row][col] = "."
        return False

    while (find_empty_positions(grid) != False):
        flag = False
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                possible_values = find_possible_values(grid, (row, col))
                if (len(possible_values) == 1 and grid[row][col] == "."):
                    grid[row][col] = possible_values[0]
                    flag = True
        if (flag == False):
            solve_recursive(grid)

    return grid

    pass


def check_solution(grid):
    """ Если решение solution верно, то вернуть True, в противном случае False """

    for i in range(len(grid)):
        numbers = []
        for j in range(len(grid[i])):
            if numbers.count(grid[i][j]) > 0:
                return False
            else:
                numbers.append(grid[i][j])

    for i in range(len(grid)):
        numbers = []
        for j in range(len(grid[i])):
            if numbers.count(grid[j][i]) > 0:
                return False
            else:
                numbers.append(grid[j][i])
    i = 0
    j = 0
    while i < 9:
        while j < 9:
            numbers = []
            block = get_block(grid, (i, j))
            for c in range(len(block)):
                if numbers.count(block[c]) > 0:
                    return False
                else:
                    numbers.append(get_block(grid, (i, j)))
            j += 3
        i += 3
    return True


def generate_sudoku(N):
    """ Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """

    grid = []
    for i in range(3 * 3):
        grid.append([str(((i * 3 + i // 3 + j) % (3 * 3) + 1)) for j in range(3 * 3)])

    def transposing(grid):
        grid = map(list, zip(*grid))
        return grid

    def swap_rows_small(grid):
        area = random.randrange(0, 3, 1)
        line1 = random.randrange(0, 3, 1)
        N1 = area * 3 + line1

        line2 = random.randrange(0, 3, 1)
        while (line1 == line2):
            line2 = random.randrange(0, 3, 1)

        N2 = area * 3 + line2

        grid[N1], grid[N2] = grid[N2], grid[N1]
        return grid

    def swap_colums_small(grid):
        transposing(grid)
        swap_rows_small(grid)
        transposing(grid)
        return grid

    def swap_rows_area(grid):
        area1 = random.randrange(0, 3, 1)
        area2 = random.randrange(0, 3, 1)
        while (area1 == area2):
            area2 = random.randrange(0, 3, 1)
        for i in range(0, 3):
            N1, N2 = area1 * 3 + i, area2 * 3 + i
            grid[N1], grid[N2] = grid[N2], grid[N1]
        return grid

    def swap_colums_area(grid):
        transposing(grid)
        swap_rows_area(grid)
        transposing(grid)
        return grid

    function_dict = {
        1: transposing(grid),
        2: swap_colums_area(grid),
        3: swap_rows_area(grid),
        4: swap_rows_small(grid),
        5: swap_colums_small(grid)
    }

    def mix(grid, amt, function_dict):
        for i in range(1, amt):
            id_func = random.randrange(1, 5, 1)
            function_dict[id_func]
        return grid

    def find_all_filled_cells(grid):
        filled_positions = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != ".":
                    filled_positions.append((i, j))
        return filled_positions

    def delete_random_cells(grid, N):
        i = 0
        while i < 81 - N:
            filled_cells = find_all_filled_cells(grid)
            random_pos = random.randrange(0, len(filled_cells), 1)
            row, col = filled_cells[random_pos]
            grid[row][col] = "."
            i += 1

    mix(grid, 15, function_dict)
    delete_random_cells(grid, N)
    return grid


def run_solve(fname):
    grid = read_sudoku(fname)
    start = time.time()
    solve(grid)
    end = time.time()
    print(f'{fname}: {end-start}')

if __name__ == '__main__':
    for fname in ('puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt'):
        p = multiprocessing.Process(target=run_solve, args=(fname,))
        p.start()
