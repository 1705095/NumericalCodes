import numpy as np

import sys

SysCr = 0


def LowUP(matA):
    n = len(matA)
    Upper = np.zeros((n, n), dtype=float)
    # print(Upper)
    Lower = np.identity(n, dtype=float)
    # print(Lower)

    for row in range(n):
        for colomn in range(n):
            Upper[row][colomn] = matA[row][colomn]

    for row in range(n):
        for Nrow in range(row + 1, n):
            factor = Upper[Nrow][row] / Upper[row][row]
            Lower[Nrow][row] = round(factor, 4)
            for colomn in range(n):
                s = Upper[Nrow][colomn] - (factor * Upper[row][colomn])
                val = round(s, 4)
                Upper[Nrow][colomn] = val

    return Lower, Upper


def ForwardSub(Lower, matB):
    n = len(Lower)
    matY = np.zeros(n, dtype=float)
    for row in range(0, n):
        matY[row] = matB[row];
        for coloumn in range(0, row):
            matY[row] = matY[row] - (matY[coloumn] * Lower[row][coloumn])
        matY[row] = np.round(matY[row] / Lower[row][row], 4)
    return matY


def BackSubstitution(Upper, matY):
    n = len(Upper)
    matX = np.zeros(n, dtype=float)
    for row in range(n - 1, -1, -1):
        matX[row] = matY[row]
        for coloumn in range(n - 1, row, -1):
            matX[row] = matX[row] - (Upper[row][coloumn] * matX[coloumn])
        matX[row] = np.round((matX[row] / Upper[row][row]), 4)
    return matX


def check(matA):
    c = 0
    n = len(matA)
    for i in range(n):
        for j in range(n):
            if matA[i][j] != 0:
                c = 1
        # print(c)
        if c == 0:
            return c
        c = 0
    return 1


def LUDecomposition(matA, matB):
    Lower, Upper = LowUP(matA)
    print(Lower)
    print(Upper)
    n = len(Upper)
    ck = check(Upper)
    if ck == 0:
        print("No unique solution")
        SysCr = 1
        sys.exit(1)
    else:
        matY = ForwardSub(Lower, matB)
        print(matY)
        matX = BackSubstitution(Upper, matY)
        print(matX)
    return Lower, Upper, matY, matX


# matA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# A = [[25, 5, 1], [64, 8, 1], [144, 12, 1]]
# B = [106.8, 177.2, 279.2]
# LUDecomposition(A, B)

# file opening
f = open("in1.txt", "r")

x = f.readline()
n = int(x)

s = f.readlines()[0:n + n]
# print(s)
matA = np.zeros((n, n), dtype=float)
matB = np.zeros((n, 1), dtype=float)
array = []

for i in range(n * 2):
    st = str(s[i])
    st = st.split(" ")
    for j in range(len(st)):
        array.append(float(st[j]))
# print(array)
k = 0
for i in range(n):
    for j in range(n):
        matA[i][j] = array[k]
        k = k + 1
for i in range(n):
    matB[i][0] = array[k]
    k = k + 1

# print(matA)
# print(matB)

L, U, Y, X = LUDecomposition(matA, matB)

# write to file

f = open("out1.txt", "w")

for i in range(len(L)):
    for j in range(len(L)):
        val = format(L[i][j], ".4f")
        f.write(str(val))
        f.write(" ")
    f.write("\n")
f.write("\n")

for i in range(len(U)):
    for j in range(len(U)):
        val = format(U[i][j], ".4f")
        f.write(str(val))
        f.write(" ")
    f.write("\n")
f.write("\n")

if SysCr == 1:
    f.write("No unique solution")
else:
    for i in range(len(Y)):
        val = format(Y[i], ".4f")
        f.write(str(val))
        f.write("\n")
    f.write("\n")

    for i in range(len(X)):
        # f.write(str("%.2f"%X[i]))
        val = format(X[i], "0.4f")
        f.write(str(val))
        f.write("\n")

f.close()
