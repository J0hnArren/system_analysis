import json
import numpy as np
from functools import reduce


def relationship_matrix(ranking):
    ranks = dict()
    rank_length = reduce(lambda count, l:
                         count + (len(l) if isinstance(l, list) else 1),
                         ranking, 0)

    for i, rank in enumerate(ranking):
        if isinstance(rank, str):
            ranks[int(rank)] = i
        else:
            for r in rank:
                ranks[int(r)] = i

    return np.matrix([
        [1 if ranks[i + 1] <= ranks[j + 1] else 0 for j in range(rank_length)]
        for i in range(rank_length)]
    )


def task(*args):
    if len(args) > 2:
        print('Too many arguments')
        return

    j1 = json.loads(args[0])
    j2 = json.loads(args[1])

    m1 = relationship_matrix(j1)
    m1_t = m1.transpose()

    m2 = relationship_matrix(j2)
    m2_t = m2.transpose()

    M = np.multiply(m1, m2)
    M_t = np.multiply(m1_t, m2_t)

    conflict_core = []

    for i in range(M.shape[0]):
        for j in range(M[i].shape[1]):
            if int(M[i, j]) == 0 and int(M_t[i, j]) == 0:
                if (str(j + 1), str(i + 1)) not in conflict_core:
                    conflict_core.append((str(i + 1), str(j + 1)))

    return json.dumps(conflict_core)


if __name__ == '__main__':
    example_1 = '["1", ["2","3"],"4", ["5", "6", "7"], "8", "9", "10"]'
    example_2 = '[["1","2"], ["3","4","5"], "6", "7", "9", ["8","10"]]'

    assert task(example_1, example_2) == '[["8", "9"]]'
