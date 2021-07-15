from pynput.mouse import Listener
from multiprocessing import Process
from playsound import playsound
from os import listdir
from random import choice
from time import sleep
sounds=[f'Noises\\{i}' for i in listdir('Noises')]
def moved(_,__):
    global player
    if not player.is_alive():
        new_player=Process(target=play_sound)
        new_player.start()
        player=new_player
def play_sound():
    playsound(choice(sounds))
    sleep(20.0)
if __name__=='__main__':
    player=Process(target=play_sound)
    with Listener(on_move=moved) as listener:
        listener.join()
