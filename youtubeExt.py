from __future__ import unicode_literals
import youtube_dl, sys
import myLogger 

class extracter:
    def __init__(self):
        self.ydl_opts_mp3={
                'format':'bestaudio/best',
                'postprocessors':[{
                    'key':'FFmpegExtractAudio',
                    'preferredcodec':'mp3',
                    'preferredquality':'192',
                    }],
                'logger':myLogger(),
                'progress_hooks':[self.myhook],
                }
        self.ydl_opts_mp4={}
        self.options = {
                "mp3": self.ydl_opts_mp3,
                "mp4": self.ydl_opts_mp4
        }

    def myhook(self, d):
        if d['status'] == 'finished':
            print('Done downloading, now converting...')

    def getList(self):
        lists=[]
        print("input the links \n *** if you want to stop typing and start to download, push 'ctrl+c ***'")
        while(1):
            try:
                url=input("url >> ")
            except KeyboardInterrupt as e:
                print("\n")
                break
            lists.append(url)
        return lists

    def extract (self,link,opt):
        print("\n*** starting ***\n")
        with youtube_dl.YoutubeDL(self.options[opt]) as ydl:
            ydl.download(link)

    def Run(self):
        try:
            choice=input("Input the number >> ")
        except (KeyboardInterrupt, EOFError) as e:
            sys.exit(1)

        if choice == '1':
            self.extract([input("input the link >> ")],'mp3')
        elif choice == '2':
            lists = self.getList()
            self.extract(lists,'mp3')
        elif choice == '3':
            self.extract([input("input the link >> ")],'mp4')
        elif choice == '4':
            lists = self.getList()
            self.extract(lists,'mp4')

    def printMenu(self):
        print()
        print("<< Program to extract mp3/mp4 files from youtube >>")
        print("---------------------------------------------------")
        print("| 1. Download mp3 with link                       |")
        print("| 2. Download mp3 with list                       |")
        print("| 3. Download mp4 with link                       |")
        print("| 4. Download mp4 with list                       |")
        print("---------------------------------------------------")
        print()





