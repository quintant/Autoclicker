from pynput import keyboard
from pynput.mouse import Button, Controller
import threading
import time
import os
os.system('mode con: cols=120 lines=51')
os.system('cls')

mouse = Controller()

print('''::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::!%&$%%%%*::::$&#BBBBBBBBBBS#&%::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::@BBB#&&&&&&&&&BBBBBB&&&&&&&&&&&&&&##BBB$::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::BB#&&&&&&&&&&&&&&&&B&&&&&&&&&&&&&&&&&&&&&BB&::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::BB&&&&&&&&&&&&&&&&&&&&BS&&&&&&&&&&&&&&&&&&&&#B&:::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::@B&&&&&&&&&&&&&&&&&&&&&&&B#&&&&&&&&&&&&&&&&&&&&&BB::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::*B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#B&:::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::BB&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B&%:::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::@BB&&&&&&&&&&&&#BB###SBBBB#&&&&&&&&&&&&&#BB#&&&&SBBBBBBBBBBBBB::::::::::::::::::::::::::::::::::::::::::::::::
::::::BBBSBB&&&&&&&&B&&&&&&&&&&#BBBBBBBBBBB&&&&BBSBBBBB&&&&&&&&&&&&&&&&&&BBB!:::::::::::::::::::::::::::::::::::::::::::
::::&B#&&&&&&&&&&&#&&&&&&&BBBBB#&&&&&&&&#BBSBBBBB#&&&&&&&&&&&&&&&&&&&&&&SBBBBB!:::::::::::::::::::::::::::::::::::::::::
:::@B&&&&&&&&&&&&&&&&&&BB#&&&&&&&&&&&&&&&&&&BB&B&&&&&&&&&&&&#&&&#BBB#SBBBBBBBBBS::::::::::::::::::::::::::::::::::::::::
::%B&&&&&&&&&&&&&&&&&&S&&&&&&&&&&&&&&&&&&SSSBBB&&&&&&&&&B#&BB#&&BBBBSSBB&#BBBSB&BB::::::::::::::::::::::::::::::::::::::
:%B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBBBB#&&&&&&&&&BBBS&&&&&&#BBB&&&SBBBBBBB&&@#SB&&#B%:::::::::::::::::::::::::::::::::::::
#B&&&&&&&&&&&&&&&&&&&&&&&&SBBBB&&&&&&BBBBBBBSSSB&#S&&&&&&&&#BBBBBBBBBBBBBBBB!!S!B&@:::::::::::::::::::::::::::::::::::::
B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBBBBBBBBBBB&&&&&&&&&&&&&BBBB#BBB!$BB#.BBBB::::::BB::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&BBBBBBBBBBBB!*BBB#:::::@@@BS%:::::BBBBBBB..:BBBB::::::BB:::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&BBBBBBBB&&&&BBBBBBB$..&BBB!:::::::::B:::::BBBBBBBBBBBBBB:::::%B::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&BS&&&&&&&BS:::BBBBBBBBBBBBBB::::::::::::::::BB!..&SBBBBBS::::SB#::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&BB&&&&*B::::::BBBBBBBBBBBBBB::::::#::%BBBSB&::$BBBBBBBBB::::BB@:::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&SBB$:::::BBBB%#%..$BBB&:::::::$BBBS&&&#BBBBB:::::::BBBB%:::::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&B&B!:::SBBBBBBBBBB@::::S#BBB&BS&&&&&&&&&BBBBBBBB#&BB::::::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BB@:::::::::::@BSBBS&#BB#&&&&&&&&&&&&&&&&&&BB@:::::::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&SBBBBBBBBBBB&#BBBBS&&&&&#BBS&&&&&&&&BBBB&BBB::::::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBBBBBBBBBB##&&&&&&&&&&&&&&&&&&#BBBBB&&&&&&&&&BB:::::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BB&&&&&&&&&&&&&&&&&&&&S&&&&&&&&&&&BB::::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBB&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BB:::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBBS&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BSB::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B&:::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBBBBB*:::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#SBBBBS####SB:::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBBBBBBBBBBBBBBBBBBBBBBS############B:::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BBBBBBBSS###############################BBB:::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBBBS##########BBBBBBBBBBBBBBS###########BBBBB:::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BS###BBBBBBBBBBBBBBBSSSSSSSSSSBBBBBBBBBBBBBB#B::::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBB#########################################BBB::::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBB###############SBBBBS#################BBBB::::::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&B&&&&&&BBBBBBBBBBBBBBBBBBBB&&&&&&&SBBBBBBBBBBBBB#::::::::::::::::::::::::::::::::::::::::::::
&&&&&&&&&&&&&&&&&&&&&&&&&&&&B&&&&&&&&#S#SS&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B::::::::::::::::::::::::::::::::::::::::::::::
BB&&&&&&&&&&&&&&&&&&&&&&&&&&&BB&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B@::::::::::::::::::::::::::::::::::::::::::::::
&&BB#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&SB#::::::::::::::::::::::::::::::::::::::::::::::::
&&&&BBB&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BB#::::::::::::::::::::::::::::::::::::::::::::::::::
BB&&&&#BBB#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&SBBBBB::::::::::::::::::::::::::::::::::::::::::::::::::::::
BBBB&&&&&&BBBBB&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BB&SBBBBBB::::::::::::::::::::::::::::::::::::::::::::::::::::::::
SSBBBB&&&&&&&&&&BBBBBB#&&&&&&&&&&&&&&&&##BBBBBBBBBBBBBBS&&SBBBBB$:::::::::::::::::::::::::::::::::::::::::::::::::::::::
SSSSSBBBB#&&&&&&&&&&&&#SS##BBBBBBBBBBBBBS&&&&&&&&&&&&&SSBBBSSSSBBB::::::::::::::::::::::::::::::::::::::::::::::::::::::
SSSSSSSSSBBBBBBBB#&&&&&&&&&&&&&&&&&&&&&&&&&&BBBBBBBBBBSSSSSSSSSSSSBBB!::::::::::::::::::::::::::::::::::::::::::::::::::
SSSSSSSSSSSSSSSBBBBBBBBBBBBBBBBBBBBBBBBBBBBBSSSSSSSSSSSSSSSSSSSSSSSSSBB:::::::::::::::::::::::::::::::::::::::::::::::::
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSBB::::::::::::::::::::::::::::::::::::::::::::::
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSBB::::::::::::::::::::::::::::::::::::::::::::
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSBS::::::::::::::::::::::::::::::::::::::::::
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSBBB:::::::::::::::::::::::::::::::::::::::::
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSBSBB*:::::::::::::::::::::::::::::::::::::::''')




def clicker():
    global y
    while 1:
        time.sleep(0.05)
        if y:
            mouse.press(Button.left)
            mouse.release(Button.left)


y = False
x = threading.Thread(target=clicker, daemon=True)

x.start()


def on_press(key):
    global y

    if key == keyboard.Key.page_down:
        y = True


def on_release(key):
    global y
    if key == keyboard.Key.page_down:
        y = False

    if key == keyboard.Key.page_up:
        return False


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
