from ProgressBar import ProgressBar # Needs to be in the same directory to import
import time # Imitates process time of a repeating function

time_bar = ProgressBar(15) # Number of loops to prepare for
time_bar.start_bar() # Generates the progress bar with the specified length
# From this point on, do not print anything to the console
for i in range(15): # Imitating a 15-loop process
    time.sleep(0.5) # Delay
    time_bar.advance_bar() # Prints out a filled character to show completion of loop
time_bar.end_bar() # Prints closing bracket and moves to the next line
# You may now print things to the console again

with ProgressBar(20) as bar: # More condensed way to do the same thing as above, using a context manager
    # Using the with statement automatically starts the progress bar
    # Do not print anything to the console until the end of the block
    for i in range(20):
        time.sleep(0.3)
        bar.advance_bar()
    # At the end of the block, it automatically closes the progress bar and moves to the next line