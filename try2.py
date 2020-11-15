import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


# plt.plot(1,1, "ro")
# plt.show()

X, Y = 0, 1
K = 2


def get_data(mu, sigma, length):
    if isinstance(mu, tuple) and isinstance(sigma, tuple):
        x = np.random.normal(loc=mu[0], scale=sigma[0], size = length)
        y = np.random.normal(loc=mu[-1], scale=sigma[-1], size = length)
        return [x,y]

def euclid(p0, p1) :
    dx = p0[X] - p1[X]
    dy = p0[Y] - p1[Y]
    return sqrt(dx ** 2 + dy ** 2)


a = get_data((1, 1), (.5, .5), 10)
b = get_data((8,8), (1, 1) , 10)

both = np.concatenate((a, b), axis = 1)



plt.plot(a[0], a[1], "ro")
plt.plot(b[0], b[1], "bo")
# plt.plot(both[0], both[1], "bx")
# plt.xlim(0,10)
# plt.ylim(0,10)

plt.show()


# Forgy initialization


# Choose k random means
