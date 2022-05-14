import vlc
from time import sleep

path1 = "Assets/1.jpg"
path2 = "Assets/1.mp4"


media_player = vlc.MediaPlayer()


def playvid(path,start_time,flag =True):
    play = True
    start_time = start_time*1000
    media = vlc.Media(path)
    media_player.set_media(media)
    media_player.set_fullscreen(True)
    media_player.play()
   

    sleep(.1)
    if flag:
        last_pts =0
        
        media_player.set_time(start_time)

        while play:
            
            media_player.set_fullscreen(True)
                        
            if media_player.get_time() >= media_player.get_length()-1000:
                media_player.stop()
                play = False
            
        



while True:
    playvid(path1,False)
    sleep(3)
    playvid(path2,True,3)
    
    
