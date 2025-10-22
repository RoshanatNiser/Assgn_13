# Name: Roshan Yadav
# Roll No: 2311144
# Assignment: Function file for Forward and Backward Euler; and Predictor and Corrector

import math
import matplotlib.pyplot as plt

def f(x=0, y=0, t=1):
    """Returns the function f(x,y)"""

    # For question 1: dy/dx = y - x^2
    if t == 1:
        return y - x**2
    
    # Derivative of f for question 1 (for Newton-Raphson)
    if t == 11:
        return y - x**2 - 2*x
    
    # For question 2: dy/dx = (x+y)^2
    if t == 2:
        return (x + y)**2 
    
    # Derivative of f for question 2 (for Newton-Raphson)
    if t == 22:
        return 2*(x + y)*(1 + f(t=2,x=x,y=y))


def g(y=0, y0=0, x0=0, t=1, h=0.1, m=0):
    """Implicit linear function for Newton-Raphson in Backward Euler"""

    if m == 0:
        # Implicit Function: y - y0 - h*f(x0, y)
        return y - y0 - h*(f(y=y, x=x0, t=t))
    
    if m == 1:
        # Derivative of the function
        if t == 1:
            return 1- h*(f(x=x0,y=y,t=1)/f(x=x0,y=y,t=11))
        if t == 2:
            return 1- h*(f(x=x0,y=y,t=2)/f(x=x0,y=y,t=22))


def forward_euler(t=1, y0=0, a=0, b=2, h=0.1):
    """Forward Euler method to solve ODE"""

    L = [] 
    L.append(y0)
    N = int((b - a) / h)
    x = a
    for i in range(0, N):
        x = x + h
        y_new = L[i] + h * (f(y=L[i], x=x, t=t))
        L.append(y_new)
    
    return L


def newton_raphson(x=2, t=1, y0=0, x0=0, h=0.1, e=10**-6, d=10**-6, max_iter=100):
    """Newton-Raphson method for implicit equation"""
    for i in range(max_iter):
        G = g(y=x, y0=y0, x0=x0, t=t, h=h, m=0)
        dG = g(y=x, y0=y0, x0=x0, t=t, h=h, m=1)

        x_new=x + (G/dG)

        if abs(g(y=x_new)-g(y=x)) < e:
            return x_new
        
    if abs(x - x_new)<d:
        return x_new
    else: 
        return x_new
      

def backward_euler(t=1, y0=0, a=0, b=2, h=0.1):
    """Backward Euler method to solve ODE"""
    L = [y0]
    N = int((b - a) / h)
    x = a
    for i in range(N):
        x_new = x + h
        
        # Initial guess
        m=L[i] + h*(f(y=L[i],x=x,t=t))
        # Newton-Raphson step
        y_new = newton_raphson(x=m, x0=x_new, y0=L[i], t=t, h=h)

        y_new= L[i] + h*(f(t=t,y=y_new,x=x_new))
        
        L.append(y_new)
        x = x_new
    return L


def predictor_corrector(t=1, a=0, b=2, y0=0, h=0.1):
    """Predictor-Corrector method to solve ODE"""
    L = []
    L.append(y0)
    N = int((b - a) / h)
    x = a
    for i in range(0, N):
        x_new = x + h
        # Predictor step
        k_1 = h * (f(y=L[i], x=x, t=t))
        y_p = L[i] + k_1
        # Corrector step
        k_2 = h * (f(y=y_p, x=x_new, t=t))
        r = L[i] + (k_1 + k_2) / 2
        L.append(r)
        x = x + h
    
    return L