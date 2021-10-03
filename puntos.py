import csv
import cv2 as cv
import numpy as np
import os
path = "C:/Users/Renatto/mediapipe-python/imagenes"

cara = open('prueba_1.csv', newline='')  
reader1 = csv.reader(cara)
cuerpo = open('prueba_2.csv', newline='')
reader2 = csv.reader(cuerpo)

a=0
i=3
for row in reader1:
    img=np.zeros((800,600,3), np.uint8)
    point_size = 1
    point_color = (0, 100, 100)
            
    for i in range (3,1407,3):
        b=int(row[i])
        c=int(row[i+1])
        k=np.array([[int(row[402]),int(row[403])],[int(row[522]),int(row[523])],
                    [int(row[474]),int(row[475])],[int(row[477]),int(row[478])],
                    [int(row[480]),int(row[481])],[int(row[483]),int(row[484])],
                    [int(row[486]),int(row[487])],[int(row[741]),int(row[742])],
                    [int(row[492]),int(row[493])],[int(row[435]),int(row[436])],
                    [int(row[438]),int(row[439])],[int(row[462]),int(row[463])],
                    [int(row[465]),int(row[466])],[int(row[468]),int(row[469])],
                    [int(row[402]),int(row[403])]],np.int32)

        t=k.reshape((-1, 1, 2))

        cv.circle(img, (b,c), point_size, point_color, 4)
        cv.polylines(img, [t], 
                      True, (255, 0, 0), 2)
                #print(b,c)

            
    cv.namedWindow("image")
    cv.imshow('image', img)
    cv.waitKey (1)
    cv.destroyAllWindows()
    frames='punto'+str(a)+'.jpg'
    cv.imwrite(os.path.join(path,frames),img)
    a+=1
cara.close()
cuerpo.close()



    #for row in reader:
        #print(row[i])