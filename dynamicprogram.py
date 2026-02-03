from pathlib import Path 

 

BASE_DIR = Path(__file__).parent 

 

def load_input(name): 
    # relative file pathing 
    file_path = BASE_DIR / "inputs" / name 
    text = file_path.read_text(encoding="utf-8") 
    # split file input text into lines, remove the last empty line 
    lines = text.split("\n") 
    lines.pop() 
    activities = lines[0] 
    time_budget = lines[1].split(" ") 
    time, budget = time_budget[0], time_budget[1] 
    events = {} 
    # loop through the lines and assemble the dictionary, ignore first two lines and empty last line 
    for i in range(2,len(lines)): 
        line = lines[i].split(" ") 
        data = line[1],line[2],line[3] 
        events[line[0]]=data 
    return activities, time, budget, events 

def score_schedule(schedule): 
    total_time = 0 
    total_cost = 0 
    total_enjoyment = 0 
    no_acts = len(schedule) 
    #catch case where no activities passed in 
    if no_acts == 0: 
        return 0, 0, 0
    #loop through each activity looking up its time, cost and enjoyment value from global table 'activities' 

    for index in range(0, no_acts): 
        curr_act_data = activities[schedule[index]] 
        total_time += int(curr_act_data[0]) 
        total_cost += int(curr_act_data[1]) 
        total_enjoyment += int(curr_act_data[2]) 

    return total_time, total_cost, total_enjoyment 


data = load_input("input_small.txt") 
#lookup table of all activities 
activities = data[3] 



