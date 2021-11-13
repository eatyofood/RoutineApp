import time
import pandas as pd
import os
import sqlalchemy as sql
import numpy as np
import random
from datetime import datetime
from tqdm import trange
import pyttsx3 

eng = pyttsx3.Engine()
eng.setProperty('rate',150)

def tag_alongs():
    '''
    updates habit logs on simple one liner questions
    - most are true / false
    '''
    tpath = '/home/brando/habit_data/tag_alongs.csv'
    df    = pd.read_csv(tpath)
    df

    li = []

    for i in range(len(df)):
        habit = df['habit'][i]
        note  = df['Note:'][i]
        tf_a  = df['true_False_answer'][i]
        c_ans = df['complete_answer'][i]
        di = {}
        di['habit'] = habit
        say(habit)
        print(note)
        ans   = input(habit.upper()+'?:').lower()
        if tf_a == True: 
            di['complete'] = False
            if 'y' in ans:
                ans = True
            else:
                ans = False

            if ans == c_ans:
                di['complete'] = True
        else:
            di['answer'] = ans
        habitlog(pd.DataFrame([di]),habit.replace(' ','_'))
        li.append(di)
    
    print(pd.DataFrame(li))


def say(thing):
    os.system(f'figlet {thing}')
    print('---------------------------------------------')
    eng.say(thing)
    eng.runAndWait()

say('day yum  yes')
say('beeotch')


def yn_quest(question):
    print('===============================')
    say(question)
    print('===============================')
    yn = input('Y/N:').lower()
    return yn


def launch_audiobook():
    path = '/home/brando/Downloads/A.New.Earth.2008.eBOOK.and.Mp3-NEUTEK/A_New_Earth-2008-AUDIOBOOK-NEUTEK/'

    files = [f for f in os.listdir(path) if '.mp3' in f]
    dlen  = len(files)
    rand  = random.randint(0,dlen)
    file  = path + files[rand]

    # launch audiobook
    os.system(f'rhythmbox {file}')
    print(file)
    pd.DataFrame(files)


def habitlog(hdf,habit_name):
    '''
    TAKES:
        1)habit dataframe:pd.DataFrame()
        2)habit name     : str
    '''
    table_name = f'{habit_name}_habit'
    addr= 'postgresql://postgres:password@localhost/'
    db  = 'habits'
    eng = sql.create_engine(addr+db)
    con = eng.connect()
    hdf.to_sql(table_name,con,if_exists='append')
    con.close()
    p   = '/home/brando/habit_data/' + habit_name
    with open(f'{p}_lastrun.txt','w') as f:
        f.write(str(datetime.now().date()))
        
    print(f'databaselog:{table_name}\n UPDATED!')

def audio_book_habit():
    di = {}
    # did you youtube?
    di['datetime'] = str(datetime.now()).split('.')[0]
    di['youtube']  = yn_quest('did you youtube yet?')
    # user input
    if  'n' in di['youtube']:
        di['completed'] = True
    else:
        di['completed'] = False

    hdf        = pd.DataFrame([di]).set_index('datetime')
    habit_name = 'AudioBookBeforeYoutube'
    habitlog(hdf,habit_name)

    # do you have an audiobook 
    book    = yn_quest('do you have a book going already?')

    if 'n' in book:
        launch_audiobook()
    print(hdf)

def sleep_jornal(dt):
    #sleep jornal 
    sdi = {}
    sdi['datetime']    = dt
    say('how many hours did you sleep?')
    sdi['hours']       = float(input('HOURS:'))
    say('did you do the bedtime routine?')
    sdi['bed_routine'] = str(input('YN:')).lower()
    say('how did you fall asleep?')
    sdi['how']         = str(input('READING,WATCHING,LAYING:')).lower()
    say('sleep jornal') 
    sdi['jornal']      = str(input('HOW DID YOU SLEEP:'))
    if sdi['hours'] > 0:
        sdi['slept'] = True
    else:
        sdi['slept'] = False

    if  'y' in sdi['bed_routine']:
        sdi['completed'] = True
    else:
        sdi['completed'] = False


    shdf = pd.DataFrame([sdi]).set_index('datetime')
    habitlog(shdf,habit_name)
    print(shdf)
    
    
    
'''
++++++++++++++++++++++++++++++ PRE-SCRIPT ++++++++++++++++++++++++++++++++
'''

say('every action is a vote')
say('for the person you want to be')


dt = str(datetime.now()).split('.')[0]

# MK BED 


def mk_bed(dt):
    # MK BED 
    habit_name      = 'MakeBed'
    bdi             = {}
    bdi['datetime'] = dt
    bdi['complete'] = False


    yn = yn_quest('did you make your bed?')
    if 'y' in yn:
        bdi['complete'] = True
    else:
        yn = yn_quest('can you make your bed?')
        if 'y' in yn:
            # 2 MINUTE TIMMER
            say('2 minutes')
            for i in trange(120):
                time.sleep(1)
            yn = yn_quest('did you make your bed?')
            if 'y' in yn:
                bdi['complete'] = True
    yn = yn_quest('did you make it yesterday?')
    if 'y' in yn:
        bdi['yesterday'] = True

    bhdf = pd.DataFrame([bdi])
    habitlog(bhdf,habit_name)
    

# MAKE BED
habit_name = 'MakeBed'
print('')
print(habit_name)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# check if script ran today yet...
rl = '/home/brando/habit_data/' + habit_name + '_lastrun.txt'
p = '/home/brando/habit_data/' + habit_name
if os.path.exists(rl):
    with open(f'{p}_lastrun.txt','r') as f:
        line = f.readlines()[0]#('str(datetime.now().date())')
    print(line)

    last_run = pd.to_datetime(line)
    if last_run == pd.to_datetime(str(datetime.now().date())):
        print('you already did this part')
    else:
        #run script
        mk_bed(dt)
else:
    mk_bed(dt)


yn = yn_quest('did you coffee yet?')
if 'n' in yn:
    for i in trange(180):
        time.sleep(1)


# SLEEP JORNAL
habit_name = 'SleepJornal'
print('')

print(habit_name)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# check if script ran today yet...
rl = '/home/brando/habit_data/' + habit_name + '_lastrun.txt'
p = '/home/brando/habit_data/' + habit_name
if os.path.exists(rl):
    with open(f'{p}_lastrun.txt','r') as f:
        line = f.readlines()[0]#('str(datetime.now().date())')
    print(line)

    last_run = pd.to_datetime(line)
    if last_run == pd.to_datetime(str(datetime.now().date())):
        print('you already did this part')
    else:
        #run script
        sleep_jornal(dt)
else:
    sleep_jornal(dt)


    


# AUDIOBOOK HABIT
habit_name = 'AudioBookBeforeYoutube'
print('')

print(habit_name)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# check if script ran today yet...
p = '/home/brando/habit_data/' + habit_name
if os.path.exists(p+'_lastrun.txt'):
    with open(f'{p}_lastrun.txt','r') as f:
        line = f.readlines()[0]#('str(datetime.now().date())')
    print(line)

    last_run = pd.to_datetime(line)
    if (last_run == pd.to_datetime(str(datetime.now().date()))):
        print('you already did this part')
    else:
        #run script
        audio_book_habit()
else:
    audio_book_habit()
