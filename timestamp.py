# NOTE: TRAFFIC file is interpreted as strings
import os
import ast 

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
i = 1
# While loop over length of timestamps
while i < len(timestamps):
    if i == len(timestamps) - 1:
        print('End of the line! {}'.format(i))
        fileSystem.close()
        break
    if timestamps[i]['timestamp'] < timestamps[i - 1]['timestamp']:
        string_timestamp = str(timestamps[i]['timestamp'])
        fileSystem.write(string_timestamp + '\n')
    i += 1

# Correct timestamps in while loop
j = 1
while j < len(timestamps):
    if j == len(timestamps) - 1:
        print('Correction done!')
        break
    if timestamps[j]['timestamp'] < timestamps[j - 1]['timestamp']:
        a, b = j, j-1
        timestamps[a], timestamps[b] = timestamps[b], timestamps[a] 
    j += 1

# Write fixed timestamps to file in while loop
k = 0
fileWrite = open(working_directory + '/timestamp_fix.txt', 'w+')
while k < len(timestamps):
    if k == len(timestamps) - 1:
        print('Writing file done!')
        fileWrite.close()
        break
    correct_string_timestamp = str(timestamps[k])
    fileWrite.write(correct_string_timestamp + '\n')
    k += 1

print(len(timestamps))
