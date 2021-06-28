## TODO:
### - add calandar habit time slot at the end, after workout. 


'''
-------------------------------------TEST MODE-------------------------------------
'''
# this just speeds routine up so you dont have to wait through bullshit

TEST = True

# normal conditions
WT            = 1   # normal default param should be 1 second
SIXTY_SECONDS = 60    # normal defalut should be 60 

if TEST == True:
    WT            = 0.1   # normal default param should be 180 (seconds OR 3 minutes) this is for making bed and coffee and breath work 
    SIXTY_SECONDS = 1   # normal defalut should be 60 
'''
-------------------------------------TEST MODE-------------------------------------
'''


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
import Routine_config
from pydub import AudioSegment
from pydub.playback import play



sound = AudioSegment.from_mp3('soothing alarm.mp3')



#Establish Paths and THE_MOMENT
now       = datetime.now() 
rpath     = 'Routines/'
save_name = rpath+'#Routine_Log.csv'




print("                        ==Brandons==                       ")

print(" ____             _   _                _           __      ")
print("|  _ \ ___  _   _| |_(_)_ __   ___    | |   _   _ / _| ___ ")
print("| |_) / _ \| | | | __| | '_ \ / _ \   | |  | | | | |_ / _ \ ")
print("|  _ < (_) | |_| | |_| | | | |  __/   | |__| |_| |  _|  __/")
print("|_| \_\___/ \__,_|\__|_|_| |_|\___|___|_____\__, |_|  \___|")
print("                                 |_____|    |___/          ")
print('-------------------------#GoodLifeApp------------------------')




'''
ROUTINE TASK FUNCTIONS >>------>
     - and so marks the begining of keeping custom task_functions in a dictionary , 
'''



def arbitrary_function():
    for i in range(5):
        print('dookie dookie dookie dookie dookie dookie dookie dookie')

def meditate(test=False,thing=True):
    
    os.system('figlet ==Meditation==')

    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('')
    print(' =============Welcome! you are doing this!=============')
    print('      - you will gain full control of your emotions')
    print('      - learn to live in the peace that surpasses all understanding')
    print('      - grow grey matter in your brain')
    print('      - gain full control over your ADHD')
    print('      - grow in self control...')
    print(' - i want to get 30 full days of doing 20 minutes before advancing ')
    print(' - sit up in a downhill posture')
    print(' - no distractions , no vape ')

    print('')
    input('are you ready')
    
    #time_limit = meditation_schedule_df.iloc[days_on_so_far]

    def play_playlist():
        playlist   = '/home/brando/Downloads/Holosync/Holosync-Awakening_Level_2/step_one.xspf'
        os.system(f'vlc {playlist}')


    minute     = 60
    if test == True:
        minute = 1
    time_limit = 20 * minute
    

    def count_down():
        
        
        
        # SO HERE YOU CHECK IF THERE IS A SCHEDULE SHEET 
        #     - check if there is a log
        #     - if so then you pull time limit from schedule
        #          - based on how many days in a row you have
        #     - update a log 


        for s in trange(time_limit):
            time.sleep(1)
        play(sound)

    if (__name__ == "__main__") and (thing == True):
        # creating thread
        t1 = threading.Thread(target=count_down)#, args=(0,))
        t2 = threading.Thread(target=play_playlist)#, args=(0,))

        # starting thread 1
        t1.start()
        # starting thread 2
        t2.start()

        # wait until thread 1 is completely executed
        t1.join()
        # wait until thread 2 is completely executed
        t2.join()

        # both threads completely executed
        print("Done!")
    

    med_log_dic = {
        'Date' : str(datetime.now()).split('.')[0],
        'time' : time_limit,
        'log'  : str(input('is there anything you want to jot down ?:'))
    }

    

    # NOW UPDATE A LOG WITH SCHEDULE
    ml_path = 'habit_data/meditation_log.txt'

    with open(ml_path,'a') as f:
        f.write(str(med_log_dic)+'\n')






task_functions = { 
                'meditate'           : meditate,
                'arbitrary_function' : arbitrary_function
} 


print(task_functions)









'''
     >>--------------------------------------------->
'''

def say(text):
    engine.say(text)
    engine.runAndWait()



def gratitude(Routine_config):
    #THANKFUL PART
    thankful_things = []
    how_much_grat   = Routine_config.how_much_thankful
    for i in range(how_much_grat):
        thing = input('write {} thing your thankful for:'.format(str(i+1)))
        thankful_things.append(thing)
    return thankful_things

#print(thankful_things)

#Load Last Archived Routine 
if os.path.exists(save_name):
    cnt_df      = pd.read_csv(save_name).set_index('Date')
    cnt_df.index= pd.to_datetime(cnt_df.index)
    dayz_n_row  = cnt_df['Days_in_row'][-1] 
    last_run    = cnt_df.index[-1]
    run_delta   = now - last_run
    one_day_delt= run_delta < pd.Timedelta(days=2)

    
    print('last_run:',last_run) 
    print('run_delta:',run_delta) 
    print(' ')
    
    # IF YOUR STILL ON A ROLL REMINDS YOU : YOUR STILL ON A ROLL!!
    if one_day_delt == True:
        today_count = dayz_n_row + 1
        print('---==WELCOME BACK==---')
        print('YOU HAD {} DAYS IN A ROW!'.format(dayz_n_row))
        print('')
        print('TODAY WILL BE {}!!'.format(today_count))
        
    else:
        print('good job. get back on that horse and rise into the sun')
        today_count = 0 

os.system('figlet DAYS_N_ROW:')
os.system('figlet + ==[ {} ]== +'.format(dayz_n_row))
print('')
print('~~~~~~~~~~~~~~~~~~~~~~~~ HISCORE:',cnt_df['Days_in_row'].max(),'~~~~~~~~~~~~~~~~~~~~~~~~')
print('')



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


def show_all():
    rpath = 'Routines/'
    sheets= [s for s in os.listdir(rpath) if '#' not in s]
    [print('==============================================\n',sheet,'=====\n',pd.read_csv(rpath+sheet)) for sheet in sheets]


def select_routine():
    rpath    = 'Routines/'
    routines = os.listdir(rpath)
    routines = [i for i in routines if '#' not in i]
    #i want to know how long each routine is.

    times = [pd.read_csv(rpath+routine)['TIME_LIMIT'].sum() for routine in routines]


    rdf      = pd.DataFrame(routines,columns=['Routine'])

    rdf['TimeLimit'] = times
    rdf['Selection'] = rdf.index
    
    
    print('type: [show] to show all the routines')
    
    which = None
    while type(which) != int:
        print(rdf)

        which = input('which one?')
        if which == 'show':
            show_all()
            which = int(input('which one?'))
        try:
            which = int(which)
        except Exception:
            print('thats not an optio try again')



    print('ROUTINE:........................ ',routines[which])
    routine_path = rpath+routines[which]
    df = pd.read_csv(routine_path)


    now = datetime.now()
    df['ETA'] = pd.Timedelta(minutes=df['TIME_LIMIT'][0]) + now

    for i in range(1,len(df)):
        df['ETA'][i] = pd.Timedelta(minutes=df['TIME_LIMIT'][i]) + df['ETA'][i-1]
        
    time_li = [str(i.time()).split('.')[0] for i in df['ETA'] ]

    df['ETA']       = time_li


    #make it a routine by eliminating the bull
    routine = routine_path.replace(rpath,'').replace('.csv','')

    #print(pd.DataFrame(time_li))
    return df, routine



def pretty_message(title,message=None):
    os.system('figlet {}'.format(title))
    print('=================================================================')
    if message != None:
        print(message)

def read_through(Routine_config):
    '''
    This runs through a list of important things/ mantras / affirmations you want to read in the morning 
    to start your day right.

    they are generate from a spreadsheet titled '#mantras.csv' add or remove any as you like. 

    if you want to skip this step open the file Routine_config.py and change read_mantras to False
    '''
    mantras = 'Routines/#mantras.csv'

    if Routine_config.read_mantras == True:
        print('YES!')
        #cheack if there are mantras
        if os.path.exists(mantras):
            madf = pd.read_csv(mantras)
            if len(madf) > 0:
                montarchive = []
                for i in range(len(madf)):
                    mantrat = madf['title'][i]
                    message = madf['mantra'][i]
                    pretty_message(mantrat,message)
                    #print(mantrat)
                    #print(message) 
                    print('')
                    one_liner = '(' + mantrat + ':' + message + ')'
                    montarchive.append(one_liner)

                    angknolage = input('press enter')
            
                return montarchive

            else:
                print('there are no mantras in sheet')
        else: 
            print('there is no mantra sheet')




# INITIATE PROGRAM
yn = ''
gotta_y = False
while gotta_y == False:

    df,routine = select_routine()
    
    #list things you are thankful for
    thankful_things = gratitude(Routine_config)

    #list of mantras you want to repeate to start the day right!
    montarchive = read_through(Routine_config)
    
    #print(df)
    yn       = 'yup'#str(input('does this look good? type yup:'))

    '''
    ------------------------BREATH PART BEGIN------------------------
    '''

    # BREATHING FIRST  >>----> ======================================================= >>---->  0   ++++++++++++++++++++++++
    play(sound)

    ### space loop - all it doese is make space 
    for i in range(69):
        print('')

    print('before anything count take ten deep breaths .... ')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

    # timmer weight or wait for testing purposes ( because waiting is boring )
    


    #while ('y' not in bth) or ('n'not in bth):
    input('                                ...are you ready?')
    three_mins = 180
    if TEST == True:
        three_mins = 18

    for i in trange(three_mins):
        time.sleep(WT)
    
    print('')
    print('')
    print('')
    feeling_one = input('cool now how do you feel? (just press enter this does nothing) ') 


    ### insert habit log update logic here

    
    habpath = 'habit_data/'
    # Create Directory If It Doesn't Exist
    if not os.path.exists(habpath):
        os.mkdir(habpath)
    
    # Update A Log Of Date Times
    with open(habpath+'breath_before_coffee.txt','a') as f :
        f.write(str(datetime.now())+'\n')


    #  MAKE BED >>----> ======================================================= >>---->  0  ++++++++++++++++++++++++
    #speach engine
    engine.say('Make your bed before drinking coffee')
    engine.runAndWait()




    print('make bed')
    for i in trange(180):
        time.sleep(WT)

    #speach engine
    engine.say('did you do it?')
    engine.runAndWait()

    keep_on = False
    did_it  = False
    while keep_on == False:
        mkbd = str(input('did you make your bed? y/n:')).lower()
        if ('y' in mkbd) or ('y' == mkbd):
            keep_on = True
            did_it  = True  
            print('good job!')
        elif 'n' in mkbd:
            keep_on = True
            print('boo try again')
        else:
            print(' sorry thats not an option:')


    with open(habpath+'make_bed.txt','a') as f:
            
        mkbd_di = str( {'Date':str(datetime.now()),'made_bed':did_it}) + '\n'
        f.write(mkbd_di)
    print(' ')
    print('Cool Habit Jornal Logged')


    # COFFEE PART ()()()()()()()()()()()()()()))())()()()()(()()()()(()()()()()()()(()())()())())()()
    #speach engine
    engine.say('make coffee')
    engine.runAndWait()
    


    
    print('===========')
    print('make coffee')
    print('===========')


    for i in trange(180):
        time.sleep(WT)

    

    # *ding
    #play(sound)
    


    '''
    ---------------------------BREATH BED & COFFEE PART END---------------------------
    '''
    print('press enter to continue')
    input('push any key to continue...')
    pretty_message('One Goal')
    print('====================[to rule them all]====================')
    print('Whats one Goal for today if you could only accomplish one thing?')
    one_goal_for_today  = str(input('Todays Highest Priority:'))





    if yn.lower()=='yup':
        df['STATUS'] = '...'
        gotta_y = True
        for i in trange(len(df)):
            df['STATUS'][i] = 'WORKING'
            task = df['TASK'][i]
            #
            #
            #
            #
            # If The Task Is Not In The Task Dictionary - run timmer and routine as normal 
            if task not in task_functions.keys():
                minute_limit= df['TIME_LIMIT'][i]
                limit       = df['TIME_LIMIT'][i]  * SIXTY_SECONDS
                #play alarm tone
                if TEST == True:
                    print('*dinggggggggggggggggggggggggggggggggggggggggggggggg')
                else:
                    play(sound,)

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
            #
            #
            #
            #
            # IF IT IS THEN YOU GET THE CUSTOM TASK FUNCTION 
            else:
                
                task_functions[task]()  # Just Make A Parameter Dictionary



            df['STATUS'][i] = 'COMPLEATE'

            
print('yey done')

#save the todo list
df['Datetime'] = pd.to_datetime(str(datetime.now()).split('.')[0])
df = df.set_index('Datetime')

'''========================[archivefunction]===================='''

print('BRO DO YOU EVEN LIFT?:')

'''
WORKOUT LOG LOGIC HERE
'''

import workout_input_script



'''
WORKOUT LOG LOGIC OUT!

'''



#SAVE ARCHIVE
path = 'Routines/'
sheet= '#routine_archive.csv'
archive_data(path,sheet,df)


print('')
print('~~~~~~~~~~~~~~~~~~~~~~~~ HISCORE:',cnt_df['Days_in_row'].max(),'~~~~~~~~~~~~~~~~~~~~~~~~')
print('')

os.system('figlet DAYS_N_ROW:')
os.system('figlet + ==[ {} ]== +'.format(today_count))

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n \n \n ')
# SAVE LOG
os.system('figlet Jornal Entry:')
#set values for todays log_entrygit
li = []
di = {}
di['Routine']       = routine
di['Date']          = now.date() 
di['Days_in_row']   = today_count


#INPUTS

di['Goal']              = one_goal_for_today 
di['Goal_Accomplished'] = False
# print most recent jorn entrys:
print(cnt_df['Captains_Log'].tail())

di['Captains_Log']      = str(input('Write a Jornal Entry:'))
di['Thankful_Thing']    = thankful_things
di['Montras']           = montarchive

#Transformation into Data Frame
li.append(di)
df = pd.DataFrame(li).set_index('Date')

# Save it...
if not os.path.exists(save_name):
    df.to_csv(save_name)
    print('first_copy saved')
else:
    odf = pd.read_csv(save_name).set_index('Date')

    # adding some accountability to your goals
    if 'Goal' in odf.columns:
        print('yesterdays goal: ',odf['Goal'][-1])
        goal_status    = str(input('did you accomplish this goal?'))
        df['Goal_Accomplished'][-1] = goal_status

    ndf = odf.append(df)
    ndf['Goal_Accomplished'][-1] = goal_status
    ndf.to_csv(save_name)
    print('appended')






# Calandar Portion
os.system('figlet ==Meditation==')

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print('work on calandar:')
say('work on calandar')

cal_path   = 'habit_data/calandar_habit.txt'
time_limit = 180

if test == True:
    time_limit = 1

for s in trange(time_limit):
    time.sleep(1)

if test == False:
    play(sound)

did_cal = False
say('did you update the calandar?')
ync = str(input('did you update calandar y/n?:')).lower()
if ('y' in ync) or ( 'y' == ync):
    did_cal = True

cal_dic = {
    'Date'  : str(datetime.now()).split('.')[0],
    'Did_it': did_cal,
    'goal'  : one_goal_for_today,
    'yester': str(input('did you accomplish yesterdays goal?:'))
    
}
with open(cal_path,'a') as f:
    f.write(str(cal_dic)+'\n')


#AudioSegment.from_mp3('Lagwagon_Lets_Talk_About_Feelings__02__Gun_In_Your_Hand.mp3')





sound = AudioSegment.from_mp3('ALARM_I_BEILIEVE.mp3')
play(sound)
#os.system('play Lagwagon_Lets_Talk_About_Feelings__02__Gun_In_Your_Hand.mp3')


'''



### it iterates between 2 inputs until you type 'done' or 'DONE'

#### > A. a task - str( user input )
#### > B. how many minutes - int( )  you think  

'''