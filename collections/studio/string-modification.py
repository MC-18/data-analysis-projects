my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
new_string = my_string[:3]
end_string = my_string[3:]
newest_string = end_string + new_string
print(new_string)
print(end_string)
print(end_string + new_string)

# Use a template literal to print the original and modified string in a descriptive phrase.
print('Original string reads', my_string, 'and moving the first 3 letters to the end results in', newest_string,'.')


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
