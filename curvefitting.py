import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
file = open("data.txt", "r")
count = 0

for line in file:
    X, Y = line.split(" ", 1)
    x.append(float(X))
    y.append(float(Y))
    count = count + 1

plt.scatter(x, y, s=1, edgecolors="blue")

# x1 = x.sort()
countY = 0

SumX = 0
SumX2 = 0
SumX3 = 0
SumX4 = 0
SumX5 = 0
SumX6 = 0

SumY = 0

SumXY = 0
SumX2Y = 0
SumX3Y = 0
for i in x:
    SumX = SumX + i
    SumX2 = SumX2 + (i * i)
    SumX3 = SumX3 + (i * i * i)
    SumX4 = SumX4 + (i * i * i * i)
    SumX5 = SumX5 + (i * i * i * i * i)
    SumX6 = SumX6 + (i * i * i * i * i * i)

for i in y:
    SumY = SumY + i
    countY = countY + 1

for i, j in zip(x, y):
    SumXY = SumXY + i * j
    SumX2Y = SumX2Y + (i * i * j)
    SumX3Y = SumX3Y + (i * i * i * j)

# first order #

matA1 = np.array([[count, SumX],
                  [SumX, SumX2]])
matB1 = np.array([SumY, SumXY])

# Second order #

matA2 = np.array([[count, SumX, SumX2],
                  [SumX, SumX2, SumX3],
                  [SumX2, SumX3, SumX4]])
matB2 = np.array([SumY, SumXY, SumX2Y])

# third order #

matA3 = np.array([[count, SumX, SumX2, SumX3],
                  [SumX, SumX2, SumX3, SumX4],
                  [SumX2, SumX3, SumX4, SumX5],
                  [SumX3, SumX4, SumX5, SumX6]])
matB3 = np.array([SumY, SumXY, SumX2Y, SumX3Y])

# First order solve

mat1 = np.linalg.solve(matA1, matB1)
fa0 = mat1[0]
fa1 = mat1[1]

print("Printing matrix")
print(matA1)
print(matB1)
print(mat1)
# Second order solve

mat2 = np.linalg.solve(matA2, matB2)
sa0 = mat2[0]
sa1 = mat2[1]
sa2 = mat2[2]

# Third order solve

mat3 = np.linalg.solve(matA3, matB3)
ta0 = mat3[0]
ta1 = mat3[1]
ta2 = mat3[2]
ta3 = mat3[3]


def FirstO(p):
    return fa0 + (fa1 * p)


def SecondO(p):
    return sa0 + (sa1 * p) + (sa2 * p * p)


def ThirdO(p):
    return ta0 + (ta1 * p) + (ta2 * p * p) + (ta3 * p * p * p)


avgY = SumY / countY
sT = 0
sR1 = 0
sR2 = 0
sR3 = 0

for i in y:
    sT = sT + (i - avgY) ** 2
for i, j in zip(y, x):
    sR1 = sR1 + (i - FirstO(j)) ** 2
    sR2 = sR2 + (i - SecondO(j)) ** 2
    sR3 = sR3 + (i - ThirdO(j)) ** 2

Cor1 = (((sT - sR1) / sT) ** .5)
Cor2 = (((sT - sR2) / sT) ** .5)
Cor3 = (((sT - sR3) / sT) ** .5)

print("First order solve:")
print("a0 = " + str(fa0))
print("a1 = " + str(fa1))
print("Regression coefficient: " + str(Cor1))
print("\n")

print("Second order solve:")
print("a0 = " + str(sa0))
print("a1 = " + str(sa1))
print("a2 = " + str(sa2))
print("Regression coefficient: " + str(Cor2))
print("\n")

print("Third order solve:")
print("a0 = " + str(ta0))
print("a1 = " + str(ta1))
print("a2 = " + str(ta2))
print("a3 = " + str(ta3))
print("Regression coefficient: " + str(Cor3))
print("\n")

Fx = x
Fy = []
Sx = x
Sy = []
Tx = x
Ty = []
x1 = x.sort()

for i in x:
    Fy.append(FirstO(i))
    Sy.append(SecondO(i))
    Ty.append(ThirdO(i))

plt.plot(Fx, Fy, label="First Order")
plt.plot(Sx, Sy, label="Second Order")
plt.plot(Tx, Ty, label="Third Order")

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
file.close()
