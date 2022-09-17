
string = 'amaama'
half = int(len(string) / 2)
 
if len(string) % 2 == 0:  # even
    first_str = string[:half]
    second_str = string[half:]
else:  # odd
    first_str = string[:half]
    second_str = string[half+1:]
 
# symmetric
if first_str == second_str:
    print(string, 'string is symmertical')
else:
    print(string, 'string is not symmertical')