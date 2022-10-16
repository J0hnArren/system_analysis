from io import StringIO
import csv


def task(csv_str):
    f = StringIO(csv_str)
    reader = csv.reader(f, delimiter=',')
    input_ = []
    result = [[] for _ in range(5)]
    for line in reader:
        input_.append([int(line[0]), int(line[1])])

    def direct(ind, arr):
        for i in input_:
            if i[ind] not in arr:
                arr.append(i[ind])

    def indirect(first_ind, second_ind, arr):
        for i in input_:
            for j in input_:
                if (i[first_ind] not in arr) and (j[first_ind] == i[second_ind]):
                    arr.append(i[first_ind])

    # d
    direct(0, result[0])
    direct(1, result[1])

    indirect(0, 1, result[2])
    indirect(1, 0, result[3])

    for line in input_:
        for next_line in input_:
            if line[1] not in result[4] and next_line[0] == line[0] and next_line != line:
                result[4].append(line[1])

    return result


# if __name__ == "__main__":
#     answer = task('''1,2
#                     1,3
#                     3,4
#                     3,5''')
#
#     for _ in answer:
#         print(_)
