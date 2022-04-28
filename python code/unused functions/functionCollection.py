puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def combine_to_squares(puzzle):
    splitArr = split_rows(puzzle)
    squares = [[], [], [],
               [], [], [],
               [], [], []]
    counter = 0
    for i in splitArr:
        if counter == 0 or counter == 3 or counter == 6:
            squares[0].append(i)
        elif counter == 1 or counter == 4 or counter == 7:
            squares[1].append(i)
        elif counter == 2 or counter == 5 or counter == 8:
            squares[2].append(i)
        elif counter == 9 or counter == 12 or counter == 15:
            squares[3].append(i)
        elif counter == 10 or counter == 13 or counter == 16:
            squares[4].append(i)
        elif counter == 11 or counter == 14 or counter == 17:
            squares[5].append(i)
        elif counter == 18 or counter == 21 or counter == 24:
            squares[6].append(i)
        elif counter == 19 or counter == 22 or counter == 25:
            squares[7].append(i)
        elif counter == 20 or counter == 23 or counter == 26:
            squares[8].append(i)
        else:
            pass
        counter += 1
    return squares


def square_combine_rows(puzzle):
    output = []
    for i in combine_to_squares(puzzle):
        squareAsRow = []
        for e in i:
            for n in e:
                squareAsRow.append(n)
        output.append(squareAsRow)
    return output


def split_rows(puzzle):
    splitArr = []
    for i in puzzle:
        splitArr.append(i[:3])
        splitArr.append(i[3:6])
        splitArr.append(i[6:9])
    return splitArr


def create_column(puzzle):
    columns = []
    for i in range(9):
        column = []
        for e in puzzle:
            column.append(e[i])
        columns.append(column)
    return columns


def zeros_in_row(puzzle):
    counterArr = []
    for i in puzzle:
        counter = 0
        for e in i:
            if e == 0:
                counter += 1
            else:
                pass
        counterArr.append(counter)
    return counterArr


def zeros_in_column(puzzle):
    puzzle = create_column(puzzle)
    counterArr = []
    for i in puzzle:
        counter = 0
        for e in i:
            if e == 0:
                counter += 1
            else:
                pass
        counterArr.append(counter)
    return counterArr


def location_least_zeros(puzzle):
    rows = zeros_in_row(puzzle)
    column = zeros_in_column(puzzle)
    locSum = []
    sums = []
    counterR = 0
    for i in rows:
        counterC = 0
        for e in column:
            locSum.append((counterR, counterC))
            sums.append(i + e)
            counterC += 1
        counterR += 1
    lowest = 18
    for i in sums:
        if lowest > i >= 1:
            lowest = i
        else:
            pass
    highestArr = []
    count = 0
    for i in sums:
        if i == lowest:
            highestArr.append(count)
        count += 1
    output = []
    for i in highestArr:
        output.append(locSum[i])
    print('lowest: ', lowest)
    print('sums: ', sums)
    return output


def zeros_in_array(array):
    output = 0
    for i in array:
        if i == 0:
            output += 1
    return output


def zeros_in_square(row, column, puzzle):
    squares = square_combine_rows(puzzle)
    output = 0
    if 0 <= row <= 2 and 0 <= column <= 2:
        output = zeros_in_array(squares[0])
    elif 3 <= row <= 5 and 0 <= column <= 2:
        output = zeros_in_array(squares[1])
    elif 6 <= row <= 8 and 0 <= column <= 2:
        output = zeros_in_array(squares[2])

    elif 0 <= row <= 2 and 3 <= column <= 5:
        output = zeros_in_array(squares[3])
    elif 3 <= row <= 5 and 3 <= column <= 5:
        output = zeros_in_array(squares[4])
    elif 6 <= row <= 8 and 3 <= column <= 5:
        output = zeros_in_array(squares[5])

    elif 0 <= row <= 2 and 6 <= column <= 8:
        output = zeros_in_array(squares[6])
    elif 3 <= row <= 5 and 6 <= column <= 8:
        output = zeros_in_array(squares[7])
    elif 6 <= row <= 8 and 6 <= column <= 8:
        output = zeros_in_array(squares[8])
    else:
        print('error')
    return output


def get_zeros_plus_value(puzzle):
    column = create_column(puzzle)
    zeros = []
    values = []
    counterI = 0
    for i in puzzle:
        counterE = 0
        for e in i:
            if e == 0:
                push = []
                value = zeros_in_array(puzzle[counterI]) + zeros_in_array(
                    column[counterE]) - 1
                zeros.append((counterI, counterE, value))
                # values.append(value)
                push.append(counterI)
                push.append(counterE)
                push.append(value)
                values.append(push)
                # I.append(zeros_in_array(puzzle[counterI]))
                # E.append(zeros_in_array(column[counterE]))
            else:
                pass
            counterE += 1
        counterI += 1
    print('Value: ', values)
    return zeros


def find_best_pot(puzzle):
    pass


def sudoku(puzzle):
    puzzle = puzzle
    print('get_zeros_plus_value: ', get_zeros_plus_value(puzzle))
    # print('location_least_zeros: ', location_least_zeros(puzzle))
    # print(zeros_in_row(puzzle))
    # print(zeros_in_column(puzzle))
    # print(ptf.plot_array_fixed_x(zeros_in_column(puzzle)))
    # print(create_column(puzzle))
    return puzzle


print(sudoku(puzzle))
