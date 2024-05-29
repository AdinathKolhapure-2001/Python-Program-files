# Gradient Descent 

import numpy as np

# y = m * x + c
# m = slope --> theta 1
# c = y intercept  --> theta 0

def gradient_descent(x, y):
    m_curr = c_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.01
    
    for i in range(iterations):
        y_predicted = m_curr * x + c_curr
        cost_fun = (1 / 2 * n) * sum([val ** 2 for val in (y - y_predicted)])
        m_der = -(1 / n) * sum(x * (y - y_predicted))
        c_der = -(1 / n) * sum((y - y_predicted))
        
        m_curr = m_curr - learning_rate * m_der
        c_curr = c_curr - learning_rate * c_der
        
        print(f"m_curr = {m_curr}, c_curr = {c_curr}, cost = {cost_fun}, iteration = {i}")
        
        
x = np.array([1, 2, 3, 4, 5])

y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)
