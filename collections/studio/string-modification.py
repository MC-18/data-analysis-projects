my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
new_string = my_string[:3]
end_string = my_string[3:]
newest_string = end_string + new_string
print(end_string + new_string)

# Use a template literal to print the original and modified string in a 
# descriptive phrase.
print('Original string reads', my_string, 'and moving the first 3 letters to the end results in', newest_string,'.')

# b) Modify your code to accept user input. 
# Query the user to enter the number of letters that will be relocated.

user_input = input("Enter the number of letters to relocate: ")
selection_int = int(user_input)
altered_string = my_string[selection_int:] + my_string[:selection_int]
print(altered_string)

# c) Add validation to your code to deal with user inputs that are longer than 
# the word. In such cases, default to moving 3 characters. Also, the template 
# literal should note the error.
if selection_int > len(my_string):
    print("Input is greater than the length of the string.")
    selection_int = 3