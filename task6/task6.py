import json
import numpy as np


def create_matrix(cols: np.array) -> np.array:
    c = len(cols)
    res = np.zeros((c, c))
    for i in range(c):
        for j in range(c):
            x = 0
            if cols[i] > cols[j]:
                x = 1
            elif cols[i] == cols[j]:
                x = 0.5
            res[i][j] = x
    return res


def create_comparisons(table: np.array) -> np.ndarray:
    pairwise_comparisons = []
    for col in range(table.shape[1]):
        pairwise_comparisons.append(create_matrix(table[:, col]).T)
    return np.mean(pairwise_comparisons, axis=0)


def task(json_data: str) -> str:
    table = np.array(json.loads(json_data)).T
    average = create_comparisons(table)
    k0 = [1 / table.shape[0] for _ in range(table.shape[1])]
    y = np.dot(average, k0)
    l_ = np.dot(np.ones(len(y)), y)
    k1 = np.dot(1 / l_, y)

    while max(abs(k1 - k0)) >= 0.001:
        k0 = k1
        y = np.dot(average, k0)
        l_ = np.dot(np.ones(len(y)), y)
        k1 = np.dot(1 / l_, y)

    return json.dumps([round(el, 3) for el in k1])


if __name__ == "__main__":
    assert task("[[1,3,2],[2,2,2],[1.5,3,1.5]]") == "[0.468, 0.169, 0.363]"
