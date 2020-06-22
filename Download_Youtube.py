from pafy import new
import sys
from colorama import init
from termcolor import colored
from pafy import get_playlist
import os
init()
os.popen('cls')
os.system('cls')


def video():
    URL = input(colored('Enter The URL or ID : ', 'yellow'))
    ob = new(URL)
    srt = ob.streams
    for strem in srt:
        print(strem)
    Qu = input(colored("Choose The Quality Number :", 'white'))
    DL = ob.streams[int(Qu)]
    path = input(colored("Which Path : ", 'cyan'))
    DL.download(path)
    print(colored("Done ...", 'red'))


def audio():
    URL = input(colored('Enter The URL or ID : ', 'yellow'))
    ob = new(URL)
    srt = ob.audiostreams
    for strem in srt:
        print(strem)
    Qu = input(colored("Choose The Quality Number :", 'white'))
    DL = ob.audiostreams[int(Qu)]
    path = input(colored("Which Path : ", 'cyan'))
    DL.download(path)
    print(colored('Done ...', 'red'))


def Play_list():
    URL = input(colored('Enter The URL or ID : ', 'yellow'))
    Path = input(colored("Which Path : ", 'cyan'))
    obj = get_playlist(URL)
    for Video in range(len(obj['items'])):
        dow = obj['items'][Video]['pafy'].getbest()
        dow.download(Path)


print(colored('''
 (                )                  
 )\ ) (  (     ( /(           *   )  
(()/( )\))(   ')\())      ( ` )  /(  
 /(_)|(_)()\ )((_)\ ___   )\ ( )(_)) 
(_))__(())\_)()_((_)___| ((_|_(_())  
 |   \ \((_)/ / \| |  | | | |_   _|  
 | |) \ \/\/ /| .` |  | |_| | | |    
 |___/ \_/\_/ |_|\_|   \___/  |_| v0.1 Mr.Daxe
                                                        
''', 'red'))
print(colored('''
choose :
[1] - Video
[2] - audio
[3] - PlayList  
''', 'white'))
V_A = input("==> :")

if V_A == '1':
    video()

elif V_A == '2':
    audio()

elif V_A == '3':
    Play_list()

else:
    print(colored('Error ..', 'red'))
    sys.exit()
