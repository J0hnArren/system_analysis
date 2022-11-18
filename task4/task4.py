from io import StringIO
from math import log
import csv


def complex_relation(func):
    def wrapped(*args):
        params = func(*args)
        arr = params[-1]
        new_arr = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i][params[0]] == arr[j][params[1]]:
                    new_arr.append(arr[i][params[2]])
        return new_arr

    return wrapped


def relation_1(arr):
    """прямое управление"""
    return [x[0] for x in arr]


def relation_2(arr):
    """прямое подчинение"""
    return [x[1] for x in arr]


@complex_relation
def relation_3(arr):
    """косвенное управление"""
    return 1, 0, 0, arr


@complex_relation
def relation_4(arr):
    """косвенное подчинение"""
    return 0, 1, 1, arr


@complex_relation
def relation_5(arr):
    """соподчинение"""
    return 0, 0, 1, arr


def entropy(p):
    """формула энтропии"""
    return -(p * log(p, 2))


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

    res_arr = [[] for _ in vertex]  # результат

    for v in vertex:
        res_arr[int(v) - 1].append(arr1.count(v))
        res_arr[int(v) - 1].append(arr2.count(v))
        res_arr[int(v) - 1].append(arr3.count(v))
        res_arr[int(v) - 1].append(arr4.count(v))
        res_arr[int(v) - 1].append(arr5.count(v))

    # Проверка на правильность отношений
    if len(args) > 1:
        for i in range(len(args[1:])):
            assert res_arr[i] == args[i+1]

    # Вычисление энтропии
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
