from __future__ import unicode_literals
import youtube_dl
import sys

def first(s) :
    ydl_opts ={
        'format':'bestaudio/best',
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
            }],
    }
    if(s==''):
        string=input(" Input the link :")
    else:
        string=s
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([string])

def second(s) :
    ydl_opts = {}
    if(s==''):
        string=input("Input the link :")
    else:
        string=s
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([string])

def third() :
    print("this function is still developing use another option")
    print("seo jung uk babo")
   
def fourth() :
    a=[]
    b=""
    print("input the lists and if you want to finish input 'ctrl+c'")
    while(1):
        try:
            b=input("url : ")
        except KeyboardInterrupt :
            print("\n")
            break
        a.append(b)
    for i in a:
        first(i)

def fifth() :
    a=[]
    b=""
    print("input the lists and if you want to finish input 'ctrl+c'")
    while(1):
        try:
            b=input("url : ")
        except KeyboardInterrupt :
            print("\n")
            break
        a.append(b)
    for i in a:
        second(i)
       

def main():
    print(" this program is for download youtube mp3 file")
    print("----------------------------------------------")
    print("| 0.To exist this Program                    |")
    print("| 1.Download mp3 with link                   |")
    print("| 2.Download mp4 with link                   |")
    print("| 3.Download mp3 by name                     |")
    print("| 4.Download mp3 with list                   |")
    print("| 5.Download mp4 with list                   |")
    print("----------------------------------------------")
    try:
        choice=input(" Input the number :")
    except KeyboardInterrupt :
        sys.exit(1)
    if choice == "1" :
        first('')
    elif choice == "2":
        second('')
    elif choice == '3':
        third()
    elif choice == '4':
        fourth()
    elif choice == '5':
        fifth()
    else :
        sys.exit(1)
   
while(1):
    main()


