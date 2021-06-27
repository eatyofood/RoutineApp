# Imoprts
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

import pandas as pd
import numpy as np
import re
import os
from datetime import datetime
import pretty_errors

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

# Load Data Frames
rep_df           = pd.read_csv('habit_data/rep_log.csv').set_index('Date')
rep_df.index = pd.to_datetime(rep_df.index)

total_df     = pd.read_csv('habit_data/total_log.csv').set_index('Date')


# Log Archive Paths 
replog_path = 'habit_data/rep_log.csv'
totlog_path = 'habit_data/total_log.csv'



# Workout Groups
group_id = dict(
    compound_curl ='cc',
    sit_ups       ='su',
    wrist_upsv    ='wu',
    flaps         ='fl',
    bench_press   ='bn',
    wrist_curls   ='wc',
    myweight      = 'myw'
#    left_curl     ='lc',
#    right_curl    ='rc',



)
# Group Id Data Frame
gidf = pd.DataFrame([group_id]).T.rename(columns={0:'abv'}) #group_id.keys())
gidf.index.name = 'muscle_groups' 
gidf = gidf.reset_index()
print(gidf)

# Define Weight Groups
groupone = [
    'cc',
    'bn',
    'wu',
    'wc',

]

grouptwo = [
    'fl'
]



# Extract Weight Group Data And Create Variables 
file = 'habit_data/weight_groupone.txt'
with open(file,'r') as f:
    weight_groupone = int(f.readlines()[0])
    print('weight_groupone:',weight_groupone)
    print('type           :',type(weight_groupone))

file = 'habit_data/weight_grouptwo.txt'
with open(file,'r') as f:
    weight_grouptwo = int(f.readlines()[0])
    print('weight_grouptwo:',weight_grouptwo)
    print('type           :',type(weight_grouptwo))


# Add Weight Group To DataFrame

## -  place holder column
gidf['weight'] = 0

## -  loop to add proper one
for i in range(len(gidf)):
    if gidf['abv'].iloc[i] in groupone:
        gidf['weight'].iloc[i] = weight_groupone
    elif gidf['abv'].iloc[i] in grouptwo:
        gidf['weight'].iloc[i] = weight_grouptwo



gidf['priority:']  = None
gidf['max_reps']   = None
gidf['last_reps:'] = None
gidf['time_delta:']= None
#gidf['delta_int:'] = None






for col in rep_df.columns:
    workout   = col
    last_date = rep_df[col].dropna().index[-1]
    last_reps = rep_df[col].dropna()[-1]

    # TODO : ONLY SHOW DATA WITH THE WEIGHT YOU ARE CURRENTLY ON .
    try:
        time_delta= str(datetime.now().date() - last_date.date()).split(',')[0]
        delta_int = int(time_delta.split(' ')[0])
    except:
        time_delta= '0 days'
        delta_int = 0
    pri_stat = None
    #print('time_delta...........',time_delta) 
    if delta_int < 3:
        pri_stat = '--WAIT--'
    elif (delta_int >= 3) and (delta_int < 5) :
        pri_stat = '-DO IT-' 
    else:
        pri_stat = '-UPDATE!-' 

    for i in range(len(gidf)):
        if gidf['muscle_groups'][i] == workout:
            #gidf['last_date:'][i] = last_date
            gidf['time_delta:'][i]=str(time_delta).split(',')[0]
            #gidf['delta_int:'][i] = delta_int
            gidf['priority:'][i]  = pri_stat
            gidf['last_reps:'][i] = last_reps
            

            print( gidf['abv'][i])
            # Max Reps - have to sort max by weight grouping and make sure its the same weight
            if gidf['abv'][i] in groupone:
                max_reps = rep_df[rep_df['weight_groupone']==weight_groupone][workout].max()
            elif gidf['abv'][i] in grouptwo:
                max_reps = rep_df[rep_df['weight_grouptwo']==weight_grouptwo][workout].max()
            else:
                max_reps  = rep_df[col].max()
            gidf['max_reps'][i]   = max_reps





    print('000000000000000000000000') 
    print('workout:',workout )
    print('last_date:',last_date)
    print('time_delta:',str(time_delta).split(',')[0])
    print('delta_int:', delta_int)
    print('priority:',pri_stat)
    print('last_reps:',last_reps)
    


print('++++++++++++=======================================================++++++++++++')
#print(gidf)



# Get Last Date You Did Each Workout And Add it to the Frame



# SAVE WEIGHT 
# Now i Need To Save weight ( from group ) on workout log


# SAVE TO WORKOUT TOTAL LOG
# need to multiply each group by its weight to 
###  -  AND THEN forward fill any blanks




'''
RETRIVE OTHER USEFULL DATA AND PRINT IT HERE 

'''

# TODO: if not path.exists() create frame

gidf

# This Is The Standarizing Function 

def workout_input():
    '''
    inputs the workout reps you did and returns a standardized dictionary
    OUTPUT:
        dict : of workouts
    '''
    
    user = None
    di   = {}
    di['Date'] = str(datetime.now().date())


    while user != 'done':
        print(gidf)
        print('++++++++++++=======================================================++++++++++++')
        print('- Enter The Index Number or Abriviation of the Workout You Want To Enter')
        print('')
        print(' - Or type "set" to change weight amount(TODO)')
        print('')
        user = str(input('EX:0 or "cc" would be "compound_curl":')).lower()
        if 'done' in user:
            pass
        else:
            try: 
                user = int(user)
                workout = gidf['muscle_groups'][user]
                print('----------')
                print(workout)
                print('----------')
                reps    = int(input('How Many Reps?:'))
                di[workout] = reps
            except:
                try:
                    workout = gidf.set_index('abv')['muscle_groups'][user]
                    print('++++++++++++')
                    print(workout)
                    print('++++++++++++')
                    reps    = int(input('How Many Reps?:'))
                    di[workout] = reps
                except: 
                    print('somthing went wrong thats not an option')
    # Update Frame
    ud_df = pd.DataFrame([di]).set_index('Date')
    print('++++++++++++++[UPDATE FRAME]++++++++++++++')
    print(ud_df)

   
    habpath = 'habit_data/'
    # Create Directory If It Doesn't Exist
    if not os.path.exists(habpath):
        os.mkdir(habpath)
    
    # Update A Log Of Date Times
    with open(habpath+'workout_archive.txt','a') as f :
        f.write(str(di)+'\n')

    
    
    # now i will put this inside of a for loop to update everything
    # and save it all as a list!
    #print(pd.DataFrame([di]))
    
    
    return di,ud_df

'''
INPUT PART

'''
# Output The Update Dictionary And Update Data Frame
wo_dic,ud_df = workout_input()

#
try:
    

    li = []
    with open('habit_data/workout_archive.txt','r') as f:
        for l in f.readlines():
            print()
            li.append(eval(l))        #.replace('\n','').replace('"',''))
    li

    ## Mixed Workout Log
    rep_df.append(pd.DataFrame(li).set_index('Date')).drop_duplicates().to_csv('habit_data/rep_df.csv')
except: 
    print('SOMETHING BROKE!')

# THEN YOU JUST ADDD SOME MORE THINGS DOWN HERE

#print(rep_df)


# get the last time you did that 

# then get the time delta 


#gidf['last_date:'] = None


#print(gidf)


## turn this into a list of dics 
### make that a dataframe
#### and mix the dataframe with gidf... 
#### OR JUST UPDATE GIDF RIGHT HERE!


# Only Update Air Fares New Data
if len(wo_dic.keys()) > 1:
    ud_df['weight_groupone'] = weight_groupone
    ud_df['weight_grouptwo'] = weight_grouptwo

    update_df = rep_df.append(ud_df)
    #print(update_df)
    update_df.to_csv('habit_data/rep_log.csv')








