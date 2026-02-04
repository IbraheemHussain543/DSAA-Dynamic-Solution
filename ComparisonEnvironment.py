#here all algorithm comparisons will be made
import time

import BruteForce
import DynamicProgram

def pretty_print_schedule(schedule, activities):
    pretty_schedule = ""
    for activity in schedule:
        pretty_schedule += f"\t- {activity} ({activities[activity][0]} hours, £{activities[activity][1]}, enjoyment {activities[activity][2]}) \n"
    return pretty_schedule

def compare(file_name, constraint):
    start = time.perf_counter()
    bf_schedule, bf_time, bf_cost, bf_enjoyment = BruteForce.main(file_name, constraint)
    end = time.perf_counter()
    bf_runtime = end - start

    start = time.perf_counter()
    dp_schedule, dp_time, dp_cost, dp_enjoyment, constraint_info, activities = DynamicProgram.main(file_name, constraint)
    end = time.perf_counter()
    dp_runtime = end - start

    bf_pretty_schedule = pretty_print_schedule(bf_schedule, activities)
    dp_pretty_schedule = pretty_print_schedule(dp_schedule, activities)

    #add extra info based on constraint 
    addon_info_time = ""
    addon_info_cost = ""
    if constraint_info[2] == "Time":
        addon_info_time = f"| Against constraint of {constraint_info[0]} hours"
    else:
        addon_info_cost = f"| Against constraint of £{constraint_info[1]}"

    output = f"""
    ========================================
    EVENT PLANNER - RESULTS
    ========================================

    Input File: {file_name}
    Available Time: {constraint_info[0]}
    Available Budget: £{constraint_info[1]}

    Using constraint: {constraint_info[2]}

    --- BRUTE FORCE ALGORITHM ---
    Selected Activities:
    {bf_pretty_schedule}

    Total Enjoyment: {bf_enjoyment}
    Total Time Used: {bf_time} {addon_info_time}
    Total Cost: £{bf_cost} {addon_info_cost}

    Execution Time: {bf_runtime} seconds

    --- DYNAMIC PROGRAMMING ALGORITHM ---

    Selected Activities:
    {dp_pretty_schedule}

    Total Enjoyment: {dp_enjoyment}
    Total Time Used: {dp_time} {addon_info_time}
    Total Cost: £{dp_cost} {addon_info_cost}

    Execution Time: {dp_runtime} seconds

    ========================================
    """

    print(output)
    print(" ")

compare("input_medium.txt", "time")

compare("input_small.txt", "cost")


