#here all algorithm comparisons will be made
import time

import BruteForce
import DynamicProgram

#formats the schedule
def pretty_print_schedule(schedule, activities):
    pretty_schedule = ""
    for activity in schedule:
        pretty_schedule += f"\t- {activity} ({activities[activity][0]} hours, £{activities[activity][1]}, enjoyment {activities[activity][2]}) \n"
    return pretty_schedule

def compare(file_name, constraint):
    #runs dynamic programming and gets necessary info for the first info print
    dp_output, activities, constraint_info = run_dp(file_name, constraint)
    bf_output = run_bf(file_name, activities, constraint)


    start_output = starter_info(file_name, constraint_info)

    print(start_output)
    print(bf_output)
    print(dp_output)
    

#this is for running brute force
def run_bf(file_name, activities, constraint):
    
    start = time.perf_counter()
    bf_schedule, bf_time, bf_cost, bf_enjoyment = BruteForce.main(file_name, constraint)
    end = time.perf_counter()
    bf_runtime = end - start

    bf_pretty_schedule = pretty_print_schedule(bf_schedule, activities)

    #just run to get necessary info (doesn't affect timings on brute force so its fine to run here)
    dp_schedule, dp_time, dp_cost, dp_enjoyment, constraint_info, activities = DynamicProgram.main(file_name, constraint)

        #add extra info based on constraint 
    addon_info_time = ""
    addon_info_cost = ""
    if constraint_info[2] == "Time":
        addon_info_time = f"| Against constraint of {constraint_info[0]} hours"
    else:
        addon_info_cost = f"| Against constraint of £{constraint_info[1]}"

    output = f"""
    --- BRUTE FORCE ALGORITHM ---

    Selected Activities:
    {bf_pretty_schedule}

    Total Enjoyment: {bf_enjoyment}
    Total Time Used: {bf_time} {addon_info_time}
    Total Cost: £{bf_cost} {addon_info_cost}

    Execution Time: {bf_runtime} seconds 
    """
    return output

#this is for running dynamic programming 
def run_dp(file_name, constraint):

    start = time.perf_counter()
    dp_schedule, dp_time, dp_cost, dp_enjoyment, constraint_info, activities = DynamicProgram.main(file_name, constraint)
    end = time.perf_counter()
    dp_runtime = end - start

    dp_pretty_schedule = pretty_print_schedule(dp_schedule, activities)

    #add extra info based on constraint 
    addon_info_time = ""
    addon_info_cost = ""
    if constraint_info[2] == "Time":
        addon_info_time = f"| Against constraint of {constraint_info[0]} hours"
    else:
        addon_info_cost = f"| Against constraint of £{constraint_info[1]}"

    output = f"""
    --- DYNAMIC PROGRAMMING ALGORITHM ---

    Selected Activities:
    {dp_pretty_schedule}

    Total Enjoyment: {dp_enjoyment}
    Total Time Used: {dp_time} {addon_info_time}
    Total Cost: £{dp_cost} {addon_info_cost}

    Execution Time: {dp_runtime} seconds
    """
    return output, activities, constraint_info

#for preliminary starter info - modularised so its printing can be more flexible
def starter_info(file_name, constraint_info):
    output = f"""
    ========================================
    EVENT PLANNER - RESULTS
    ========================================

    Input File: {file_name}
    Available Time: {constraint_info[0]}
    Available Budget: £{constraint_info[1]}

    Using constraint: {constraint_info[2]}
    """
    return output

#main program entering into loop waiting for user input

def main():
    running = True
    constraints = ["Cost", "Time"]
    inputs = ["input_small.txt", "input_medium.txt","input_large.txt", "input_1000.txt"]
    print(" ")
    print("Welcome to the Event Planner, here you can run a brute force and dynamic algorithm to find the best schedule within a given constraint!")
    while running:
        
        print("\nWhich input file would you like to use for computing?")
        print(f"Available files {inputs}")

        #enter a loop until valid file given
        looping = True
        while looping:
            input_file = input("Enter:")
            if input_file not in inputs:
                print("Invalid file")
            else:
                looping = False

        print("Pick a constraint: Cost or Time")
        looping = True
        while looping:
            constraint = input("Enter:")
            if constraint not in constraints:
                print("Invalid constraint")
            else:
                looping = False
        
        print("\nWould you like to run the brute force, dynamic approach or both?")
        choice = input("Enter:")

        dp_schedule, dp_time, dp_cost, dp_enjoyment, constraint_info, activities = DynamicProgram.main(input_file, constraint)

        if choice in ["bf", "Brute Force", "brute", "brute force", "b"]:
            start_output = starter_info(input_file, constraint_info)
            bf_output = run_bf(input_file, activities, constraint)
            print(start_output)
            print(bf_output)
        elif choice in ["dp", "dynamic", "dynamic approach", "dynamic program", "d", "Dynamic Program", "Dynamic Approach"]:
            start_output = starter_info(input_file, constraint_info)
            run_dp(input_file, constraint)
            print(start_output)
        else:
            compare(input_file, constraint)
        

main()