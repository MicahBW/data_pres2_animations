import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import sys
import math
from datetime import datetime


# plt.plot(1,1, "ro")
# plt.show()

X, Y, ASSIGMENT = 0, 1, 2
K = 2
FLOAT_MAX = sys.float_info.max
ass_colors = ["b", "r", "m", "k", "g"]


def get_data(mu, sigma, length):
    if isinstance(mu, tuple) and isinstance(sigma, tuple):
        x = np.random.normal(loc=mu[0], scale=sigma[0], size = length)
        y = np.random.normal(loc=mu[-1], scale=sigma[-1], size = length)
        return np.array([x,y]).T
    else:
        print "ERROR: Ivalid use of get_data"


def euclid(p0, p1) :
    dx = p0[X] - p1[X]
    dy = p0[Y] - p1[Y]
    return math.sqrt(dx ** 2 + dy ** 2)

def graph_format(data):
    # Usage: plt.plot(graph_format(data)[X],graph_format(data)[Y],'or')
    x_val = [i[0] for i in data]
    y_val = [i[1] for i in data]
    return [x_val, y_val]

## REMEMBER TO CHANGE K
## TRIANGULAR
# a = get_data((0,0), (0.5, 0.5), 30)
# b = get_data((9,0), (0.5, 0.5), 30)
# c = get_data((5,0), (5, 0.5), 30)

## TWO LINES
a = get_data((-1,5), (0.01, 3), 30)
b = get_data((1,5), (0.01, 3), 30)


data = np.concatenate((a, b), axis = 0)

assignments = np.array([[-1]] * len(data))
dws = np.concatenate((data, assignments), axis = 1) # defines the data with assignments


prev_means = []

plt.xlim(-10, 10)
plt.ylim(-10, 10)




# Forgy Mean Initialization: Choose initial means at random from data
initial_means_indexes = random.sample(range(0, len(data)), K)
means = []
for i in initial_means_indexes:
    means.append(data[i])

for point in dws :
    plt.plot(point[X], point[Y],  "ko", markersize=10)
for mean in means:
    plt.plot(mean[X], mean[Y], "^c", markersize=10)
# plt.savefig("created_graphics/" + datetime.utcnow().strftime('%Y%m%d %H%M%S%f')[:-3] + "START")
plt.show()

while True:

    # Assignment Step
    for point in dws :

        min_mean = FLOAT_MAX
        for i in range(0, len(means)):
            mean = means[i]
            distance = euclid((point[X], point[Y]), mean)
            if distance < min_mean:
                min_mean = distance
                point[ASSIGMENT] = float(i)

    # Vizualization Step
    for point in dws :
        plt.plot(point[X], point[Y], ass_colors[int(point[ASSIGMENT])] + "o", markersize=10)
    for mean in means:
        plt.plot(mean[X], mean[Y], "^c", markersize=10)
    # plt.savefig("created_graphics/" + datetime.utcnow().strftime('%Y%m%d %H%M%S%f')[:-3])
    plt.show()



    # Update step
    mean_sum_x = mean_sum_y = 0.0
    mean_counter = 0.0
    for i in range(K):
        for point in dws:
            if point[ASSIGMENT] == i:
                mean_counter += 1
                mean_sum_x += point[X]
                mean_sum_y += point[Y]
        means[i] = (mean_sum_x/mean_counter, mean_sum_y/mean_counter)
        mean_sum_x = 0.0
        mean_sum_y = 0.0
        mean_counter = 0.0

    # Vizualization Step
    for point in dws :
        plt.plot(point[X], point[Y], ass_colors[int(point[ASSIGMENT])] + "o", markersize=10)
    for mean in means:
        plt.plot(mean[X], mean[Y], "^c", markersize=10)
    # plt.savefig("created_graphics/" + datetime.utcnow().strftime('%Y%m%d %H%M%S%f')[:-3] + "U")
    plt.show()




    # If the point assigments don't change then that imlies that the means won't have changed
    print "prev_means"
    print prev_means
    print "MEANS:"
    print means
    if prev_means == means:
        for point in dws :
            plt.plot(point[X], point[Y], ass_colors[int(point[ASSIGMENT])] + "o", markersize=10)
        for mean in means:
            plt.plot(mean[X], mean[Y], "^c", markersize=10)
        plt.savefig("created_graphics/" + datetime.utcnow().strftime('%Y%m%d %H%M%S%f')[:-3] + "FINAL")
        plt.show()
        break
    prev_means = means[:] #PERROR: Ther are now t


print dws
