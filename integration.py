import matplotlib.pyplot as plt

gx = []
gfx = []


def trapezoid(h, fx0, fx1):
    # print("applying trap")
    # print("value = " + str(h * (fx0 + fx1) / 2))
    # print("\n")
    FX0 = fx[fx0]
    FX1 = fx[fx1]

    gx.append(x[fx0])
    gx.append(x[fx1])

    gfx.append(fx[fx0])
    gfx.append(fx[fx1])

    plt.fill_between(gx, gfx, color="yellow")
    del gx[:]
    del gfx[:]

    return h * (FX0 + FX1) / 2


def simpsonOneThird(h, fx0, fx1, fx2):
    # print("applying 1/3")
    # print("value = " + str((2 * h) * (fx0 + 4 * fx1 + fx2) / 6))
    # print("\n")
    # h = b - a
    FX0 = fx[fx0]
    FX1 = fx[fx1]
    FX2 = fx[fx2]

    gx.append(x[fx0])
    gx.append(x[fx1])
    gx.append(x[fx2])

    gfx.append(fx[fx0])
    gfx.append(fx[fx1])
    gfx.append(fx[fx2])

    plt.fill_between(gx, gfx, color="blue")
    del gx[:]
    del gfx[:]

    return (2 * h) * (FX0 + 4 * FX1 + FX2) / 6


def simpsonThreeEighth(h, fx0, fx1, fx2, fx3):
    # print("applying 3/8")
    # print("value = " + str((3 * h / 8) * (fx0 + 3 * fx1 + 3 * fx2 + fx3)))
    # print("\n")
    # h = b - a
    FX0 = fx[fx0]
    FX1 = fx[fx1]
    FX2 = fx[fx2]
    FX3 = fx[fx3]

    gx.append(x[fx0])
    gx.append(x[fx1])
    gx.append(x[fx2])
    gx.append(x[fx3])

    gfx.append(fx[fx0])
    gfx.append(fx[fx1])
    gfx.append(fx[fx2])
    gfx.append(fx[fx3])

    plt.fill_between(gx, gfx, color="red")
    del gx[:]
    del gfx[:]

    return (3 * h / 8) * (FX0 + 3 * FX1 + 3 * FX2 + FX3)


f = open("input.txt", "r")
p = f.readline()
p = int(p)
x = []
fx = []
tempFX = []
tempX = []
for line in f:
    X, Y = line.split(" ", 1)
    X = float(X)
    Y = float(Y)
    x.append(X)
    fx.append(Y)
f.close()

TrapezoidCount = 0
Simpson13Count = 0
Simpson38Count = 0

tempFX = fx.copy()
tempX = x.copy()

plt.plot(x, fx)
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid()

# print(p)
# print(x)
# print(fx)

# straight from book
h = round(x[1] - x[0], 5)

result = []
# print(" p = " + str(p))
numberOfInterval = 1
x.append(9999999999999)
fx.append(9999999999999)

for i in range(1, p):
    hf = round(x[i + 1] - x[i], 5)
    if h == hf:
        numberOfInterval = numberOfInterval + 1
    else:
        if numberOfInterval == 1:

            result.append(trapezoid(h, i - 1, i))
            TrapezoidCount += 1

        elif numberOfInterval == 2:

            result.append(simpsonOneThird(h, i - 2, i - 1, i))
            Simpson13Count += 2

        elif numberOfInterval == 3:

            result.append(simpsonThreeEighth(h, i - 3, i - 2, i - 1, i))
            Simpson38Count += 3

        elif numberOfInterval == 4:

            result.append(simpsonOneThird(h, i - 4, i - 3, i - 2))
            Simpson13Count += 2

            result.append(simpsonOneThird(h, i - 2, i - 1, i))
            Simpson13Count += 2

        elif numberOfInterval > 4:
            temp = i
            while numberOfInterval > 4:
                result.append(simpsonThreeEighth(h, temp - 3, temp - 2, temp - 1, temp))
                Simpson38Count += 3
                numberOfInterval -= 3

                temp -= 3

            if numberOfInterval == 1:
                result.append(trapezoid(h, temp - 1, temp))
                TrapezoidCount += 1

            elif numberOfInterval == 2:
                result.append(simpsonOneThird(h, temp - 2, temp - 1, temp))
                Simpson13Count += 2

            elif numberOfInterval == 3:
                result.append(simpsonThreeEighth(h, temp - 3, temp - 2, temp - 1, temp))
                Simpson38Count += 3

            elif numberOfInterval == 4:
                result.append(simpsonOneThird(h, temp - 4, temp - 3, temp - 2))

                result.append(simpsonOneThird(h, temp - 2, temp - 1, temp))

                Simpson13Count += 4
        h = hf
        numberOfInterval = 1

FinalResult = 0

for k in result:
    FinalResult = FinalResult + k

print("Trapezoidal: " + str(TrapezoidCount) + " intervals")
print("Simpson  1 3: " + str(Simpson13Count) + " intervals")
print("Simpson 3 8: " + str(Simpson38Count) + " intervals")
print("Integral value = " + str(FinalResult))

# print(tempX)
# print(tempFX)

plt.plot(tempX, tempFX, "YELLOW", label="Trapezoidal")
plt.plot(tempX, tempFX, "BLUE", label="Simpson 1/3")
plt.plot(tempX, tempFX, "RED", label="Simpson 3/8")

plt.plot(tempX, tempFX, color="black")
plt.scatter(tempX, tempFX, color="black")
plt.legend()
plt.show()

OUT = open("output.txt", "w")
OUT.write("Trapezoidal: "+str(TrapezoidCount)+" intervals"+"\n")
OUT.write("Simpson 1 3: "+str(Simpson13Count)+" intervals"+"\n")
OUT.write("Simpson 3 8: "+str(Simpson38Count)+" intervals"+"\n")
OUT.write("Integral value: "+str(FinalResult))
OUT.close()

