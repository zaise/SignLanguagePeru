from pytube import YouTube
import os
from moviepy.editor import *
import shutil
import pandas as pd


if not os.path.exists('Descarga'):
    os.makedirs('Descarga')

if not os.path.exists('TEMP'):    
    os.makedirs('TEMP')   

train_df=pd.read_csv('train.csv') 
train_df['url']='https://www.youtube.com/watch?v='+train_df['youtube_id']

def main():
    #for i in range (0,100):
    for i in range (0,train_df.shape[0]):
        try:
            video=train_df['url'][i]
            name=train_df['label'][i]+str(i)+".mp4"
            
            #####################
            #DESCARGA
            YouTube(video).streams.get_highest_resolution().download(filename = name,output_path = 'TEMP/')
            ######################
            
            name_mid="TEMP/"+name
            name_out="Descarga/"+name

            #(name_mid, train_df['time_start'][i],train_df['time_end'][i], targetname=name_out)
            #CORTAR VIDEOS
            video_ = VideoFileClip(name_mid).subclip(train_df['time_start'][i],train_df['time_end'][i])
            video_.write_videofile(name_out,audio=False)
            video_.close()
            ###################
            
        except:
            continue    
        
        shutil.rmtree("TEMP/")#Quitar para tener los videos originales
     

if __name__ == '__main__':
    main()

    

'''    for i in range (3,5):
        try:
            name=train_df['label'][i]+str(i)+".mp4"
            name_mid="TEMP/"+name
            name_out="Descarga/"+name
            video = VideoFileClip(name_mid).subclip(train_df['time_start'][i],train_df['time_end'][i])
            #video.write_videofile(name_out)    
            video.to_videofile(name_out, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
            
        except:
            continue   '''