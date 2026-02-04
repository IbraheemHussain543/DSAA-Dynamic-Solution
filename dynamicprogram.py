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
    #create as many rows as there are activities and an additional one 
    for row in range(0, (num_acts)+ 1):
        matrix.append([0] * (constraint[1]+1)) #created seperately to give each a unique space in memory
    return matrix

def fill_matrix(matrix):
    keys = list(activities.keys())
    rows = len(keys) + 1
    cols = len(matrix[0])

    for row in range(1, rows):
        for col in range(1, cols):
            curr_act = activities[keys[row - 1]]
            cost = int(curr_act[constraint[2]])
            value = int(curr_act[2])
            
            #either dont take this item (use value from row above)
            skip = matrix[row - 1][col]
            
            #or take this item (if it fits)
            if col >= cost:
                #add best from knapsack with the remaining allowance to value
                take = matrix[row - 1][col - cost] + value
            else:
                take = 0
            
            #choose the better option
            matrix[row][col] = max(skip, take)
    return matrix

def extract_solution(matrix):
    optimal_schedule = []
    keys = list(activities.keys())
    rows = len(keys) + 1
    cols = len(matrix[0])

    #start at the last value in the table
    curr_row = rows-1
    curr_col = cols-1

    while curr_row > 0:
        curr_joy = matrix[curr_row][curr_col]
        above_joy = matrix[curr_row-1][curr_col]
        #if theres a change this means the current activity is included in the optimal schedule
        if curr_joy != above_joy:
            optimal_schedule.append(keys[curr_row-1])
            #offset the column we are on by the cost of the activity we just added
            curr_col -= int(activities[keys[curr_row-1]][constraint[2]])
        curr_row -= 1
    return optimal_schedule


#debug function to display tables in a neat fashion, breaks when either rows or columns are too high
def pretty_print(matrix):
    keys = list(activities.keys())
    #top line helping with visuals and labelling
    print(f"{" ":<20} {constraint[0]:<10} {"Enjoyment":<10} {" "}")
    #for each line show the assigned activity except the first which has no activies
    for index in range(0, len(keys) + 1):
        if index == 0:
            #turns all the elements in the array into a long string with each of them having a 4 space block reserved
            row_str = " ".join(f"{cell:<8}" for cell in matrix[index])
            #the <20 ensure neat formatting by creating a 20 character space for reserved for each variable
            print(f"{" ":<20} {"":<10} {" ":<10} {row_str}")
        else:
            #all other activities after row 0 must have an activity on their left with its constraint value and enjoyment displayed
            curr_act = keys[index-1]
            row_str = " ".join(f"{cell:<8}" for cell in matrix[index])
            print(f"{curr_act:<20} {activities[curr_act][constraint[2]]:<10} {activities[curr_act][2]:<10} {row_str}")


        

#load input file
num_acts, time_allowed, cost_allowed, activities = load_input("input_custom_2.txt") 

chosen = input("Choose time or cost as a constraint: ")
if chosen in ["time", "t", "Time", "T"]:
    constraint = ["Time", time_allowed, 0] #this structure contains the name of the constraint, its value, its index in each activities dictionary
else:
    constraint = ["Cost", cost_allowed, 1]

#warning to ensure file is formated correctly
if num_acts != len(activities):
    print("WARNING: File is claiming different number of activities to what was found, are you missing an empty line at the end or is there another formatting issue?")

print("\n" + constraint[0] + " constraint with a maximum of " + str(constraint[1]) + "\n") 

matrix = create_matrix()
filled_matrix = fill_matrix(matrix)

optimal_schedule = extract_solution(matrix)
total_time, total_cost, total_enjoyment = score_schedule(optimal_schedule)
print(f"Best schedule is {optimal_schedule} with enjoyment of {total_enjoyment}, cost of {total_cost} and time of {total_time} \n")
    


