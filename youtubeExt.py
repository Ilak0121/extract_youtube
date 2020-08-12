from __future__ import unicode_literals
import youtube_dl, sys

class extracter:
    def __init__(self):
        self.ydl_opts_mp3={
                'format':'bestaudio/best',
                'postprocessors':[{
                    'key':'FFmpegExtractAudio',
                    'preferredcodec':'mp3',
                    'preferredquality':'192',
                    }],
                }
        self.ydl_opts_mp4={}

    def getList(self):
        lists=[]
        print("input the links \n *** if you want to stop typing and start to download, push 'ctrl+c'")
        while(1):
            try:
                url=input("url > ")
            except KeyboardInterrupt as e:
                print("\n")
                break
            lists.append(url)
        return lists

    def extract_one(self,link,opt):
        if opt == 'mp3':
            with youtube_dl.YoutubeDL(self.ydl_opts_mp3) as ydl:
                ydl.download(link)
        elif opt == 'mp4':
            with youtube_dl.YoutubeDL(self.ydl_opts_mp4) as ydl:
                ydl.download(link)

    def extract_list(self,lists,opt):
        print("\n*** starting ***\n")
        for link in lists: self.extract_one(link,opt) 

    def Run(self):
        try:
            choice=input("Input the number >> ")
        except (KeyboardInterrupt, EOFError) as e:
            sys.exit(1)

        if choice == '1':
            self.extract_one([input("input the link >> ")],'mp3')
        elif choice == '2':
            lists = self.getList()
            self.extract_list(lists,'mp3')
        elif choice == '3':
            self.extract_one([input("input the link >> ")],'mp4')
        elif choice == '4':
            lists = self.getList()
            self.extract_list(lists,'mp4')

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





