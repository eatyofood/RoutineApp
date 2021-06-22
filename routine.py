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
    WT = 0.01


    #while ('y' not in bth) or ('n'not in bth):
    input('                                ...are you ready?')

    for i in trange(180):
        time.sleep(WT)
    
    print('')
    print('')
    print('')
    input('cool now how do you feel? (just press enter this does nothing) ') 


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




    
    for i in trange(180):
        time.sleep(WT)

    #speach engine
    engine.say('did you do it?')
    engine.runAndWait()

    keep_on = False
    did_it  = False
    while keep_on == False:
        mkbd = str(input('did you make your bed? y/n:')).lower()
        if ('y' in mkbd ):
            keep_on = True
            did_it  = True  

        if 'n' in mkbd:
            keep_on = True
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
    


    

    for i in trange(180):
        time.sleep(WT)

    

    # *ding
    #play(sound)
    


    '''
    ---------------------------BREATH BED & COFFEE PART END---------------------------
    '''




    if yn.lower()=='yup':
        df['STATUS'] = '...'
        gotta_y = True
        for i in trange(len(df)):
            df['STATUS'][i] = 'WORKING'
            task = df['TASK'][i]
            minute_limit= df['TIME_LIMIT'][i]
            limit       = df['TIME_LIMIT'][i]  #* 60
            #play alarm tone
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


#di['Workout_Log']       = 
di['Goal']              = str(input('whats one goal for today?'))
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



#AudioSegment.from_mp3('Lagwagon_Lets_Talk_About_Feelings__02__Gun_In_Your_Hand.mp3')


sound = AudioSegment.from_mp3('ALARM_I_BEILIEVE.mp3')
play(sound)
#os.system('play Lagwagon_Lets_Talk_About_Feelings__02__Gun_In_Your_Hand.mp3')


'''



### it iterates between 2 inputs until you type 'done' or 'DONE'

#### > A. a task - str( user input )
#### > B. how many minutes - int( )  you think  

'''