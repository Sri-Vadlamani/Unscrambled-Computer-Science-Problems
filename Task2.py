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
def longest_time(list):
    totals={}
    for num, sec in list :
        if num not in totals :
            totals[num] = sec
        else :
            totals[num] += sec
    return totals

call_tel = [[call[0], int(call[3])] for call in calls]
receive_tel = [[call[1], int(call[3])] for call in calls]
full_list = call_tel + receive_tel
unique_list = longest_time(full_list)
long_time = list(max(zip(unique_list.values(), unique_list.keys())))
long_time[0],long_time[1]=long_time[1],long_time[0]
print("{} spent the longest time, {} seconds, on the phone during September 2016."
      .format(*long_time))
