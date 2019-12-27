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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
all_numbers = set()

''' This method takes any list as input and adds the incoming & outgoing numbers to the set
Since set can contain only the unique elements, the resulting structure will have no repeated members'''


def get_unique_number_from_list(item_list):
    index = 0
    while index < len(item_list):
        item = item_list[index]
        all_numbers.add(item[0])
        all_numbers.add(item[1])
        index += 1


'''Time complexity:
Steps performed 
step 1 - Create a unique set of the provided files - this includes going over the whole list so worst case will be to run 
 the loop same number of times as the input size -- n*m (assuming n and m are ist sizes for both texts & calls respectively'''
get_unique_number_from_list(texts)
get_unique_number_from_list(calls)

'''Step - 2 This will take constant amount of time

so O(n) is the worst case complexity for this problem'''
print("There are " + len(all_numbers).__str__() + " different telephone numbers in the records.")


def test():
    with open('sample.csv', 'r') as f:
        reader = csv.reader(f)
        samples = list(reader)
        get_unique_number_from_list(samples)

        print("There are " + len(all_numbers).__str__() + " different telephone numbers in the records.")


# test()