import matplotlib.pyplot as plt

import numpy as np



def Expansion(valueX, iteration):
    i = 1
    count = 0
    while i <= iteration:
        if i % 2 == 0:
            count = count - (np.power(valueX, i) / i)

        else:
            count = count + (np.power(valueX, i) / i)

        i = i + 1
    return count

# Question A


x = float(input("Enter value of x = "))
iteration = int(input("Number of iteration = "))

result = Expansion(x, iteration)
print(result)

# Question B

x = np.arange(-1+.1, 1.1, .1)
y = np.array([])
for i in x:
    result = np.log(1+i)
    y = np.append(y, result)

plt.plot(x, y)
plt.title("Question b")
plt.xlabel("x")
plt.ylabel("ln(1+x)")
plt.legend()
plt.grid()
plt.show()

# Question C

x = np.arange(-1 + .1, 1.1, .1)

y = Expansion(x,1)
plt.plot(x,y)


y = Expansion(x,3)
plt.plot(x,y)


y = Expansion(x,5)
plt.plot(x,y)


y = Expansion(x,20)
plt.plot(x,y)


y = Expansion(x,50)
plt.plot(x,y)

plt.title("Question C")
plt.grid()
plt.show()

# Question D

originalValue = np.log(1.5)
x = np.arange(1, 51, 1)
y = np.array([])

for i in x:
    result = Expansion(.5, i)
    y = np.append(y, np.abs(originalValue-result))

plt.plot(x,y)
plt.title("Question D")
plt.grid()
plt.show()

