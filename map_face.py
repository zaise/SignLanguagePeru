#M=csvread('C:\Users\ronyn\mediapipe-python\prueba_1.csv');
#M(:,[1 2])=[];
#M(:,[1:3:1405])=[];
#for n=1:336
#    x=M(n,1:2:936);
#    y=M(n,2:2:936);
#    plot(x,y,'r:+');
#    drawnow;
#    pause(0.3)
#end 

import matplotlib.pyplot as plt

def plotframe(datos):
    
    d = datos.strip().split(',')
    del d[0:2], d[-1]
    d = [int(i) for i in d]

    dclean_x = d[1:1404:3]
    dclean_y = d[2:1405:3]

    plt.scatter(dclean_x, dclean_y)
    plt.show(block=False)
    plt.pause(10)
    plt.close()
    
with open('prueba_1.csv','r') as fi:
    datos = fi.readlines()
    
for n in range(468):
    plotframe(datos[n])

        





