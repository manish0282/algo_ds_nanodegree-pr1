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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# 1 What is the first record of texts and what is the last record of calls?

'''Input - provided data files

Big-O: 
Finding the first record of text and last record of calls is independent of the input size, say n. 
The time complexity or the big-O notation for either of the operations is constant time or O(1)'''
first_record_Of_text = texts[0]
last_record_Of_calls = calls[- 1]

print("First record of texts, " + first_record_Of_text[0] + " texts " + first_record_Of_text[1] + " at time " + first_record_Of_text[2])
print("Last record of calls, " + last_record_Of_calls[0] + " calls " + last_record_Of_calls[1] + " at time " + last_record_Of_calls[2], " lasting " + last_record_Of_calls[3] + " seconds")

