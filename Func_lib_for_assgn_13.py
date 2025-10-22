# Name: Roshan Yadav
# Roll No: 2311144
# Assignment: Function file for Forward and Backward Euler; and Predictor and Corrector

import math
import matplotlib.pyplot as plt

def f(x=0,y=0,t=1):
    # For question 1
    if t==1: # returns f(x)=y + x^2
        return y-x**2
    
    if t==11: # returns derivative of f(x)=y + x^2
        return  f(x=x,y=y,t=t) + 2*x
    
    # For question 2
    if t==2: # returns f(x)=(x+y)^2
        return (x+y)**2 
    
    if t==22: # returns derivative of f(x)=(x+y)^2
        return 2*(x+y)*(f(x=x,y=y,t=t))

    
def g(x=0,y0=0,x0=0,t=1,h=0.1,m=0):
    if m==0:
            return x- y0 - h*(f(y=x,x=x0,t=t))
    if m==1:
        if t==1:
            n=11
        if t==2:
            n==22
        return 1-h*(f(y=x,x=x0,t=n))



def forward_euler(t=1,y0=0,a=0,b=2,h=0.1):
    L=[] 
    L.append(y0)
    N=int(((b-a)/h))
    x=a
    for i in range(0,N):
        r=L[i] + h*(f(y=L[i],x=x,t=t))
        L.append(r)
        x=x+h
    
    return L

def newton_raphson(x=2,t=1, y0=0, x0=0, e=10**-6, d=10**-6):
    """This Function returns roots of a 
    function employing Newton-Raphson Method"""

    # Iteration step
    a = g( x=x, y0=y0, x0=x0, t=t, m=0)
    b = g( x=x, y0=y0, x0=x0, t=t, m=1)
    x_new = x - (a/b)

    # Checking convergence
    if abs(x_new - x) < e and abs(g( x=x, y0=y0, x0=x0, t=t, m=0)) < d:
        return x_new
    else:
        return newton_raphson(x=x_new)


def backward_euler(t=1,y0=0,a=0,b=2,h=0.1):
    L=[]
    L.append(y0)
    N=int((b-a/h))
    x=a
    for i in range(0,N):
        x_new=x+h
        y=newton_raphson(x=1,x0=x_new,y0=L[i],t=t)
        r= L[i] + h*(f(y=y,x=x_new,t=t))
        L.append(r)
    return L



def predictor_corrector(t=1,a=0,b=2,y0=0,h=0.1):
    L=[]
    L.append(y0)
    N=int((b-a/h))
    x=a
    for i in range(0,N):
        x_new=x+h
        k_1=h*(f(L[i],x,t=t))
        y_p=L[i] + k_1
        k_2= h*(f(y=y_p,x=x_new,t=t))
        r=L[i] + (k_1 + k_2)/2
        L.append(r)
    
    return L
