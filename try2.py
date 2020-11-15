import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import sys


# plt.plot(1,1, "ro")
# plt.show()

X, Y = 0, 1
K = 2
FLOAT_MAX = sys.float_info.max



def get_data(mu, sigma, length):
    if isinstance(mu, tuple) and isinstance(sigma, tuple):
        x = np.random.normal(loc=mu[0], scale=sigma[0], size = length)
        y = np.random.normal(loc=mu[-1], scale=sigma[-1], size = length)
        return np.array([x,y]).T

def euclid(p0, p1) :
    dx = p0[X] - p1[X]
    dy = p0[Y] - p1[Y]
    return sqrt(dx ** 2 + dy ** 2)

def graph_format(data):
    # Usage: plt.plot(graph_format(data)[X],graph_format(data)[Y],'or')
    x_val = [i[0] for i in data]
    y_val = [i[1] for i in data]
    return [x_val, y_val]


a = get_data((1, 1), (.5, .5), 10)
b = get_data((8,8), (1, 1) , 10)

data = np.concatenate((a, b), axis = 0)

print data

plt.plot(graph_format(a)[X],graph_format(a)[Y],'ro')
plt.plot(graph_format(b)[X],graph_format(b)[Y],'bo')
plt.show()
# plt.plot(both[0], both[1], "bx")
# plt.xlim(0,10)
# plt.ylim(0,10)

#plt.show()


# d_to_concat = np.concatenate((all_d_sets, [-1] ), axis = 1)
#
# data = all_d_sets.T
#
# # Forgy initialization
#
#
# # Choose k random means
# initial_means_indexes = random.sample(range(0, data.size - 1), K)
# means = []
# for i in initial_means_indexes:
#     means.append(data[i])
# print means
# assignments = [-1]*data.size
#
#
#
# # We're going to need to do the following every time
# for point in datas :
#     min_mean = FLOAT_MAX
#     for mean in means:
#         distance = euclid(point, mean)
#         if distance < min_mean:
#             min_mean = distance
#             assignments
#
#
#
# #
