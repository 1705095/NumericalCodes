import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.000, 1, .01)
y = np.array([])

for i in x:
    result = ((i / (1 - i)) * np.sqrt(6 / (2 + i))) - .05
    y = np.append(y, result)

plt.plot(x, y)
plt.grid()
plt.show()

function = lambda x: x ** 3 - 2400 * x ** 2 - 3 * x + 2


def secant_method(function, fst_guess, sec_guess, tol, max_iter):
    x0 = fst_guess
    x1 = sec_guess
    loopCount = 0

    while loopCount < max_iter and abs(function(x1) - function(x0)) > tol:
        x2 = ((x0 * function(x1)) - (x1 * function(x0))) / (function(x1) - function(x0))
        x0 = x1
        x1 = x2
        loopCount = loopCount + 1
    return x2, loopCount


root, itr = secant_method(function, 0, 1, .005, 200)
print("secant root = ", root)
print("iteration in secant =", itr)


def false_position(function, lower_bound, upper_bound, error, max_itr):
    if function(lower_bound) * function(upper_bound) >= 0:
        return -1
    result = lower_bound
    count = 0

    for i in range(max_itr):
        result = ((lower_bound * function(upper_bound)) - (upper_bound * function(lower_bound))) / (
                function(upper_bound) - function(lower_bound))

        if function(result) <= error:
            break

        elif function(result) * function(lower_bound) < 0:
            upper_bound = result
        else:
            lower_bound = result
        count = count + 1
    return result, count


root, count = false_position(function, 0, 1, .005, 200)
print("false position root = ", root)
print("false position iteration = ", count)
