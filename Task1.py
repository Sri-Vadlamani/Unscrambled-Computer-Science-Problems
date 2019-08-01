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
diff_tel_num = set()
text_out = set([text[0] for text in texts])
text_in = set([text[1] for text in texts])
call_out = set([call[0] for call in calls])
call_in = set([call[1] for call in calls])
diff_tel_num.update(text_out)
diff_tel_num.update(text_in)
diff_tel_num.update(call_out)
diff_tel_num.update(call_in)

print("There are {} different telephone numbers in the records.".format(len(diff_tel_num)))
