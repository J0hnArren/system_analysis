from io import StringIO
from math import log
import csv


def relation_1(arr):
    return [x[0] for x in arr]


def relation_2(arr):
    return [x[1] for x in arr]


def relation_3(arr):
    new_arr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i][1] == arr[j][0]:
                new_arr.append(arr[i][0])
    return new_arr


def relation_4(arr):
    new_arr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i][0] == arr[j][1]:
                new_arr.append(arr[i][1])
    return new_arr


def relation_5(arr):
    new_arr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i][0] == arr[j][0]:
                new_arr.append(arr[i][1])
    return new_arr


def entropy(p):
    return - (p * log(p, 2))


def task(*args):
    f = StringIO(args[0])
    graph = list(csv.reader(f, delimiter=','))
    graph = list(map(lambda x: [int(i) for i in x], graph))

    # Отношение 1 - прямое управление
    arr1 = relation_1(graph)

    # Отношение 2 - прямое подчинение
    arr2 = relation_2(graph)

    # Отношение 3 - косвенное управление
    arr3 = relation_3(graph)

    # Отношение 4 - косвенное подчинение
    arr4 = relation_4(graph)

    # Отношение 5 - соподчинение
    arr5 = relation_5(graph)

    vertex = set()  # номера вершин

    for x in graph:
        vertex.update(x)
    vertex = list(vertex)

    res_arr = [[] for i in vertex]  # результат

    for v in vertex:
        res_arr[int(v) - 1].append(arr1.count(v))
        res_arr[int(v) - 1].append(arr2.count(v))
        res_arr[int(v) - 1].append(arr3.count(v))
        res_arr[int(v) - 1].append(arr4.count(v))
        res_arr[int(v) - 1].append(arr5.count(v))

    # Проверка на правильность отношений
    for i in range(len(args[1:])):
        assert res_arr[i] == args[i+1]

    H = 0
    for i in range(len(vertex)):
        for j in range(len(vertex)):
            if res_arr[i][j] != 0:
                H += entropy(res_arr[i][j] / (len(vertex) - 1))

    return H


if __name__ == '__main__':
    data = '''1,2
              1,3
              3,4
              3,5'''

    n1 = [2, 0, 2, 0, 0]
    n2 = [0, 1, 0, 0, 1]
    n3 = [2, 1, 0, 0, 1]
    n4 = [0, 1, 0, 1, 1]
    n5 = [0, 1, 0, 1, 1]

    assert task(data, n1, n2, n3, n4, n5) == 6.5
