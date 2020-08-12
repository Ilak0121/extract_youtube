import subprocess, sys

def install_check(package):
    subprocess.check_call([sys.executable,'-m','pip','install',package,'--upgrade'],stderr=subprocess.STDOUT,stdout=None)

if __name__ == '__main__':
    install_check('youtube-dl')
    import youtubeExt as ye
    Ye = ye.extracter()
    while(1):
        Ye.printMenu()
        Ye.Run()
