import random
import pylab
import numpy as np
from scipy.stats import chi2


def dd_func(x):  # distribution density
    return x ** (-1 / 3) * 2 / 3 / 7


def func(x):
    return x ** (3 / 2)


def th_func(x):
    return 1 / 7 * (x ** (2 / 3))


a = 1
b = 8
n = 200
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
p_is = []
while i < len(intervals) - 1:
    frequencies.append(dx / (n * (intervals[i+1] - intervals[i])))
    p_is.append(th_func(intervals[i+1]) - th_func(intervals[i]))
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
xlist = np.arange(x[0], x[-1], 0.01)
ylist = [dd_func(x) for x in xlist]
pylab.plot(xlist, ylist)
if abs(1 - sum(p_is)) < 0.01:
    print("Контрольное соотношение выполняется")


chi_square = sum((dx - n * pi)**2 / (n * pi) for pi in p_is)
print("Хи-квадрат:", chi_square)

alpha = 0.01
k = M - 1
th_chi_square = chi2.isf(alpha, k)
if th_chi_square - chi_square:
    print("Теоретическое закон распределения соответсвует действительному")
pylab.show()
# ---------------------------------------------------------------------------------------------------------------------


def th_func(x):
    return 1 / 8 * (x ** (2 / 3))


n = 30
a = 0
b = 8
Y = []
for _ in range(n):
    Y.append(round(func(random.uniform(a, b)), 2))
i = 0
print("Вариационный ряд:\n", sorted(Y))

x_emp = list(sorted(set(Y)))
y_emp = [Y.count(x_emp[1]) / n]


for x in x_emp[1:]:
    y_emp.append(round(Y.count(x) / n + y_emp[-1], 7))

x_emp_new = [x_emp[0] - 2]
y_emp_new = [0, 0]
for y in y_emp:
    y_emp_new.append(y)
    y_emp_new.append(y)
for x in x_emp:
    x_emp_new.append(x)
    x_emp_new.append(x)
x_emp_new.append(x_emp[-1] + 2)

i = 0
while i < len(x_emp_new) // 2:
    print('\t\t{0} при y с \t({1} , {2})'.format(y_emp_new[2 * i], x_emp_new[2 * i], x_emp_new[2 * i+1]))
    i += 1

pylab.plot(x_emp_new, y_emp_new)

xlist = np.arange(func(a), func(b), 0.01)
ylist = [th_func(x) for x in xlist]
pylab.plot(xlist, ylist)
# ---------------------------------------------------------------------------------------------------------------------

max_delta1 = round(max(abs(th_func(i) - j) for i, j in zip(x_emp, y_emp)), 2)
max_delta2 = round(max(abs(th_func(i) - j) for i, j in zip(x_emp, [0] + y_emp[:-1])), 2)
max_delta = max((max_delta1, max_delta2))
print("Максимальная разность между теор. и эмп. функциями распределения:", max_delta)
emp_lambda = round(np.sqrt(n) * max_delta, 2)
th_lambda = 1.6
if emp_lambda < th_lambda:
    print("Теоретическое закон распределения соответсвует действительному")
pylab.show()
# ---------------------------------------------------------------------------------------------------------------------
n = 50
Y = []
for _ in range(n):
    Y.append(round(func(random.uniform(a, b)), 2))
i = 0
print("Вариационный ряд:\n", sorted(Y))

x_emp = list(sorted(set(Y)))
y_emp = [Y.count(x_emp[1]) / n]
for x in x_emp[1:]:
    y_emp.append(round(Y.count(x) / n + y_emp[-1], 7))
emp_d = 1 / (12 * n) + sum((th_func(i) - y_emp[k])**2 for k, i in enumerate(x_emp))
th_d = 0.744
if emp_d < th_d:
    print("Теоретическое закон распределения соответсвует действительному")