"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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


def solve_task_3(item_list):
    index = 0
    phone = ""
    duration = 0

# Step 1: iterates through the whole data set of size n
    while index < len(item_list):
        item = item_list[index]

# Step 2: Comparison happens in constant time and is independent of the sample size
        if duration < int(item[3]):
            phone = item[0]
            duration = int(item[3])
        index += 1

# Step 3: Print takes constant time. So worst case complexity is O(n)
    print(phone + " spent the longest time, " + str(duration) + " seconds, on the phone during September 2016.")


solve_task_3(calls)


def test():
    with open('sample.csv', 'r') as f:
        reader = csv.reader(f)
        samples = list(reader)

        solve_task_3(samples)

# 1. input is the list of calls from the csv file
# 2. Output is "Number" and "time" tuple
# 3.

# test()

