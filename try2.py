import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import sys
import math


# plt.plot(1,1, "ro")
# plt.show()

X, Y, ASSIGMENT = 0, 1, 2
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
    return math.sqrt(dx ** 2 + dy ** 2)

def graph_format(data):
    # Usage: plt.plot(graph_format(data)[X],graph_format(data)[Y],'or')
    x_val = [i[0] for i in data]
    y_val = [i[1] for i in data]
    return [x_val, y_val]


a = get_data((1, 1), (.2, .2), 10)
b = get_data((4,4), (1, 1) , 10)

data = np.concatenate((a, b), axis = 0)

# print data

# plt.plot(graph_format(a)[X],graph_format(a)[Y],'ro')
# plt.plot(graph_format(b)[X],graph_format(b)[Y],'bo')
# plt.plot(graph_format(data)[X],graph_format(data)[Y],'bo')
# plt.show()
# plt.xlim(0,10)
# plt.ylim(0,10)

#plt.show()



# Forgy initialization


# Choose k random means
initial_means_indexes = random.sample(range(0, len(data) - 1), K)
means = []
for i in initial_means_indexes:
    # means.append(data[i])]
    break
print means


means = [data[0], data[1]]
# for point in data:
#     point.append(-1)
# print data


assignments = np.array([[-1]] * len(data))
dws = np.concatenate((data, assignments), axis = 1) # defines the data with assignments








ass_colors = ["bo", "ro"]

past_dws = np.array([])
while True:
    # We're going to need to do the following every time
    ps = ""
    # Assign the points
    for point in dws :
        ps += str(point[ASSIGMENT])

        min_mean = FLOAT_MAX
        for i in range(0, len(means)):
            mean = means[i]
            distance = euclid((point[X], point[Y]), mean)
            if distance < min_mean:
                min_mean = distance
                point[ASSIGMENT] = i
    print ps
    # Check if the point assignments changed

    print (dws == past_dws)

    if (dws == past_dws).all() :
        break
    past_dws = dws

    # Recalculate Means
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

        # Plot the points by their assignment
        for point in dws :
            plt.plot(point[X], point[Y], ass_colors[int(point[ASSIGMENT])]) # PERROR: Int conversion

        # And plot the means
        for mean in means:
            plt.plot(mean[X], mean[Y], "oc")
        # plt.plot(graph_format(a)[X],graph_format(a)[Y],'gx')
        plt.show()






print dws
# ass_colors = ["bo", "ro"]
# for point in dws :
#     plt.plot(point[X], point[Y], ass_colors[int(point[ASSIGMENT])]) # PERROR: Int conversion
#
# plt.plot(graph_format(a)[X],graph_format(a)[Y],'gx')
# plt.show()
#
