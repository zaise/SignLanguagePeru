import subprocess
import os
from time import sleep
import holistic
import ImVid

path_video='C:/Users/lesli/mediapipe-python/Videos'

contenido = os.listdir(path_video)

for n in range(0,len(contenido)):
    video_n=contenido[n]
    print(n+1,'° video',video_n)
    holistic.main(video_n)
    ImVid.main()
    ImVid.Video_salida(video_n)
