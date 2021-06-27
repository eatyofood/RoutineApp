# Imoprts
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
import re
from datetime import datetime
import pretty_errors
import pandas as pd
import numpy as np
import os


# Workout Groups
group_id = dict(
    compound_curl ='cc',
    sit_ups       ='su',
    wrist_upsv    ='wu',
    flaps         ='fl',
    bench_press   ='bn',
    wrist_curls   ='wc',
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
file = 'weight_groupone.txt'
with open(file,'r') as f:
    weight_groupone = int(f.readlines()[0])
    print('weight_groupone:',weight_groupone)
    print('type           :',type(weight_groupone))


file = 'weight_grouptwo.txt'
with open(file,'r') as f:
    weight_grouptwo = int(f.readlines()[0])
    print('weight_grouptwo:',weight_grouptwo)
    print('type           :',type(weight_grouptwo))

# Add Weight Group To DataFrame

## place holder column
gidf['weight'] = 0

## loop to add proper one
for i in range(len(gidf)):
    if gidf['abv'].iloc[i] in groupone:
        gidf['weight'].iloc[i] = weight_groupone
    elif gidf['abv'].iloc[i] in grouptwo:
        gidf['weight'].iloc[i] = weight_grouptwo


print('=======================================================')
print(gidf)


