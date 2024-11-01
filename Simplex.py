from xmlrpc.client import MAXINT


def iterate(matrix, accuracy):
    pivot_column = -1
    for i in range(0, len(matrix[-1]) - 1):
        if matrix[-1][i] < 0:
            if pivot_column != -1:
                if matrix[-1][i] < matrix[-1][pivot_column]:
                    pivot_column = i
            else:
                pivot_column = i
    if pivot_column == -1:
        for i in range(0, len(matrix) - 1):
            if matrix[i][-1] < 0:
                return "The method is not applicable!"
        return "done"
    minimum, pivot_row = MAXINT, -1
    for i in range(0, len(matrix) - 1):
        if matrix[i][pivot_column] == 0 or matrix[i][-1] <= 0:
            continue
        temp = matrix[i][-1] / matrix[i][pivot_column]
        if minimum > temp > 0:
            minimum = temp
            pivot_row = i
    if minimum == MAXINT or matrix[pivot_row][pivot_column] == 0:
        return "The method is not applicable!"
    for i in range(0, len(matrix)):
        if i != pivot_row:
            parameter = -matrix[i][pivot_column] / matrix[pivot_row][pivot_column]
            for j in range(0, len(matrix[i])):
                matrix[i][j] = round(matrix[i][j] + matrix[pivot_row][j] * parameter, accuracy)
        else:
            parameter = matrix[pivot_row][pivot_column]
            for j in range(0, len(matrix[i])):
                matrix[i][j] = round(matrix[i][j] / parameter, accuracy)
    return "continue"


def applySimplex(matrix, number_of_variables, accuracy, function=1):
    while True:
        result = iterate(matrix, accuracy)
        if result != "continue":
            break
    if result != "done":
        print(result)
        return
    for i in range(0, number_of_variables):
        count = 0
        index = -1
        for j in range(0, len(matrix)):
            if matrix[j][i] == 1:
                count += 1
                index = j
            elif matrix[j][i] != 0:
                count += 200
                break
        if count != 1:
            print("x" + str(i + 1) + " = 0")
        else:
            print("x" + str(i + 1) + " = " + str(round(matrix[index][-1], accuracy)))
    resultValue = round(matrix[-1][-1], accuracy)
    print("Maximize" if function else "Minimize", " of the function =", resultValue if function else -resultValue)


def minimize(matrix, number_of_variables, accuracy):
    while True:
        result = iterate(matrix, accuracy)
        if result != "continue":
            break
    if result != "done":
        print(result)
        return
    for i in range(0, number_of_variables):
        print(
            "x" + str(i + 1) + " = " + str(round(matrix[-1][len(matrix[-1]) - 2 - number_of_variables + i], accuracy)))
    print("Minimum of the function =", round(matrix[-1][-1], accuracy))
    pass


def transpose(matrix):
    other = []
    for i in range(0, len(matrix[1])):
        other.append([])
        for j in range(0, len(matrix)):
            other[i].append(matrix[j][i])
    return other


def solve(objective_function, constraint_functions,
          right_hand_side, accuracy=2, function="Maximize"):
    matrix = []
    for i in range(0, len(constraint_functions)):
        matrix.append(constraint_functions[i] + [0] * i + [1] +
                      [0] * (len(constraint_functions) - 1 - i) + [0] + [right_hand_side[i]])
    if function == "Maximize":
        matrix.append(([i * -1 for i in objective_function] + len(constraint_functions) * [0] + [1, 0]))
        applySimplex(matrix, len(objective_function), accuracy)
    elif function == "Minimize":
        matrix.append((objective_function + len(constraint_functions) * [0] + [1, 0]))
        for i in objective_function:
            if i < 0:
                applySimplex(matrix, len(objective_function), accuracy, 0)
                return
        matrix = []
        for i in range(0, len(constraint_functions)):
            matrix.append(constraint_functions[i])
        matrix.append(objective_function)
        matrix = transpose(matrix)
        matrix.append([-1 * i for i in right_hand_side] + [0] * (len(matrix)) + [1] + [0])
        for i in range(0, len(matrix) - 1):
            temp = matrix[i][-1]
            matrix[i].pop()
            matrix[i] += [0] * i + [1] + [0] * (len(constraint_functions[0]) - i) + [temp]
        minimize(matrix, len(constraint_functions[0]), accuracy)


if __name__ == '__main__':
    obj_f = list(map(int, input().split()))
    x = int(input())
    constr_f = []
    for i in range(0, x):
        constr_f.append(list(map(int, input().split())))
    rhs = list(map(int, input().split()))
    acc = int(input())
    func = input()

    solve(obj_f, constr_f, rhs, function=func, accuracy=acc)
