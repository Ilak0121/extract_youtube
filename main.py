import subprocess, sys
import youtubeExt as ye

def install_check(package):
    subprocess.check_call([sys.executable,'-m','pip','install',package,'--upgrade'],stderr=subprocess.STDOUT,stdout=None)

if __name__ == '__main__':
    install_check('youtube-dl')
    Ye = ye.extracter()
    while True:
        Ye.Run()
