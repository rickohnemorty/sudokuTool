puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def create_dict(puzzle):
    arr = []
    for i in puzzle:
        for e in i:
            arr.append(e)
    squares = [
        0, 0, 0, 1, 1, 1, 2, 2, 2,
        0, 0, 0, 1, 1, 1, 2, 2, 2,
        0, 0, 0, 1, 1, 1, 2, 2, 2,
        3, 3, 3, 4, 4, 4, 5, 5, 5,
        3, 3, 3, 4, 4, 4, 5, 5, 5,
        3, 3, 3, 4, 4, 4, 5, 5, 5,
        6, 6, 6, 7, 7, 7, 8, 8, 8,
        6, 6, 6, 7, 7, 7, 8, 8, 8,
        6, 6, 6, 7, 7, 7, 8, 8, 8
    ]
    positions = []
    counter_i = 0
    counter_e = 0
    counter_square = 0
    for i in arr:
        if counter_i >= 9:
            counter_e += 1
            counter_i = 0
        else:
            pass
        positions.append((counter_i, counter_e, squares[counter_square]))
        counter_i += 1
        counter_square += 1
    dictionary = dict(zip(positions, arr))
    return dictionary


def create_position_zeros(puzzle):
    dictionary = create_dict(puzzle)
    counter = 0
    positions_zeros = []
    for i in list(dictionary.values()):
        if i == 0:
            positions_zeros.append(list(dictionary)[counter])
        else:
            pass
        counter += 1
    return positions_zeros


def calculate_value_of_all_zeros(puzzle):
    positions_zeros = create_position_zeros(puzzle)
    # iterate through all positions of zeros
    result = []
    positions_of_values_y = []
    positions_of_values_x = []
    for i in positions_zeros:
        zeros_in_same_square = 0
        for e in positions_zeros:
            if e[2] == i[2]:
                zeros_in_same_square += 1
            else:
                pass
        zeros_in_row_minus_square = 0
        for e in positions_zeros:
            if i[1] == e[1] and i[2] != e[2]:
                zeros_in_row_minus_square += 1
            else:
                pass
        zeros_in_column_minus_square = 0
        for e in positions_zeros:
            if i[0] == e[0] and i[2] != e[2]:
                zeros_in_column_minus_square += 1
            else:
                pass
        value = zeros_in_same_square + zeros_in_column_minus_square + zeros_in_row_minus_square
        result.append(value)
        positions_of_values_y.append(i[1])
        positions_of_values_x.append(i[0])
    return [positions_of_values_y, positions_of_values_x, result]


def get_values_rows(puzzle):
    data = calculate_value_of_all_zeros(puzzle)
    result = []
    rows = data[0]
    values = data[2]
    counter = 0
    counter_idx = 0
    append_arr = []
    for i in rows:
        if counter_idx != i:
            result.append(append_arr)
            append_arr = []
            counter_idx += 1
        else:
            pass
        append_arr.append(float(values[counter]))
        counter += 1
    result.append(append_arr)

    return [result, list(set(rows))]


def test(puzzle):
    pass


# test(puzzle)
