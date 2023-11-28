# Mehraneh 30062786
# AT3.1 
# File I/O and Pseudo Code

#Declare variables and assign them the string
string1 = """Python has been an important part of Google since the beginning,
and remains so as the system grows and evolves.  \n"""
string2 = """Today dozens of Google engineers use Python, and we're looking
for more people with skills in this language." said PEter Norvig,
director of search quality at Google, Inc."""
# concatenate two strings and assign it to a variable
output_string = string1 + string2
# open a txt file in a write mode and if it doesn't exist create it
file = open("python.txt", "w")
# write the concatenate strings in the file
file.write(output_string)
# close the file
file.close()
# open the txt file in read mode
file =  open("python.txt", "r")
# with for loop read each line of the txt file
for input_string in file:
    # Display each line of the txt file
    print(input_string, end="")
    # close the file
file.close()

