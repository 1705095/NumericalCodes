import numpy as np
import matplotlib.pyplot as plt


def function(x, y):
    return (x + (20 * y)) * np.sin(x * y)
    # return x * np.sqrt(y)


def euler(lower, upper, step_Size, initial_value):
    EulerX = []
    while lower < upper:
        EulerX.append(float(lower))
        lower = lower + step_Size

    EulerY = [float(initial_value)]
    index = 1
    for x in EulerX:
        result = EulerY[index - 1] + step_Size * function(x, EulerY[index - 1])
        EulerY.append(float(result))
        index += 1
    EulerX.append(float(upper))
    return EulerX, EulerY


def RK2ndOrder(lower, upper, step_size, initial_value, a2):
    a1 = 1 - a2
    p1 = (1 / 2) * (1 / a2)
    q11 = (1 / 2) * (1 / a2)
    arrX = []
    arrY = [float(initial_value)]

    while lower < upper:
        arrX.append(float(lower))
        lower = lower + step_size
    index = 0
    for x in arrX:
        k1 = function(x, arrY[index])
        k2 = function(x + p1 * step_size, arrY[index] + q11 * k1 * step_size)
        result = arrY[index] + (a1 * k1 + a2 * k2) * step_size
        arrY.append(float(result))
        index += 1
    arrX.append(upper)
    return arrX, arrY


def heun(lower, upper, step_size, initial_value, a2):
    arrX, arrY = RK2ndOrder(lower, upper, step_size, initial_value, a2)
    return arrX, arrY


def midpoint(lower, upper, step_size, initial_value, a2):
    arrX, arrY = RK2ndOrder(lower, upper, step_size, initial_value, a2)
    return arrX, arrY


def ralston(lower, upper, step_size, initial_value, a2):
    arrX, arrY = RK2ndOrder(lower, upper, step_size, initial_value, a2)
    return arrX, arrY


def RK4thOrder(lower, upper, step_size, initial_value):
    arrX = []
    while lower < upper:
        arrX.append(float(lower))
        lower = lower + step_size
    arrY = [float(initial_value)]
    index = 0
    for x in arrX:
        k1 = function(x, arrY[index])
        k2 = function(x + (step_size / 2), arrY[index] + (k1 * step_size) / 2)
        k3 = function(x + (step_size / 2), arrY[index] + (k2 * step_size) / 2)
        k4 = function(x + step_size, arrY[index] + (k3 * step_size))
        result = arrY[index] + ((k1 + 2 * k2 + 2 * k3 + k4) * step_size) * (1.0 / 6.0)
        arrY.append(float(result))
        index = index + 1
    arrX.append(float(upper))
    return arrX, arrY


eux1, euy1 = euler(0, 10, .01, 4)
eux2, euy2 = euler(0, 10, .05, 4)
eux3, euy3 = euler(0, 10, .1, 4)
eux4, euy4 = euler(0, 10, .5, 4)

hx1, hy1 = heun(0, 10, .01, 4, (1 / 2))
hx2, hy2 = heun(0, 10, .05, 4, (1 / 2))
hx3, hy3 = heun(0, 10, .1, 4, (1 / 2))
hx4, hy4 = heun(0, 10, .5, 4, (1 / 2))

mdx1, mdy1 = midpoint(0, 10, .01, 4, 1)
mdx2, mdy2 = midpoint(0, 10, .05, 4, 1)
mdx3, mdy3 = midpoint(0, 10, .1, 4, 1)
mdx4, mdy4 = midpoint(0, 10, .5, 4, 1)

rsx1, rsy1 = ralston(0, 10, .01, 4, (2 / 3))
rsx2, rsy2 = ralston(0, 10, .05, 4, (2 / 3))
rsx3, rsy3 = ralston(0, 10, .1, 4, (2 / 3))
rsx4, rsy4 = ralston(0, 10, .5, 4, (2 / 3))

rkx1, rky1 = RK4thOrder(0, 10, .01, 4)
rkx2, rky2 = RK4thOrder(0, 10, .05, 4)
rkx3, rky3 = RK4thOrder(0, 10, .1, 4)
rkx4, rky4 = RK4thOrder(0, 10, .5, 4)

plt.figure(1)
plt.title("Step size = .01")
plt.plot(eux1, euy1, label="Euler")
plt.plot(hx1, hy1, label="Heun")
plt.plot(mdx1, mdy1, label="Middle Point")
plt.plot(rsx1, rsy1, label="Ralston")
plt.plot(rkx1, rky1, label="RK 4th")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

plt.figure(2)
plt.title("Step size = .05")
plt.plot(eux2, euy2, label="Euler")
plt.plot(hx2, hy2, label="Heun")
plt.plot(mdx2, mdy2, label="Middle Point")
plt.plot(rsx2, rsy2, label="Ralston")
plt.plot(rkx2, rky2, label="RK 4th")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

plt.figure(3)
plt.title("Step size = .1")
plt.plot(eux3, euy3, label="Euler")
plt.plot(hx3, hy3, label="Heun")
plt.plot(mdx3, mdy3, label="Middle Point")
plt.plot(rsx3, rsy3, label="Ralston")
plt.plot(rkx3, rky3, label="RK 4th")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

plt.figure(4)
plt.title("Step size = .5")
plt.plot(eux4, euy4, label="Euler")
plt.plot(hx4, hy4, label="Heun")
plt.plot(mdx4, mdy4, label="Middle Point")
plt.plot(rsx4, rsy4, label="Ralston")
plt.plot(rkx4, rky4, label="RK 4th")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

plt.figure(5)
plt.title("Euler")
plt.plot(eux1, euy1, label=".01")
plt.plot(eux2, euy2, label=".05")
plt.plot(eux3, euy3, label=".1")
plt.plot(eux4, euy4, label=".5")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

plt.figure(6)
plt.title("Heun")
plt.plot(hx1, hy1, label=".01")
plt.plot(hx2, hy2, label=".05")
plt.plot(hx3, hy3, label=".1")
plt.plot(hx4, hy4, label=".5")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

plt.figure(7)
plt.title("Midpoint")
plt.plot(mdx1, mdy1, label=".01")
plt.plot(mdx2, mdy2, label=".05")
plt.plot(mdx3, mdy3, label=".1")
plt.plot(mdx4, mdy4, label=".5")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

plt.figure(8)
plt.title("Ralston")
plt.plot(rsx1, rsy1, label=".01")
plt.plot(rsx2, rsy2, label=".05")
plt.plot(rsx3, rsy3, label=".1")
plt.plot(rsx4, rsy4, label=".5")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

plt.figure(9)
plt.title("RK 4th")
plt.plot(rkx1, rky1, label=".01")
plt.plot(rkx2, rky2, label=".05")
plt.plot(rkx3, rky3, label=".1")
plt.plot(rkx4, rky4, label=".5")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
