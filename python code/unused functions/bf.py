# create and matrix with arrays containing columns of the puzzle
def create_column(puzzle):
    columns = []
    for i in range(9):
        column = []
        for e in puzzle:
            column.append(e[i])
        columns.append(column)
    return columns


# count amount of zeros in an array and returns an integer
def zeros_in_array(array):
    output = 0
    for i in array:
        if i == 0:
            output += 1
    return output


# !!! not finished !!!
def square_combine_rows(puzzle):
    output = []
    for i in combine_to_squares(puzzle):
        squareAsRow = []
        for e in i:
            for n in e:
                squareAsRow.append(n)
        output.append(squareAsRow)
    return output


# split the row array into three
def split_rows(puzzle):
    splitArr = []
    for i in puzzle:
        splitArr.append(i[:3])
        splitArr.append(i[3:6])
        splitArr.append(i[6:9])
    return splitArr


# creates a matrix in the shape of the sudoku 3x3 squares
def combine_to_squares(puzzle):
    splitArr = split_rows(puzzle)
    squares = [[],[],[],
               [],[],[],
               [],[],[]]
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


# finds the amount of zeros in a square based on the position of the gap (row, column)
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


# get position of all zeros and a value of the correlating zeros
def get_zeros_plus_value(puzzle):
    column = create_column(puzzle)
    values = []
    counterI = 0
    x = []
    y = []
    for i in puzzle:
        counterE = 0
        for e in i:
            if e == 0:
                value = zeros_in_array(puzzle[counterI]) + zeros_in_array(column[counterE]) - 2 + zeros_in_square(counterI, counterE, puzzle)*0.5
                y.append(counterI)
                x.append(counterE)
                values.append(value)
            else:
                pass
            counterE += 1
        counterI += 1
    return [y, x, values]


# calculates an average value (correlating zeros) of all zeros in all rows
def get_rows_avgvalue(puzzle, type):
    column = create_column(puzzle)
    values = []
    counterI = 0
    x = []
    y = []
    if type == 'column':
        puzzle = create_column(puzzle)
    else:
        pass
    for i in puzzle:
        counterE = 0
        appendRowVal = []
        for e in i:
            if e == 0:
                value = zeros_in_array(puzzle[counterI]) + zeros_in_array(column[counterE]) - 2 + zeros_in_square(counterI, counterE, puzzle) * 0.5
                y.append(counterI)
                appendRowVal.append(value)
            else:
                pass
            counterE += 1
        values.append(appendRowVal)
        y.append(counterI)
        counterI += 1
    return [values, list(set(y))]
