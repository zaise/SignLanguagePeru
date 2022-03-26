from os import read
import os
import numpy as np
import cv2 as cv
import shutil

import pandas as pd
import glob

def main():

    shutil.rmtree('Imagenes/')

    os.makedirs('Imagenes', exist_ok=True)

    path = "Imagenes"

    datos = []

    with open("Tamaño.txt") as fname:
        lineas=fname.readlines()
        for linea in lineas:
            datos.append(linea.strip('\n'))
    
    #Ta=open("Tamaño.txt","r")  
    Size=datos[0]
    #Ta.close 
    Lim = Size.split(';')


    F = pd.read_csv('prueba_1.csv', sep=';', index_col=False,on_bad_lines='skip')    
    F1=F.Frame
    F=F.drop(['Frame', 'Tiempo'], axis=1)
    F=F.drop(F.columns[::3], axis='columns')
    f=0
    f_may=0

    if len(F1)!=0:
        f_may=F1[len(F1)-1]


    I = pd.read_csv('prueba_2.csv', sep=';', index_col=False,on_bad_lines='skip')         
    I1=I.Frame
    I=I.drop(['Frame', 'Tiempo'], axis=1)
    I2=I[:]
    I=I.drop(I.columns[::3], axis='columns')
    i=0

    i_may=0

    if len(I1)!=0:
        i_may=I1[len(I1)-1]


    M = pd.read_csv('prueba_3.csv', sep=';', index_col=False,on_bad_lines='skip')       
    M1=M.Frame
    M=M.drop(['Frame', 'Tiempo'], axis=1)
    M=M.drop(M.columns[::4], axis='columns')
    M=M.drop(M.columns[2::3], axis='columns')
    m=0
    m_may=0

    if len(M1)!=0:
        m_may=M1[len(M1)-1]

    #N_=m_may

    #if f_may>N_:
    #    N_=f_may

    #if i_may>N_:
    #    N_=i_may

    a=0

    for n in range(0,int(float(datos[1]))):
        a=a+1
        #file_name = 'Imagen_'+str(a)

        img=np.zeros((int(Lim[1]),int(Lim[0]),3), np.uint8)
        point_size = 1
        point_color = (0, 0, 500)
        point_color_manos = (500, 0, 0)

        if  n<f_may and (F1.iloc[f]==n):

            x_f=F.iloc[f,0:len(F.columns):2]
            y_f=F.iloc[f,1:len(F.columns):2]
            f=f+1        

            for f_c in range (0,468):
                cv.circle(img, (x_f[f_c],y_f[f_c]), point_size, point_color, 2)
        
    
        if  n<i_may and (I1.iloc[i]==n):

            index_=I2.iloc[i,0:len(I2.columns):3]
            x_i=I2.iloc[i,1:len(I2.columns):3]
            y_i=I2.iloc[i,2:len(I2.columns):3]
            i=i+1

            x_i[np.isnan(x_i)] = -1
            y_i[np.isnan(y_i)] = -1

            index_[np.isnan(index_)] = -1


            for i_cu in range (0,33):
                if (x_i[i_cu] and y_i[i_cu]) != -1:
                    cv.circle(img, (int(x_i[i_cu]),int(y_i[i_cu])), point_size, point_color, 4)

            for t in range (0,33):

                for t_1 in range (0,33):

                    if(index_[t]==1 and index_[t_1]==2):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==2 and index_[t_1]==3):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==4 and index_[t_1]==5):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==5 and index_[t_1]==6):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==9 and index_[t_1]==10):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==11 and index_[t_1]==12):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==11 and index_[t_1]==13):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==13 and index_[t_1]==15):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==12 and index_[t_1]==14):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==14 and index_[t_1]==16):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==15 and index_[t_1]==17):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==17 and index_[t_1]==19):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==19 and index_[t_1]==21):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==15 and index_[t_1]==21):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==16 and index_[t_1]==18):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==18 and index_[t_1]==20):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==20 and index_[t_1]==22):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==16 and index_[t_1]==22):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==11 and index_[t_1]==23):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==12 and index_[t_1]==24):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==23 and index_[t_1]==24):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==23 and index_[t_1]==25):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==25 and index_[t_1]==27):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==27 and index_[t_1]==29):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==29 and index_[t_1]==31):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==24 and index_[t_1]==26):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==26 and index_[t_1]==28):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==28 and index_[t_1]==30):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)
                    if(index_[t]==30 and index_[t_1]==32):
                        cv.line(img,(int(x_i[t]),int(y_i[t])),(int(x_i[t_1]),int(y_i[t_1])),(0, 255, 0), 2)

            
    
        if  n<m_may and (M1.iloc[m]==n):
            x_m=M.iloc[m,0:len(M.columns)-1:2]
            y_m=M.iloc[m,1:len(M.columns):2]

            for m_c in range (0,21):
                cv.circle(img, (x_m[m_c],y_m[m_c]), point_size, point_color_manos, 4)
        
            if M1.iloc[m+1]==n:
                x_m1=M.iloc[m+1,0:len(M.columns)-1:2]
                y_m1=M.iloc[m+1,1:len(M.columns):2]
                m=m+2

                for m_c in range (0,21):
                    cv.circle(img, (x_m1[m_c],y_m1[m_c]), point_size, point_color_manos, 4)
            
            else:
                m=m+1


        frames='Img'+str(a)+'.jpg'    

        cv.putText(img, "FRAME:" + str(a-1), (10, 30),cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
    
        cv.imwrite(os.path.join(path,frames),img)


def Video_salida(a):

    img_array = []

    jpg = glob.glob('Imagenes/*.jpg')
    total_jpg = len(jpg)

    for x in range (1,total_jpg):
        path1 = 'Imagenes/Img%01d.jpg' % x
        ima = cv.imread(path1)
        img_array.append(ima)

    height, width  = ima.shape[:2]

    video = cv.VideoWriter('Salida/'+str(a[:-4])+str('out')+str('.mp4'),cv.VideoWriter_fourcc(*'mp4v'),20,(width,height))
    #video = cv.VideoWriter('Salida/'+str(a[:-4])+str('out')+str('.avi'),cv.VideoWriter_fourcc(*'MJPG'),20,(width,height))
        

    for y in range(len(img_array)):
        video.write(img_array[y])

    video.release()