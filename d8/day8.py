from d8.day8_input import DATA

test_input = """30373
25512
65332
33549
35390"""


def first_res(data):
    original_matrix = list()
    visibility_matrix = list()
    visible_counter = 0
    for el in data.split("\n"):
        original_matrix.append([int(i) for i in el])
        visibility_matrix.append([0 for i in range(len(el))])

    outer = len(original_matrix) * 2 + len(original_matrix[0]) * 2 - 4
    look_from_top(original_matrix, visibility_matrix)
    look_from_bottom(original_matrix, visibility_matrix)
    look_from_left(original_matrix, visibility_matrix)
    look_from_right(original_matrix, visibility_matrix)

    for i in visibility_matrix[1:-1]:
        tmp = i[1:-1]
        visible_counter += sum(tmp)

    return visible_counter + outer


def look_from_top(original_matrix, visibility_matrix):
    current = original_matrix[0]
    forbidden_j = []
    for i in range(1, len(original_matrix)):
        if len(forbidden_j) == len(current):
            break

        for j in range(1, len(current)):
            if original_matrix[i][j] > current[j]:
                visibility_matrix[i][j] = 1
                current[j] = original_matrix[i][j]
            elif original_matrix[i][j] == current[j]:
                pass
            else:
                forbidden_j.append(j)


def look_from_bottom(original_matrix, visibility_matrix):
    current = original_matrix[-1]
    forbidden_j = []
    for i in range(len(original_matrix) - 2, 0, -1):
        if len(forbidden_j) == len(current):
            break

        for j in range(len(current)):
            if original_matrix[i][j] > current[j]:
                visibility_matrix[i][j] = 1
                current[j] = original_matrix[i][j]
            elif original_matrix[i][j] == current[j]:
                pass
            else:
                forbidden_j.append(j)


def look_from_left(original_matrix, visibility_matrix):
    current = [el[0] for el in original_matrix]
    for j in range(1, len(current)):
        for i in range(1, len(original_matrix)):
            if original_matrix[j][i] > current[j]:
                visibility_matrix[j][i] = 1
                current[j] = original_matrix[j][i]

            if original_matrix[j][i] >= 9:
                break


def look_from_right(original_matrix, visibility_matrix):
    current = [el[-1] for el in original_matrix]
    for j in range(1, len(current)):
        for i in range(len(original_matrix) - 2, 0, -1):
            if original_matrix[j][i] > current[j]:
                visibility_matrix[j][i] = 1
                current[j] = original_matrix[j][i]
            if original_matrix[j][i] >= 9:
                break


def second_res(data):
    original_matrix = list()
    max_score = 0
    for el in data.split("\n"):
        original_matrix.append([int(i) for i in el])

    for i in range(1, len(original_matrix) - 1):
        len_row = len(original_matrix[i])
        for j in range(1, len_row - 1):
            score = count_score(original_matrix, i, j)
            if score > max_score:
                max_score = score

    return max_score


def count_score(matrix, pos_i, pos_j):
    counter_left, counter_right, counter_top, counter_bottom = 0, 0, 0, 0
    i, j = pos_i, pos_j

    while matrix[pos_i][pos_j] > matrix[i-1][j] and i - 1 > 0 and i < (len(matrix)- 1):
        counter_top += 1
        i -= 1
    if i - 1 == 0 or matrix[pos_i][pos_j] == matrix[i-1][j]:
        counter_top += 1

    i, j = pos_i, pos_j
    while matrix[pos_i][pos_j] > matrix[i+1][j] and i > 0 and i < (len(matrix) - 2):
        counter_bottom += 1
        i += 1
    if i + 1 == (len(matrix)-1) or matrix[pos_i][pos_j] == matrix[i+1][j]:
        counter_bottom += 1

    i, j = pos_i, pos_j
    while matrix[pos_i][pos_j] > matrix[i][j - 1] and j - 1 > 0 and j < (len(matrix[0]) - 1):
        counter_left += 1
        j -= 1

    if j - 1 == 0 or matrix[pos_i][pos_j] == matrix[i][j-1]:
        counter_left += 1

    i, j = pos_i, pos_j
    while matrix[pos_i][pos_j] > matrix[i][j+1] and j > 0 and j < (len(matrix[0]) - 2):
        counter_right += 1
        j += 1

    if j + 1 == (len(matrix[0])-1) or matrix[pos_i][pos_j] == matrix[i][j + 1]:
        counter_right += 1

    return counter_top * counter_bottom * counter_right * counter_left


assert first_res(test_input) == 21
assert first_res(DATA) == 1820

assert second_res(test_input) == 8
assert second_res(DATA) == 385112
