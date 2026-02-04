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
    return int(activities), int(time), int(budget), events 

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

def create_matrix():
    matrix = []
    emptyRow = [" "] * (constraint[1]+1)

    emptyRow[0] = 0 #budgets 0 here so always 0
    firstRow = [0] * (constraint[1]+1) #first row has no assigned item so full of 0s

    matrix.append(firstRow)
    for row in range(0, (num_acts)):
        matrix.append(emptyRow)

    return matrix

def parse_matrix(matrix):
    return

def pretty_print(matrix):
    keys = list(activities.keys())
    #top line helping with visuals and labelling
    print(f"{" ":<20} {constraint[0]:<10} {"Enjoyment":<10} {" "}")
    #for each line show the assigned activity except the first which has no activies
    for index in range(0, len(matrix)):
        if index == 0:
            # the <20 ensure neat formatting by creating a 20 character space for reserved for each variable
            print(f"{" ":<20} {"":<10} {" ":<10} {matrix[index]}")
        else:
            curr_act = keys[index-1]
            print(f"{curr_act:<20} {activities[curr_act][0]:<10} {activities[curr_act][constraint[2]]:<10} {matrix[index]}")

#load input file
num_acts, time_allowed, cost_allowed, activities = load_input("input_small.txt") 

#chosen = input("Choose time or cost as a constraint: ")
chosen = "time"
if chosen in ["time", "t", "Time", "T"]:
    constraint = ["Time", time_allowed, 2] #this structure contains the name of the constraint, its value, its index in each activities dictionary
else:
    constraint = ["Cost", cost_allowed, 1]

print("\n" + constraint[0] + " constraint with a maximum of " + str(constraint[1]) + "\n") 

matrix = create_matrix()

pretty_print(matrix)
    


