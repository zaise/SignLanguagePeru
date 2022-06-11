#import subprocess
from cgitb import reset
import os
import holistic
import ImVid
from time import sleep
import functools


# Iterable con las rutas de los scripts
#scripts_paths = ("C:/Users/lesli/mediapipe-python/holistic.py", "C:/Users/lesli/mediapipe-python/nuevo_7.py", "C:/Users/lesli/mediapipe-python/SVideo.py")
#procesos = [subprocess.Popen(["python", script]).communicate() for script in scripts_paths]

'''path_video='C:/Users/lesli/mediapipe-python/Videos'

contenido = os.listdir(path_video)
'''

if not os.path.exists('csv'):
    os.makedirs('csv')


path_video='Videos'

contenido = os.listdir(path_video)

#shutil.rmtree('Salida/')

#os.makedirs('Salida', exist_ok=True)

#os.makedirs(path_video, exist_ok=True)

videos_iniciales=len(contenido)

@functools.lru_cache(maxsize=None)
def main(n):

    print('video',str(n+1)+str('/')+str(videos_iniciales),contenido[n])
    print('Sacando puntos...')
    holistic.main(contenido[n])
    sleep(0.1)
    print('Sacando Imagenes...')
    ImVid.main(contenido[n])
    print('Sacando Videos...')
    ImVid.Video_salida(contenido[n])
    main.cache_clear()

for n in range(0,videos_iniciales):
    demo=main(n)




'''@functools.lru_cache(maxsize=None)
def main(n):
    print('video',str(n+1)+str('/')+str(videos_iniciales),contenido[n])
    print('Sacando puntos...')
    holistic.main(contenido[n])
    sleep(0.1)
    print('Sacando Imagenes...')
    ImVid.main()
    print('Sacando Videos...')
    ImVid.Video_salida(contenido[n])
    

for n in range(0,videos_iniciales):
    demo=main(n)
    main.cache_clear()'''








'''for n in range(0,videos_iniciales):
    video_n=contenido[0]
    print('video',str(n+1)+str('/')+str(videos_iniciales),video_n)
    print('Sacando puntos...')
    holistic.main(video_n)
    print('Sacando Imagenes...')
    ImVid.main()
    print('Sacando Videos...')
    ImVid.Video_salida(video_n)
    contenido=np.delete(contenido,0)'''









'''path_video='C:/Users/lesli/mediapipe-python/Videos'

contenido = os.listdir(path_video)

os.makedirs(path_video, exist_ok=True)

for n in range(0,len(contenido)):
    video_n=contenido[n]
    procesos = [subprocess.Popen(["python", script]).communicate() for script in scripts_paths]'''


