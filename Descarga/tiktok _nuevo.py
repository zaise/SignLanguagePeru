import os
import pandas as pd
import shutil
from moviepy.editor import *

from TikTokApi import TikTokApi


if not os.path.exists('Descarga'):
    os.makedirs('Descarga')

train_df=pd.read_csv('tiktoks.csv') 


def main():

    print('Iniciando descarga')
    
    for i in range (0,train_df.shape[0]):

        if not os.path.exists('TEMP'):
            os.makedirs('TEMP')

        try:
            video=train_df['url'][i]
            name=train_df['tiktok_id'][i]+'_'+str(i)+".mp4"
            name_mid="TEMP/"+name
            name_out="Descarga/"+name
            
            
            if train_df['cortar'][i]=="si":
            #DESCARGA
                descarga(name_mid,video)
            #CORTAR
                video_ = VideoFileClip(name_mid).subclip(train_df['ti'][i],train_df['tf'][i])
                video_.write_videofile(name_out,audio=False)#Para descargar con audio quitar audio=False
                video_.close()

            if train_df['cortar'][i]=="no":
            #DESCARGA
                descarga(name_out,video)                    
            
        except:
            continue    

        shutil.rmtree("TEMP/")#Quitar para tener los videos originales


def descarga(name,video):

    with TikTokApi() as api:
        ID_sc=video.split(sep='/')
        ID_c=ID_sc[5][0:19]
        video = api.video(id=ID_c)

        # Bytes del video de TikTok
        video_data = video.bytes()

        with open(name, "wb") as out_file:
            out_file.write(video_data)
            print(name+' Completo')


if __name__ == '__main__':
    main()