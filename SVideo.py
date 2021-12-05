import cv2 as cv
img_array = []

for x in range (0,481):
    path1 = 'C:/Users/lesli/mediapipe-python/imagenes/img%01d.jpg' % x
    ima = cv.imread(path1)
    img_array.append(ima)

height, width  = ima.shape[:2]

'''for x in range(0,len(archivos)):
    Narchivo = archivos[x]
    Darchivo = path1 + str(Narchivo)
    ima=cv.imread(Darchivo)
    img_array.append(ima)'''

video = cv.VideoWriter('SVideo.mp4',cv.VideoWriter_fourcc(*'mp4v'),20,(width,height))
        

for y in range(len(img_array)):
    video.write(img_array[y])

video.release()