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

def check_schedule(schedule, max_score, best_schedule, allowed_time, allowed_cost): 
    time, cost, enjoyment = score_schedule(schedule) 
    #check if schedule has highest happieness so far 
    if enjoyment > max_score: 

        #ensure the schedule follows selected constraint and if so make it new best schedule 
        if constraint == "time": 
            if time <= allowed_time: 
                best_schedule = schedule 
                max_score = enjoyment 

        elif constraint == "cost": 
            if cost <= allowed_cost: 
                best_schedule = schedule 
                max_score = enjoyment 

        else: 
            if (time <= allowed_time) and (cost <= allowed_cost): 
                best_schedule = schedule 
                max_score = enjoyment 

    return max_score, best_schedule


def power_set(list): 
    #define constraints and placeholders for best schedule
    allowed_time = int(data[1]) 
    allowed_cost = int(data[2])   
    max_score = 0 
    best_schedule = [] 

    result = [[]] 

    #generate each subset and check it against the current best enjoyment one
    for i in list: 
        subsets = [] 
        for subset in result: 
            subset = subset + [i] 
            subsets.append(subset) 

            max_score, best_schedule = check_schedule(subset, max_score, best_schedule, allowed_time, allowed_cost)

        result.extend(subsets) 

    return best_schedule

def main(file_name, picked_constraint):
    global data, activities, constraint
    data = load_input(file_name) 
    constraint = picked_constraint
    #lookup table of all activities 
    activities = data[3] 
    #generate powersets from the activities and check values for best one 
    best_schedule = power_set(activities) 

    #final results from brute force check     
    time, cost, enjoyment = score_schedule(best_schedule) 

    return best_schedule, time, cost, enjoyment
