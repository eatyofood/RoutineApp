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






print('          ____                      ')
print("  _____  | __ ) _ __ __ _ _ __   __| | ___  _ __  ___   _____ ")
print(" |_____| |  _ \| '__/ _` | '_ \ / _` |/ _ \| '_ \/ __| |_____|")
print(" |_____| | |_) | | | (_| | | | | (_| | (_) | | | \__ \ |_____|")
print("         |____/|_|  \__,_|_| |_|\__,_|\___/|_| |_|___/        ")
print("")
print("                             *ultimate*                                ")
print("              ____     _    ____  _   _ ____   ____    ")
print("             / / /    / \  |  _ \| | | |  _ \  \ \ \   ")
print("            / / /    / _ \ | | | | |_| | | | |  \ \ \  ")
print("           / / /    / ___ \| |_| |  _  | |_| |   \ \ \ ")
print("          /_/_/    /_/   \_\____/|_| |_|____/     \_\_\ ")
print("                                                       ")
                      
print(" _     ___ ____ _____    __  __    _    _   _    _    ____ _____ ____  _ ")
print("| |   |_ _/ ___|_   _|  |  \/  |  / \  | \ | |  / \  / ___| ____|  _ \| |")
print("| |    | |\___ \ | |    | |\/| | / _ \ |  \| | / _ \| |  _|  _| | |_) | |")
print("| |___ | | ___) || |    | |  | |/ ___ \| |\  |/ ___ \ |_| | |___|  _ <|_|")
print("|_____|___|____/ |_|____|_|  |_/_/   \_\_| \_/_/   \_\____|_____|_| \_(_)")
print("")
print("=============================================================================")

#print('welcome to the scedualer-- just type\n1.the thing\n2.how many minutes it should take\n then type done')
print("      - CREATE HOURS WORTH OF TODO_LIST TIMMERS IN UNDER A MINUTE! - ")
print("type: ")
print("")
print('1. a task --> enter')
print('2. how many minutes it should take --> enter ')
print('3. ^ rinse & repeate, until [satisfied|overwelmed] ')
print("4. type: done or DONE to start the timmers")

print('')

print("-------------------------------------------------------------------------------")



'''SPEACH TO TEXT ENGINE'''

#INPUTS
voice_id= 11
rate    = 150

#VOICE ENGINE
engine    = pyttsx3.init()
engine.setProperty('voice', 'english+f4')
engine.setProperty("rate",rate)
rate   = engine.getProperty('rate')
#print('rate:',rate)



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



# INITIATE PROGRAM
yn = ''
gotta_y = False
while gotta_y == False:

    df = schedual_loop()
    #print(df)
    yn = 'yup'#str(input('does this look good? type yup:'))
    # VOICE 
    
        
    
    engine.say("shake. and. bake.            bay. bee!")
    engine.runAndWait() 
    if yn.lower()=='yup':
        df['STATUS'] = '...'
        gotta_y = True
        for i in trange(len(df)):
            df['STATUS'][i] = 'WORKING'
            task = df['TASK'][i]
            minute_limit= df['TIME_LIMIT'][i]
            limit       = df['TIME_LIMIT'][i] * 60
            play(sound)
            print(df)
            #speach engine
            engine.say(task)
            engine.runAndWait()
            speak_time(minute_limit)
            print('==========++++++++===========[{}]==========++++++++=========='.format(task))
            #print(task)
            pretty_message(task)
            
            for m in trange(limit):
                time.sleep(1)
            #playsound.playsound('algos/itstime.mp3')
            #os.system('printf\a')
            df['STATUS'][i] = 'COMPLEATE'

            
print('yey done')

#save the todo list
df['Datetime'] = pd.to_datetime(str(datetime.now()).split('.')[0])
df = df.set_index('Datetime')

'''========================[archivefunction]===================='''





#INPUTS
path = 'todo_list_archive/'
sheet= 'todolist_archive.csv'
archive_data(path,sheet,df)


#AudioSegment.from_mp3('Lagwagon_Lets_Talk_About_Feelings__02__Gun_In_Your_Hand.mp3')


sound = AudioSegment.from_mp3('ALARM_I_BEILIEVE.mp3')
play(sound)
#os.system('play Lagwagon_Lets_Talk_About_Feelings__02__Gun_In_Your_Hand.mp3')


'''



### it iterates between 2 inputs until you type 'done' or 'DONE'

#### > A. a task - str( user input )
#### > B. how many minutes - int( )  you think  

'''