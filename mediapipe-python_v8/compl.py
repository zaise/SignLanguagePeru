import os
from time import sleep
import holistic
import ImVid
import shutil

path_video='Videos'

contenido = os.listdir(path_video)

#shutil.rmtree('Salida/')

#os.makedirs('Salida', exist_ok=True)

for n in range(0,len(contenido)):
    video_n=contenido[n]
    print(n+1,'° video',video_n)
    holistic.main(video_n)
    ImVid.main()
    ImVid.Video_salida(video_n)

