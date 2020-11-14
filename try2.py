import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# plt.plot(1,1, "ro")
# plt.show()


def get_data(mu, sigma, length):
    if isinstance(mu, tuple) and isinstance(sigma, tuple):
        x = np.random.normal(loc=mu[0], scale=sigma[0], size = length)
        y = np.random.normal(loc=mu[-1], scale=sigma[-1], size = length)
        return [x,y]

a = get_data((1, 1), (.1, .1), 10)
b = get_data((3,3), (.3, .3) , 10)

plt.plot(a[0], a[1], "ro")
plt.plot(b[0], b[1], "ro")
plt.show()




"""
def get_data(mu, sigma, length):
    def convert(list):
        return tuple(i for i in list)
    a = np.random.normal(loc=mu, scale=sigma, size=(length, 2))
    ret = []
    for element in a:
        ret.append(convert(element))

    return ret
"""
