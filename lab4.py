import random
from scipy import stats
import pylab


def func(x):
    return x ** (3/2)


n_s = [20, 30, 50, 70, 100,  150]
len_intervalss = []
for n in n_s:
    print("Размер выборки:", n)
    a = 1
    b = 8
    Y = []
    for _ in range(n):
        Y.append(round(func(random.uniform(a, b)), 2))
    print("Вариационный ряд:\n", sorted(Y))
    x = list(sorted(Y))
    x_line = sum(x) / n
    print("Точечная оценка математического ожидания:", x_line)

    D = sum(((i - x_line) ** 2 for i in x)) / n
    print("Точечная оценка дисперсии:", D)

    S20 = sum(((i - x_line) ** 2 for i in x)) / (n - 1)
    print("Точечная несмещённая оценка дисперсии:", S20)
    a_s = [0.01, 0.05, 0.1]
    len_intervals = []
    th_m_x = 10.2868191991
    print("Теоретичесое мат. ожидание:", th_m_x)
    th_m_x2 = 146.25
    th_D = th_m_x2 - th_m_x ** 2
    print("Теоретическая дисперсия:", th_D)
    th_len_intervals = []
    for a in a_s:
        print("Уровень значимости -", 1 - a)
        b = stats.t.ppf(1 - a, n - 1) * th_D ** 0.5 / n ** 0.5
        print("Доверительныый интервал для теор. мат.")
        print(th_m_x - b, "<= x <=", th_m_x + b)
        th_len_intervals.append(2 * b)
        b = stats.t.ppf(1 - a, n - 1) * S20 ** 0.5 / n ** 0.5
        print("Доверительныый интервал для эмп. мат.")
        print(x_line - b, "<= x <=", x_line + b)
        len_intervals.append(2 * b)
    b = stats.t.ppf(1 - 0.01, n - 1) * S20 ** 0.5 / n ** 0.5
    len_intervalss.append(2 * b)

    pylab.plot(a_s, len_intervals)
    pylab.plot(a_s, th_len_intervals)
    pylab.show()
    print()
pylab.plot(n_s, len_intervalss)
pylab.show()
