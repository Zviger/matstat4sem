import random
import pylab
import numpy as np


def dd_func(x):  # distribution density
    return x ** (-1 / 3) * 2 / 3 / 7


def func(x):
    return x ** (3 / 2)


def th_func(x):
    return 1 / 7 * (x ** (2 / 3))


a = 1
b = 8
print("Введите N:")
n = int(input())
Y = []
for _ in range(n):
    Y.append(round(func(random.uniform(a, b)), 2))
i = 0
print("Вариационный ряд:\n", sorted(Y))
x = list(sorted(Y))

if n < 100:
    M = int(n ** 0.5)
else:
    M = int(2 * np.log(n))
dx = (x[-1] - x[0]) / M
intervals = []
for i in range(M + 1):
    intervals.append(x[0] + i * dx)
frequencies = [0] * (len(intervals) - 1)
for i in x:
    j = 1
    while j < len(intervals):
        if i == intervals[j]:
            if j + 1 == len(intervals):
                frequencies[j - 1] += 1
            else:
                frequencies[j - 1] += 0.5
                frequencies[j] += 0.5
            j += 1
        elif i < intervals[j]:
            frequencies[j - 1] += 1
            break
        else:
            j += 1
y_g1 = frequencies[:]
i = 0
while i < len(y_g1):
    y_g1[i] = y_g1[i] / (n * dx)
    i += 1
x_g1_new = []
for i in intervals:
    x_g1_new.append(i)
    x_g1_new.append(i)
y_g1_new = [0]
for i in y_g1:
    y_g1_new.append(i)
    y_g1_new.append(i)
y_g1_new.append(0)
print("Гистограмма равноинтервальным методом:")
i = 1
while i < len(intervals):
    print('\t\t{0} при y с \t({1} , {2})'.format(y_g1_new[2 * i], x_g1_new[2 * i - 1], x_g1_new[2 * i]))
    i += 1
pylab.plot(x_g1_new, y_g1_new)
# ---------------------------------------------------------------------------------------------------------------------
xlist = np.arange(x[0] + 0.00001, x[-1], 0.01)
ylist = [dd_func(x) for x in xlist]
pylab.plot(xlist, ylist)
pylab.show()
# ---------------------------------------------------------------------------------------------------------------------
x = []
y = []
for i in intervals[:-1]:
    x.append(i + dx / 2)
for i in x:
    y.append(Y.count(i))
pylab.plot(x_g1_new, y_g1_new)
pylab.plot(x, y_g1)
pylab.show()
# ---------------------------------------------------------------------------------------------------------------------
x_emp = intervals[:]
y_emp = [0]
for i in frequencies:
    y_emp.append(round(y_emp[-1] + i / n, 5))
y_emp.append(1)
x_emp_new = [x_emp[0] - 2]
y_emp_new = []
for i in y_emp:
    y_emp_new.append(i)
    y_emp_new.append(i)
for i in x_emp:
    x_emp_new.append(i)
    x_emp_new.append(i)
x_emp_new.append(x_emp[-1] + 2)
print("Эмпирическая функция распределения:")
i = 0
while i < len(x_emp):
    print('\t\t{0} при y с \t({1} , {2})'.format(y_emp_new[2 * i], x_emp_new[2 * i], x_emp_new[2 * i + 1]))
    i += 1
pylab.plot(x_emp_new, y_emp_new)
pylab.show()
# ---------------------------------------------------------------------------------------------------------------------
x = list(sorted(Y))
while n % M != 0:
    M -= 1
dx = n // M
intervals = [x[0]]
for i in range(dx - 1, n, dx):
    intervals.append(x[i])
frequencies = []
i = 0
while i < len(intervals) - 1:
    frequencies.append(dx / (n * (intervals[i+1] - intervals[i])))
    i += 1
y_g2 = frequencies[:]
x_g2_new = []
for i in intervals:
    x_g2_new.append(i)
    x_g2_new.append(i)
y_g2_new = [0]
for i in y_g2:
    y_g2_new.append(i)
    y_g2_new.append(i)
y_g2_new.append(0)
print("Гистограмма равновероятностным методом методом:")
i = 1
while i < len(intervals):
    print('\t\t{0} при y с \t({1} , {2})'.format(y_g2_new[2 * i], x_g2_new[2 * i - 1], x_g2_new[2 * i]))
    i += 1
pylab.plot(x_g2_new, y_g2_new)
# ---------------------------------------------------------------------------------------------------------------------
xlist = np.arange(x[0] + 0.00001, x[-1], 0.01)
ylist = [dd_func(x) for x in xlist]
pylab.plot(xlist, ylist)
pylab.show()
# ---------------------------------------------------------------------------------------------------------------------
x_emp = intervals[:]
y_emp = [0]
for i in frequencies:
    y_emp.append(round(y_emp[-1] + dx / n, 5))
y_emp.append(1)
x_emp_new = [x_emp[0] - 2]
y_emp_new = []
for i in y_emp:
    y_emp_new.append(i)
    y_emp_new.append(i)
for i in x_emp:
    x_emp_new.append(i)
    x_emp_new.append(i)
x_emp_new.append(x_emp[-1] + 2)
print("Эмпирическая функция распределения:")
i = 0
while i < len(x_emp):
    print('\t\t{0} при y с \t({1} , {2})'.format(y_emp_new[2 * i], x_emp_new[2 * i], x_emp_new[2 * i + 1]))
    i += 1
pylab.plot(x_emp_new, y_emp_new)
pylab.show()
# ---------------------------------------------------------------------------------------------------------------------
