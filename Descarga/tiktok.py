import os
import pandas as pd

from TikTokApi import TikTokApi


if not os.path.exists('Descarga'):
    os.makedirs('Descarga')

train_df=pd.read_csv('tiktoks.csv') 


def main():
    
    print('Iniciando descarga')
    for i in range (0,train_df.shape[0]):
        try:
            video=train_df['url'][i]
            name=train_df['tiktok_id'][i]+str(i)+".mp4"
            name_out="Descarga/"+name
            

            #DESCARGA
            with TikTokApi() as api:
                ID_sc=video.split(sep='/')
                ID_c=ID_sc[5][0:19]
                video = api.video(id=ID_c)

                # Bytes del video de TikTok
                video_data = video.bytes()

                with open(name_out, "wb") as out_file:
                    out_file.write(video_data)
                    print(name_out+' Completo')
            
        except:
            continue         

if __name__ == '__main__':
    main()

