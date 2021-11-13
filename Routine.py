import threading

from datetime import datetime
import time
import os
from tqdm import trange
import pandas as pd
import warnings
import playsound
import pandas as pd
from pandas.core.common import SettingWithCopyWarning
import pyttsx3
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
import pretty_errors


from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3('soothing alarm.mp3')

#INPUTS
voice_id= 11
rate    = 150

#VOICE ENGINE
engine    = pyttsx3.init()
engine.setProperty('voice', 'english+f4')
engine.setProperty("rate",rate)
rate   = engine.getProperty('rate')
#print('rate:',rate)

def say(thing):
    os.system(f'figlet {thing}')
    print('-------------------------------------------------------------------------')
    engine.say(thing)
    engine.runAndWait()




TEST  = False

if TEST== True:
    seconds = 1
else:
    seconds = 60

now   = str(datetime.now()).split('.')[0]

print('\n \n \n')
print('      ++++++                   111                  +++++++')

print("                               _.._")
print("                             .'    '.")
print("                            (____/`\ \ ")
print("                           (  |    )  )")
print("                           )  _\  _/  (")
print("                 __..---.(`_.'  ` \    )")
print("                `;-""-._(_( .      `; (")
print("                /       `-`'--'     ; )")
print("               /    /  .    ( .  ,| |(")
print("_.-`'---...__,'    /-,..___.-'--'_| |_)")
print("'-'``'-.._       ,'  |   / .........'")
print("       ___``;--'` ;   |   `-`    _  ")
print("      | __ )  _`_.__.' _ __   __| | ___  _ __  ___ _____ ")              
print("|_____|  _ \| '__/ _` | '_ \ / _` |/ _ \| '_ \/ __|_____|")
print("|_____| |_) | | | (_| | | | | (_| | (_) | | | \__ \_____|")
print("      |____/|_|  \__,_|_| |_|\__,_|\___/|_| |_|___/      ")
print("")
print("                         *sexy*                                ")
os.system('figlet +RoutineAp+')
print('                              42                            ')
print("==========================================================")
time.sleep(3)
print('')
import cuties.II
print("----------------------------------------------------------")



'''SPEACH TO TEXT ENGINE'''



def speak_time(num):
    '''
    this function pronounces minutes for a timed todolist
    '''
    #word = text_number(num)
    text = ' {} minutes'.format(num) 
    engine.say(text)
    engine.runAndWait()



def schedual_loop():
    thing = ""
    thingli = []
    while thing.lower() != 'done':
        shedic= {}
        thing = str(input('TASK:'))
        if thing.lower() != 'done':
            #FIX THIS!

            #OLD--------------------------------------
            #limit                = int(input('TIMELIMIT:'))
            #NEW-----------------------------------------
            limit = None

            while type(limit) != int:
                try:
                    limit = int(input('TIME:'))
                except Exception:
                    print('thats not an int, try again')
            print('YEY!')

            shedic['TASK']       = thing
            shedic['TIME_LIMIT'] = limit
            if len(thingli) > 0:
                df = pd.DataFrame(thingli)
                other_items = df['TIME_LIMIT'].sum()
                total_time_so_far   = limit + other_items
                time_delta           = pd.Timedelta(minutes=total_time_so_far) + datetime.now() 
            else:
                time_delta           = pd.Timedelta(minutes=limit) + datetime.now() 
            shedic['ETA']        = str(time_delta.time()).split('.')[0] 
            thingli.append(shedic)
            df = pd.DataFrame(thingli)
            print(df)
        else:
            shedf = pd.DataFrame(thingli)
            
    return shedf


#ARCHIVE FUNCTION
def archive_data(path,sheet,df):
    '''
    CREATING AND UPDATEING AN ARCHIVE FUNCTION:
    df MUST have a datetimeindex
    TODO: test it!
   
   TAKES: 
    1. path = str: the directory you want to save in (this'll create it if it isnt real yet)
    2. sheet= str: whatever your archive is named, or what you would like to name it
    3. df   = pd.DataFrame: if the archive has not been concived yet this will be the first data in it

    '''
    #standardize the index's ... indi indices ??? indy
    df.index.name = 'Datetime'
    #sort it
    df['index_copy'] = df.index
    df = df.sort_values('index_copy')
    df = df.drop('index_copy',axis=1)

    # SAVING - create dirs if they dont exists

    if not os.path.exists(path):
        os.mkdir(path)
    # if the archive doesnt exist this creates it
    if not os.path.exists(path+sheet):
        df.to_csv(path+sheet)

    df

    #load up old data - drop overlapping rows and update
    oldf = pd.read_csv(path+sheet).set_index('Datetime')
    #most recent date
    last_date = oldf.index[-1]

    #set mask
    print('Last todolist in archive is from:',last_date)
    #filter
    newdf = df[df.index>last_date]

    if len(newdf)>0:
        #filtered new data
        print('Most recent todolists is from:',newdf.index[-1])
        oldf = oldf.append(newdf)
        print('the archive has been updated [o_0]')
        oldf.to_csv(path+sheet)
        print(oldf)
    else:
        print('--there are no new recent headlines to append--')


def pretty_message(title,message=None):
    os.system('figlet {}'.format(title))
    print('=================================================================')
    if message != None:
        print(message)


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XXX -THE MAIN SHOW- XXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def the_main_show():
    # INITIATE PROGRAM
    yn = ''
    gotta_y = False
    while gotta_y == False:

        df = pd.read_csv('todo_list_archive/routine.csv') #schedual_loop()
        #print(df)
        yn = 'yup'#str(input('does this look good? type yup:'))
        # VOICE 
        
            
        
        if yn.lower()=='yup':
            df['STATUS'] = '...'
            gotta_y = True
            for i in trange(len(df)):
                df['STATUS'][i] = 'WORKING'
                task = df['TASK'][i]
                minute_limit= df['TIME_LIMIT'][i]
                limit       = df['TIME_LIMIT'][i] * seconds

                # timmer sound
                if TEST == False:
                    play(sound)
                print(df)
                #speach engine
                engine.say(task)
                engine.runAndWait()
                speak_time(minute_limit)
                print('==========++++++++===========[{}]==========++++++++=========='.format(task))
                #print(task)
                pretty_message(task)
                
                if TEST == False:
                    for m in trange(limit):
                        time.sleep(1) 

                #playsound.playsound('algos/itstime.mp3')
                #os.system('printf\a')
                df['STATUS'][i] = 'COMPLEATE'

                
    print('\nyey done\n')




    #save the todo list
    df['Datetime'] = pd.to_datetime(now)
    df = df.set_index('Datetime')

    '''========================[archivefunction]===================='''





    #INPUTS
    path = 'todo_list_archive/'
    sheet= 'todolist_archive.csv'
    archive_data(path,sheet,df)



    # ROUTINE ARCHIVE INPUTS
    rpath          = 'todo_list_archive/routine_archive.csv'
    di             = {}
    di['datetime'] = now
    workout        = input('WORKOUT TYPE ( CC,WC,WU,FL,BN):')
    di[workout]    = input('REPS                          :')
    di['jornal']   = input('JORNAL ENTRY                  :')
    di['day_count']= 1
    di['dayzNrow'] = 1
    if os.path.exists(rpath):
        ordf            = pd.read_csv(rpath).set_index('datetime')
        ordf.index      = pd.to_datetime(ordf.index)
        di['day_count'] = ordf['day_count'][-1] + 1 

        if (datetime.now() - ordf.index[-1]) < pd.Timedelta(days=2):
            di['dayzNrow'] = ordf['dayzNrow'][-1] + 1  
        daycount = str(di['day_count'])
        dayznrow = str(di['dayzNrow'])

        os.system(f'figlet DAYCOUNT___:{daycount}')
        os.system(f'figlet DAYZ_n_ROW:{dayznrow}')
        print(ordf)

    # SAVE ROUTINE ARCHIVE 
    rdf    = pd.DataFrame([di]).set_index('datetime')

    if not os.path.exists(rpath):
        rdf.to_csv(rpath)
    else:
        ordf = pd.read_csv(rpath).set_index('datetime')
        nrdf = ordf.append(rdf)
        nrdf.to_csv(rpath)

def play_sound():
    '''
    plays meditation soundtracks
    (binural beats)
    TODO: give this imputs from a config file

    '''
    soundpath='sounds/meditation_tracks/'
    dili = os.listdir(soundpath)
    print(dili)
    sound = AudioSegment.from_file(soundpath+dili[1])

    play(sound)

from random import randint 

def play_random_sound():
    ''''
    plays a random selection from the music/audiobooks in the directory:
        sounds/music_n_audio_books/ 

    add what you want to listen to here
    '''
    soundpath = 'sounds/music_n_audio_books/'
    dili = os.listdir(soundpath)
    r    = randint(0,len(dili))
    print(dili)
    audio_file = soundpath + dili[r]
    print('==============================[selected audio]=================================')
    print('lucky_number:',r)
    print('lucky_file  :',audio_file)
    sound = AudioSegment.from_file(audio_file) 
    print('===============================================================================')

    play(sound)

#ACTIVATE 

#if (__name__ == "__main__") :#and (thing == True):
    # creating thread
t1 = threading.Thread(target=the_main_show
)#, args=(0,))
t2 = threading.Thread(target=play_random_sound)#, args=(0,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XXX -PART II - XXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# --- VERY CRUDE WAY TO MAKE IT WORK IN THE NEXT 5MINS ---
# TODO:
# - uncrude this!!


# second part of routine
from cuties.funk import pin_up
def part_II():
    '''
    mean - lean quick & DIRTY routine... 
    '''
    say('Meditation 20min') 
    for i in trange(60*20):

        time.sleep(1)
        pin_up
    say('good job')
    print('')
    time.sleep(2)
    say('priority time')
    say('its time to do')
    say('whatever thing is...')
    say('THE MOST ')
    say('IMPORTANT THING!')

    for i in trange(60*60):
        time.sleep(1)
#if (__name__ == "__main__") :#and (thing == True):
# creating thread
t1 = threading.Thread(target=part_II)#, args=(0,))
t2 = threading.Thread(target=play_sound)#, args=(0,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

#play_sound()

say(

    'are you ready for part 2?'
)
time.sleep(3)
print('\n \n \n \n *excite \n \n \n \n ')

# second part of routine
def part_II():
    '''
    mean - lean quick & DIRTY routine... 
    '''
    say('Meditation 20min') 
    for i in trange(60*20):
        time.sleep(1)
    say('good job')
    print('')
    time.sleep(2)
    say('priority time')
    say('its time to do')
    say('whatever thing is...')
    say('THE MOST ')
    say('IMPORTANT THING!')

    for i in trange(60*60):
        time.sleep(1)

#part_II()

sound = AudioSegment.from_mp3('ALARM_I_BEILIEVE.mp3')
#play(sound)

# The End


