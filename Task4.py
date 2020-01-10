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

calling_numbers = set()
non_calling_numbers = set()


# Complexity: O(1)
def add_text_numbers():
    index = 0

    while index < len(texts):
        item = texts[index]
        non_calling_numbers.add(item[0])
        non_calling_numbers.add(item[1])
        index += 1


# Add calling & non calling numbers to callers and non callers set
def filter_calling_number():
    index = 0

    while index < len(calls):
        item = calls[index]
        calling_numbers.add(item[0])
        non_calling_numbers.add(item[1])
        index += 1


# Complexity: O(n)
def solve_part():
    # Complexity: O(1)
    filter_calling_number()

    # Complexity: O(1)
    add_text_numbers()

    telemarketers = calling_numbers.difference(non_calling_numbers)

    # Complexity: O(n)
    index = 0

    sorted_list = list(telemarketers)
    sorted_list.sort()

    while index < len(sorted_list):
        print(sorted_list[index])
        index += 1


solve_part()
