# OverView 
this is 3 seperate bash terminal apps i made to orginize my life 

### Schedule App
Behold simple Sraight forward schedule planning in seconds 
- lets me plan my whole day or the next hour in seconds 
- i made this b/c i NEEDED IT. as someone who gets lost perfecting minute details instead of hammering on the bigger picture. 

### Routine App
- gives you a time limit for each task on a routine you set.  
- counts how many days in a row you've done it, total days, days since starting. 
- starts playing with music/ audiobook of your choosing

### Fitness Tracker
- quickly tracks weight lifting progress & plots progress.

 

# Set Up
### Download 
    git clone github.git/eatyofood/RoutineApp 

### Install 
    #go to ap directory
    cd RoutineApp/

    #install requirements
    pip install -r requirements.txt 




### Starting the Schedule App
    # to make a schedule...
    python schedule.py 

#### type in a task & it will ask you how long it should take 
- it'll tell you what time you could expect to be done with task if you start now.
- it keeps looping asking for task's & time limits while adding the last thing to your list until you type "done" or "DONE" 
                        TASK  TIME_LIMIT       ETA
    0  get clothes out of dryer           6  14:24:54
    1          fold the laundry           6  14:32:11
    2             take a shower          12  14:44:46
    TASK:call billy    
    TIME:10

##### Options
    - you can save a list by typing 'save' 
    - load a previsouly saved list by typing 'load'
    - or jump into the routine app by typing 'routine' 
    - 'help' will bring up these instructions

### Routine App 
    - set you routine task's and time limits by editing the csv file 'routine.csv' in 'todo_list_archive' directory 

    - if one of the task's on your routine is 'workout' :
        - it will prompt the fitness tracker 

### Fitness Tracker
    - enter the type of workout you did & how many reps. 
    - add new workouts by typing 'add' 
    - remove old workougs by typeing 'remove'




    

