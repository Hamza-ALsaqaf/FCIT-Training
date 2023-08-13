# -*- coding: utf-8 -*-
import yt_dlp as youtube_dl
import threading
import os

class DownloadVideo(threading.Thread):
    def __init__(self,link):
        threading.Thread.__init__(self)
        
        self.link         = link
        self.break_       = False
    
    def run(self):
        video_location=r"C:\\Users\\ypt\\Desktop\\"
        options = {}
        # options["format"]          = "best"
        options["format"]          = "bestvideo[ext=mp4]"
        options["socket_timeout"]  = 10
        options["ignoreerrors"]    = True
        options["nooverwrites"]    = True
        options["continue_dl"]     = True
        # options["outtmpl"]         = os.path.join(video_location,"%(id)s.%(format)s.%(title)s.%(ext)s")
        options["outtmpl"]         = os.path.join(video_location,"%(title)s.%(ext)s")
        options["progress_hooks"]  = []
        options["progress_hooks"].append(self.my_hook)
            
        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([self.link])
        except Exception as e:
            print(e)
    
    def my_hook(self,info):
        if self.break_:
            raise Exception('Canceled!')
        status  = info["status"] 
        if status == 'finished':
            print('finished')
            return 
        elif status == "error":
            print('error')
            return 
        
        _percent_str      = info["_percent_str"]
        _speed_str        = info["_speed_str"]
        _eta_str          = info["_eta_str"]
        filename          = info["filename"]
        tmpfilename       = info["tmpfilename"]
        total_bytes       = info["total_bytes"]
        downloaded_bytes  = info["downloaded_bytes"]
        print("\n*************************************************************")
        print(_percent_str)
        print(_speed_str)
        print(_eta_str)
        print(filename)
        print(tmpfilename)
        print(total_bytes)
        print(downloaded_bytes)
        print("*************************************************************\n")


# download_video = DownloadVideo("https://www.youtube.com/watch?v=vbpGVi7kRR4")
#download_video = DownloadVideo("https://fb.watch/moZ9-Yg726/")
download_video = DownloadVideo("https://www.youtube.com/watch?v=0wVUFtBTBxY&pp=ygUQdmlkZW8gMzAgc2Vjb25kcw%3D%3D")
download_video.start()


