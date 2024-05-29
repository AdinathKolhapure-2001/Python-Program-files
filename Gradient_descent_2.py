# Gradient Descent


import numpy as np


def gradient_descent(x, y):
    m_curr = c_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.01
    
    for i in range(iterations):
        y_predicted = m_curr * x + c_curr
        cost = (1 / 2*n) * sum([val ** 2 for val in (y - y_predicted)])
        md = -(1 / n) * sum(x * (y - y_predicted))
        cd = -(1 / n) * sum((y - y_predicted))
        m_curr = m_curr - learning_rate * md
        c_curr = c_curr - learning_rate * cd
        
        print(f'm = {m_curr}, c_curr = {c_curr}, cost = {cost}, iteration = {i}')
        
        
        
# call the function

x = np.array([1, 2, 3, 4, 5])

y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)