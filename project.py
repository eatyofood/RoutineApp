## TODO:
# -while now is less that end time
#     - playsound
# - replace all the all caps variable with a project config file


import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
import playsound
import os
import pretty_errors
from pydub import AudioSegment
from pydub.playback import play
from tqdm import trange
import time
import pyttsx3
import miniaudio
from datetime import datetime




GOAL = str(input('what is your goal for this ProjectBlock?:'))
MUTE = input('mute: do you want binural beats? if not put True:')

# speach engine
engine = pyttsx3.Engine()
engine.setProperty('voice', 'english+f4')
engine.setProperty('rate',150)
engine.say('welcome back Brandon')
engine.runAndWait()


def say(words):
    '''
    says words
    '''

    engine.say(words)
    engine.runAndWait()

def fig(thing):
    os.system('figlet {}'.format(thing))


SOUNDPATH = 'soothing alarm.mp3'
SOUNDPATH = 'Gamma - Alert focus.flac'

#STEP I - initialize, focus, plan schedual
sound = AudioSegment.from_mp3('soothing alarm.mp3')


#things
things = ['meditate','plan','schedual']
#time limit in minutes
limit  = 6 * 60

for thing in things:
    say(thing)
    print('================================================================')
    os.system('figlet {}'.format(thing))
    print('================================================================')

    for i in trange(limit):
        time.sleep(1)
    print('bing!')
    #play(sound)



def half_hour_block(goal):
    stream = miniaudio.stream_file(SOUNDPATH)
    with miniaudio.PlaybackDevice() as device:
        device.start(stream)
        
        #maybe put a while loop here while legnth_of_audio + startime <  endtime
        fig(goal)
        print('================================================================')
        input("Audio file playing in the background. Enter to stop playback: ")

fig('Break it DOWN!!')
print('================================================================')
print('if you were going to set a goal for each half hour what would they be?')
t1 = str(input('whats the 1st checkpoint?:'))
t2 = str(input('whats the 2nd checkpoint?:'))
t3 = str(input('whats the 3d checkpoint?:'))

ts = [t1,t2,t3]
limit = 30*60
if MUTE == True:
    for thing in ts:
        say(thing)
        print('================================================================')
        os.system('figlet {}'.format(thing))
        print('================================================================')

        for i in trange(limit):
            time.sleep(1)
        print('bing!')
else:

    #BOCK I
    half_hour_block(t1)
    #BOCK II
    half_hour_block(t2)
    #BOCK III
    half_hour_block(t3)



#play(sound)

RESULT = str(input('did you finish {}?:'.format(GOAL)))

di = {}
li = []

di['id']      = str(datetime.now())
di['Goal']    = GOAL
di['Result']  = RESULT
di['Breakdn'] = [t1,t2,t3]

li.append(di)
df = pd.DataFrame(li)

PATH = 'ProjectBlockLogs.csv'
if not os.path.exists(PATH):
    df.to_csv(PATH,index=False)
    print('CREATED',PATH)
    print(df)
else:
    odf = pd.read_csv(PATH)
    ndf = odf.append(df)
    ndf.to_csv(PATH,index=False)
    print('APPENDED',PATH)

    print(ndf)

yn = str(input('do you want to update Project Diary?:'))


PD_PATH = '/home/brando/algos/project_diary.ods'


if yn.lower() == 'y':
    os.system('libreoffice {}'.format(PD_PATH))





