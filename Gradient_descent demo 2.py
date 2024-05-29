# Gradient Descent

import numpy as np
import matplotlib.pyplot as plt

def y_function(x):
    return np.sin(x)


def y_derivative(x):
    return np.cos(x)



x = np.arange(-5, 5, 0.1)
y = y_function(x)


curr_pos = (1, y_function(1))
learning_rate = 0.09

iteration = 100

for i in range(iteration):
    x_new = curr_pos[0] - learning_rate * y_derivative(curr_pos[0])
    y_new = y_function(x_new)
    curr_pos = (x_new, y_new)
    

    plt.plot(x, y)
    plt.scatter(curr_pos[0], curr_pos[1], color = 'red')
    plt.pause(0.001)
    plt.clf()
