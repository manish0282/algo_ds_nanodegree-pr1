"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from typing import Set, Any, List, Dict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

''' 
Input - provided dataset for calls
Output - Maximum time spent and the Calling number associated with it
'''


def get_unique_number_from_list(item_list):
    index = 0

    all_numbers = set()
    while index < len(item_list):
        item = item_list[index]
        all_numbers.add(item[0])
        all_numbers.add(item[1])
        index += 1

    unique_numbers = list(all_numbers)
    return unique_numbers


'''Time complexity:
Steps performed 
step 1 - Create a unique set of the provided files - this includes going over the whole list so worst case will be to run 
 the loop same number of times as the input size -- n*m (assuming n and m are ist sizes for both texts & calls respectively'''
# unique_number_list = get_unique_number_from_list(calls)

number_duration: Dict[Any, int] = dict()


def solve_task_3():
    # (item_list):
    index = 0
    phone = ""
    duration = 0

    unique_number_list = get_unique_number_from_list(calls)

    # Step 1: iterates through the whole data set of size n

    while index < len(unique_number_list):
        item = unique_number_list[index]
        duration_of_call = 0

        # step 2: check if this number exists in either the callee or the called number
        number_count = 0
        while number_count < len(calls):
            callee = calls[number_count][0]
            caller = calls[number_count][1]

            if callee == item or caller == item:
                duration = calls[number_count][3]
                duration_of_call += int(duration)

            number_count += 1

        number_duration[item] = duration_of_call
        index += 1

    # Step 3: Print takes constant time. So worst case complexity is O(n)
    sorted_dict = sorted(number_duration.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    number_to_spend_most_time = sorted_dict[0]

    print(number_to_spend_most_time[0] + " spent the longest time, " + str(number_to_spend_most_time[1]) + " seconds, on the phone during September 2016.")


solve_task_3()
