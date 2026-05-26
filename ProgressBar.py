class ProgressBar: # A class for a simple progress bar that can be used in the console
    def __init__(self, length, fill_char='█', empty_char=' '):
        self.length = length # Number of loops to prepare for
        self.fill_char = fill_char # Character to print for each completed loop, defaults to full block
        self.empty_char = empty_char # Character to print for each loop yet to be completed, defaults to space

    def start_bar(self):
        print("\x1b[?25l\x1b[31m", end='', flush=True) # Hides the cursor and sets the text color to red
        print(f'[{self.empty_char * self.length}]\r[', end='', flush=True) # Defines the width between brackets
    
    def advance_bar(self):
        print(f'{self.fill_char}', end='', flush=True) # Prints a single filled character

    def end_bar(self):
        print(']\n') # Prints end cap and moves to next line
        print("\x1b[?25h\x1b[39m", end='', flush=True) # Shows the cursor and resets the text color to default

    def __enter__(self): # This runs with a context manager
        self.start_bar() # Automatically starts the progress bar when the block is entered, rather than manually
        return self

    def __exit__(self, exc_type, exc, tb):
        self.end_bar() # Automatically ends the progress bar when the block is exited, rather than manually