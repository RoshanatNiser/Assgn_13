# Name: Roshan Yadav
# Roll No: 2311144
# Assignment: Forward and Backward Euler; and Predictor and Corrector


from Func_lib_for_assgn_13 import *

def h(x,t):
    if t==1:
        return x**2 + 2*x + 2 - 2*(math.e)**x
    if t==2:
        return math.tan(x + (math.pi)/4) + x
    
# For question 1

a=0
b=2
h=0.1
N=int((b-a)/h)
X_1=[]
L_A_1=[]
x=a
for i in range(0,N):
    X_1.append(x)
    L_A_1.append(h(x=x,t=1))
    x=x+h

L_f_1=forward_euler(t=1,a=0,b=2,y0=0)
L_b_1=backward_euler(t=1,a=0,b=2,y0=0)
L_p_1=predictor_corrector(t=1,a=0,b=2,y0=0)



# For question 2

a=0
b=(math.pi)/5
h=0.1
N=int((b-a)/h)
X_2=[]
L_A_2=[]
x=a
for i in range(0,N):
    X_2.append(x)
    L_A_2.append(h(x=x,t=2))
    x=x+h

b=(math.pi)/5
L_f_2=forward_euler(t=2,a=0,b=b,y0=1)
L_b_2=backward_euler(t=2,a=0,b=b,y0=1)
L_p_2=predictor_corrector(t=2,a=0,b=b,y0=1)




# plots

#For Question 1
plt.plot(X_1,L_f_1,label='Forward Euler')
plt.plot(X_1,L_b_1,lable='Backward Euler')
plt.plot(X_1,L_p_1,label='Predictor and Corrector')
plt.plot(X_1,L_A_1,label='Analytical value')
plt.title('For Question 1')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend(True)
plt.savefig(f"Assgn_13_Question_1.png", dpi=300, bbox_inches='tight')
plt.close()

# For Question 2
plt.plot(X_2,L_f_2,label='Forward Euler')
plt.plot(X_2,L_b_2,lable='Backward Euler')
plt.plot(X_2,L_p_2,label='Predictor and Corrector')
plt.plot(X_2,L_A_2,label='Analytical value')
plt.title('For Question 2')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend(True)
plt.savefig(f"Assgn_13_Question_2.png", dpi=300, bbox_inches='tight')
plt.close()

