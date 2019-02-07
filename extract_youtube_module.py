from __future__ import unicode_literals
import youtube_dl
import sys

class extracter:
    def __init__(self):
        list_up=[]
        ydl_optsi_mp3={
            'format':'bestaudio/best',
            'postprocessors':[{
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192',
                }],
        }
        ydl_opts_mp4={}

    def extract_single(self,link):
        if(link == '')
            string=input("input the link :")
        else:
            string=link
        with youtube_dl.YoutubeDL(self.ydl_opts_mp3) as ydl:
            ydl.download([string])

    def extract_list(self):
        print("input the links \n *** if you want to stop typing and start to download, push 'ctrl+c'")
        while(1):
            try:
                temp=input("url :")
            except KeyboardInterrupt :
                print("\n")
                break
            self.list_up.append(temp)
        print("*** download will be start with below links***")
        for i in self.list_up:
            print(i)
        print("*** starting ***")

        for i in self.list_up:
            self.extract_single(i)

    def print_menu(self):
        print(" this program is for download youtube mp3 file")
        print("----------------------------------------------")
        print("| 0.To exist this Program                    |")
        print("| 1.Download mp3 with link                   |")
        print("| 2.Download mp4 with link                   |")
        print("| 3.Download mp3 by name                     |")
        print("| 4.Download mp3 with list                   |")
        print("| 5.Download mp4 with list                   |")
        print("----------------------------------------------")
        # soon will be update list comparing before downloaded
        # filesystem update will be



