#here all algorithm comparisons will be made
import time

import BruteForce
import DynamicProgram

def compare(file_name, constraint):
    start = time.perf_counter()
    bf_schedule, bf_time, bf_cost, bf_enjoyment = BruteForce.main(file_name, constraint)
    end = time.perf_counter()
    bf_runtime = end - start

    start = time.perf_counter()
    dp_schedule, dp_time, dp_cost, dp_enjoyment, constraint_info = DynamicProgram.main(file_name, constraint)
    end = time.perf_counter()
    dp_runtime = end - start

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
    - Game-Night (3 hours, £80, enjoyment 120)
    - Pizza-Workshop (2 hours, £60, enjoyment 100)
    - Hiking (5 hours, £30, enjoyment 140)

    Total Enjoyment: {bf_enjoyment}
    Total Time Used: {bf_time}
    Total Cost: £{bf_cost}

    Execution Time: {bf_runtime} seconds

    --- DYNAMIC PROGRAMMING ALGORITHM ---

    Selected Activities:
    - Game-Night (3 hours, £80, enjoyment 120)
    - Pizza-Workshop (2 hours, £60, enjoyment 100)
    - Hiking (5 hours, £30, enjoyment 140)

    Total Enjoyment: {dp_enjoyment}
    Total Time Used: {dp_time}
    Total Cost: £{dp_cost}

    Execution Time: {dp_runtime} seconds

    ========================================
    """

    print(output)

compare("input_large.txt", "time")


