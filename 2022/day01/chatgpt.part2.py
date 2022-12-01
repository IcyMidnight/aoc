# Ok can you now find the top three batches?
# Actually make that the sum of the top three batches

# Yes, here is a python program that loads a file specified as a command line argument and finds
# the sum of the top three batches with the largest sums:

import sys

# Get the file name from the command line argument
file_name = sys.argv[1]

# Open the file
with open(file_name, 'r') as f:
  # Read the file line by line
  lines = f.readlines()

# Initialize a list to store the top three batches
top_batches = []

# Initialize the current batch
current_batch = []

# Iterate over the lines
for line in lines:
  # Check if the line is blank
  if line.strip() == '':
    # If the line is blank, add the current batch to the list of top batches
    top_batches.append(current_batch)

    # Sort the top batches in descending order by their sums
    top_batches = sorted(top_batches, key=sum, reverse=True)

    # Keep only the top three batches
    top_batches = top_batches[:3]

    # Clear the current batch
    current_batch = []
  else:
    # If the line is not blank, convert the line to an integer and add it to the current batch
    current_batch.append(int(line))

# Print the sum of the top three batches
print(sum([sum(batch) for batch in top_batches]))

# This program reads the file name from the command line argument, and then reads the file line by
# line. It keeps track of the current batch of integers and adds it to a list of top batches when
# it encounters a blank line. It then sorts the top batches in descending order by their sums,
# keeps only the top three batches, and clears the current batch. Finally, it prints the sum of the
# top three batches.

# Please note that this program assumes that the file contains only integers and blank lines. If the
# file contains any other data, the program will throw an error.

# I hope this helps! Let me know if you have any other questions.
