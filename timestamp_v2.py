import os
import ast
from operator import itemgetter

working_directory = os.path.dirname(os.path.abspath(__file__))

# Initialize empty list as timestamps
timestamps = []

# Open the file with absolute path and append to timestamps
with open(working_directory + '/timestamp-error-1501617611789.traffic') as f:
    for line in f.readlines():
        # Convert strings to a dictionary 
        to_dictionary = ast.literal_eval(line)
        timestamps.append(to_dictionary)

# Now that we have a copy in a list....Time for the fun part!
fileSystem = open(working_directory + '/timestamp_errors.txt', 'w+')
# While loop over length of timestamps
i = 1
while i < len(timestamps):
    if i == len(timestamps) - 1:
        print('End of the line! {}'.format(i))
        fileSystem.close()
        break
    if timestamps[i]['timestamp'] < timestamps[i - 1]['timestamp']:
        string_timestamp = str(timestamps[i]['timestamp'])
        fileSystem.write(string_timestamp + '\n')
    i += 1

# Fix timestamps
fixed_timestamps = sorted(timestamps, key = itemgetter('timestamp'))
fileWrite = open(working_directory + '/timestamp_fix.txt', 'w+')
for i in fixed_timestamps:
    fileWrite.write(str(i) + '\n')