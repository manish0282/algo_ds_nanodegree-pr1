"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""
Input: provided data set for texts and calls
Output: Possible list of telemarketers
Solution: 
    1. List all unique outgoing numbers & Texts
    2. Filter the list of numbers in pt. 1 if they never received text/ calls
    3. Worst case complexity for this is O(n^2)
"""

outward_numbers = set()
receiving_numbers = set()

# Complexity: O(1)
def add_unique_number_to_list(item_list, out=1):
    index = 0

    while index < len(item_list):
        item = item_list[index]
        if out == 1:
            outward_numbers.add(item[0])
        else:
            receiving_numbers.add(item[1])
        index += 1


# Complexity: O(n)
def solve_part():
    # Complexity: O(1)
    add_unique_number_to_list(calls)
    # Complexity: O(1)
    add_unique_number_to_list(texts)

    # Complexity: O(1)
    add_unique_number_to_list(calls, out=0)
    # Complexity: O(1)
    add_unique_number_to_list(texts, out=0)

    telemarketers = list()

    out_index = 0
    in_index = 0

    # Complexity: O(1)
    outgoing_numbers = list(outward_numbers)
    inward_numbers = list(receiving_numbers)

    # Complexity: O(n)
    for out_index in (0, len(outgoing_numbers)-1):
        calling_number = str(outgoing_numbers[out_index])
        out_index += 1

        # Complexity: O(n)
        for in_index in (0, len(inward_numbers)-1):
            rec_num = str(inward_numbers[in_index])
            if calling_number == rec_num:
                telemarketers.append(calling_number)
            in_index += 1

    index = 0
    # Complexity: O(n)
    while index < len(telemarketers):
        print(telemarketers[index])
        index += 1


solve_part()
