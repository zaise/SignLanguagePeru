import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

F = np.genfromtxt(open('prueba_1.csv','r'), delimiter=',', invalid_raise = False)
F[np.isnan(F)] = 0
F1=F[:,0]
F=np.delete(F,[0,1],axis=1) 
F=np.delete(F,np.s_[::3],axis=1)
f=0
f_may=F1[len(F1)-1]


I=np.genfromtxt(open('prueba_2.csv','r'), delimiter=',', invalid_raise = False)
I[np.isnan(I)] = 0
I1=I[:,0]
I=np.delete(I,[0,1],axis=1) 
I2=I
I=np.delete(I,np.s_[::3],axis=1)
i=0
i_may=I1[len(I1)-1]


M=np.genfromtxt(open('prueba_3.csv','r'), delimiter=',', invalid_raise = False)
M[np.isnan(M)] = 0
M1=M[:,0]
M=np.delete(M,[0,1],axis=1) 
M=np.delete(M,np.s_[::4],axis=1)
M=np.delete(M,np.s_[2::3],axis=1)
m=0
m_may=M1[len(M1)-1]

N_=m_may

if f_may>N_:
    
    N_=f_may

if i_may>N_:
    
    N_=i_may


for n in range(0,int(N_)+1):
    if  n<f_may and (F1[f]==n):
        x_f=F[f,0::2]
        y_f=F[f,1::2]
        f=f+1        
        plt.scatter(x_f,-y_f, marker=".", color="red")
        plt.show(block=False)
        
    
    if  n<i_may and (I1[i]==n):
        x_i=I[i,0::2]
        y_i=I[i,1::2]
        i=i+1
        plt.scatter(x_i,-y_i, marker=".", color="green")
        plt.show(block=False)
    
    if  n<m_may and (M1[m]==n):
        x_m=M[m,0::2]
        y_m=M[m,1::2]
        plt.scatter(x_m,-y_m, marker=".", color="orange")
        plt.show(block=False)
        if M1[m+1]==n:
            x_m1=M[m+1,0::2]
            y_m1=M[m+1,1::2]
            m=m+2
            plt.scatter(x_m1,-y_m1, marker=".", color="blue")
            plt.show(block=False)
        
        else:
            m=m+1

    plt.axis([0, 1000, -700, 30])
    plt.pause(1)
    plt.close()
    