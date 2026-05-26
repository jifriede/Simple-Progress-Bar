# Simple Progress Bar
A simple way to monitor progress on a looping program (python).  
## Purpose
When programs are computationaly expensive, they take time to perform their task. Sometimes it is useful to be aware of how long it will take or that it's not stuck in an infinite loop. This simple program allows you to import a class and have easy progress bars.
## Inputs
``` python
ProgressBar(length, fill_char*, empty_char*)
```
- length is required, defines the number of empty spaces between brackets
- fill_char is optional, simply changes the character printed for each completed loop
- empty_char is optional, simply changes the character printed between the brackets during start_bar
## Commands
Initialization:

``` python
example_bar = ProgressBar(15)
```

This makes a example_bar object for a 15-loop bar.

``` python
start_bar()
```

- Based on the bar's initialization, creates an empty bar in the console.  
- Do not print anything to console until the bar is finished.  

``` python
advance_bar()  
```

- Prints a single fill_char  

``` python
end_bar()  
```

- Prints the bar cap and moves to a new line.  
- You may now print things to console again.  

### This can be used with a context manager:  

``` python
with ProgressBar(length) as bar:
    for i in range(length):
        # code
        bar.advance_bar()
```

- This means that you don't need to manually start_bar or end_bar.
- Don't print anything to console while within the context block.

## Dependancies
No dependancies needed.   
time import library is needed for example.py
## Assumptions
**Assumes you are not printing anything to the console while the bar is active**. This is very important! You can use console cursor locations to fix this assumption, but I designed this to be a very simple progress bar.
## Authors
Jared-Isaac Friedel
## Created
2026-04-30
## Last Updated
2026-05-26
## Version
v2.1