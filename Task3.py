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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

''' 
Part A
Input - Calls data-set
Output - Print the list of unique area codes called from number with prefix 080
Solution - 
    1. Find numbers called from 080
    2. Check for the unique area codes of these called numbers and store them
    3. Sort result in chronological order
    4. Print the sorted result set with the provided message 
'''

CUSTOMER_CARE_PREFIX = "140"


# Complexity: O(1)
def get_phone_prefix(number):
    if number.find("(") != -1:
        split_str = number.split(')')

        first_part = split_str[0]
        prefix_first_part = first_part.replace('(', "")

        return prefix_first_part

    return None


# Complexity: O(n)
def solve_part_a():
    index = 0
    prefix_set = set()

    # iterate through whole data set - O(n)
    while index < len(calls):
        item = calls[index]

        calling_number = item[0]

        # get the prefix to ascertain if the callee was from Bangalore
        number_prefix = get_phone_prefix(calling_number)

        # if call made from Bangalore, Complexity O(1)
        if number_prefix == "080":

            called_number = item[1]

            if get_phone_prefix(called_number) is not None:
                prefix_set.add(get_phone_prefix(called_number))

            elif called_number.find(" "):
                mobile_number = called_number.split(" ")
                mobile_prefix = mobile_number[0]
                prefix_set.add(mobile_prefix)

            else:
                if called_number.find(CUSTOMER_CARE_PREFIX, 0) != -1:
                    prefix_set.add(CUSTOMER_CARE_PREFIX)

        index += 1

    # Complexity: O(nlog n)
    sorted_numbers = sorted(prefix_set, key=int)

    index = 0
    while index < len(sorted_numbers):
        print(sorted_numbers[index])
        index += 1


''' 
Part B
Input - Calls data-set
Output - Percentage of calls to & from Bangalore numbers 
Solution - 
    1. Find numbers called from 080
    2. Check for the unique area codes of these called numbers and if they are to 080, add them
    3. Print the result with the provided message 
'''


def solve_part_b():
    index = 0
    count_of_calls_to_bangalore = 0
    total_Calls_from_bangalore = 0

    # iterate through whole data set - O(n)
    while index < len(calls):
        item = calls[index]

        calling_number = item[0]

        # get the prefix to ascertain if the callee was from Bangalore
        number_prefix = get_phone_prefix(calling_number)

        # if call made from Bangalore, Complexity O(1)
        if number_prefix == "080":
            total_Calls_from_bangalore += 1
            called_number = item[1]

            if get_phone_prefix(called_number) is not None and get_phone_prefix(called_number) == "080":
                count_of_calls_to_bangalore += 1

        index += 1

    #     Complexity O(1)
    percentage_of_calls = (count_of_calls_to_bangalore * 100) / total_Calls_from_bangalore

    print(str(round(percentage_of_calls, 2)) + " percent of calls from fixed lines in Bangalore are calls to other "
                                               "fixed lines in Bangalore.")


# Complexity O(NLogN)
solve_part_a()

# Complexity O(n)
solve_part_b()
