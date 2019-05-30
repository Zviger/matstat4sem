import random
import pylab
import numpy as np


def func(x):
    return x ** (3/2)


def th_func(x):
    return 1/8 * (x ** (2/3))


a = 0
b = 8
print("Введите N:")
n = int(input())
Y = []
for _ in range(n):
    Y.append(round(func(random.uniform(a, b)), 2))
i = 0


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

xlist = np.arange(0, func(b), 0.01)
ylist = [th_func(x) for x in xlist]
pylab.plot(xlist, ylist)
pylab.show()
