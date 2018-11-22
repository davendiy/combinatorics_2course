#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com


def lcs(a, b, i, j):

    if i <= 0 or j <= 0:
        return 0
    elif a[i-1] == b[j-1]:
        return lcs(a, b, i-1, j-1) + 1
    else:
        return max(lcs(a, b, i, j-1), lcs(a, b, i-1, j))


def dynamic(a, b):
    m = len(a)
    n = len(b)
    val = [[0 for x in range(n)] for x in range(m)]
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                val[i][j] = val[i-1][j-1] + 1
            else:
                val[i][j] = max(val[i-1][j], val[i][j-1])

    return val


def dynamic2(a, b):
    m = len(a)
    n = len(b)
    val = [[0 for i in range(n)] for i in range(m)]
    seq = [[[] for i in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                val[i][j] = val[i-1][j-1] + 1
                seq[i][j] = [*seq[i-1][j-1]] + [a[i]]
            else:
                val[i][j] = max(val[i-1][j], val[i][j-1])
                if val[i-1][j] >= val[i][j-1]:
                    seq[i][j] = seq[i-1][j]
                else:
                    seq[i][j] = seq[i][j-1]
    # for line in val: print(line)
    # print('\n\n')
    # for line in seq: print(line)
    return val, seq[m-1][n-1]


def build_seq(matrix, a, b, i, j):
    if i == 0 or j == 0:
        return ''
    elif matrix[i][j] == matrix[i-1][j-1] + 1:
        return build_seq(matrix, a, b, i-1, j-1) + a[i]
    elif matrix[i][j] == matrix[i][j-1]:
        return build_seq(matrix, a, b, i, j-1)
    elif matrix[i][j] == matrix[i-1][j]:
        return build_seq(matrix, a, b, i-1, j)


if __name__ == '__main__':
    test_a = 'absdkf'
    test_b = 'absadflaks'
    test_m = len(test_a)
    test_n = len(test_b)

    res = dynamic(test_a, test_b)
    subseq = build_seq(res, test_a, test_b, test_m-1, test_n-1)

    print(res[test_m-1][test_n-1])
    print(subseq)

    for row in res:
        print(' '.join(map(str, row)))

    print()
    test2, tmp = dynamic2(test_a, test_b)
    for row in test2:
        print(row)
