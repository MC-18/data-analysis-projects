# Part 1 A -- Make a Line
def make_line(size):
    line = ""
    for i in range(size):
        line += "#"
    return line

# print(make_line(5))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
# def make_square(size):
#     square = ""
#     for i in range(size):
#         line = make_line(size)
#         square += (make_line(size) + "\n")
#     return square
# print(make_square(5))




# Part 1 C -- Make a Rectangle
# def make_rectangle(width, height):
#     rectangle = ""
#     for i in range(height):
#         rectangle += (make_line(width) + "\n")
#     return rectangle
# print(make_rectangle(5, 3))

# Making a square using make_rectangle
# def make_square(size):
#     return (make_rectangle(size, size))
# print(make_square(5))


# Part 2 A -- Make a Stairs
# def make_downward_stairs(height):
#     stairs = ""
#     for i in range(height):
#         stairs += (make_line(i + 1) + "\n")
#     return stairs
# print(make_downward_stairs(5))

# Part 2 B -- Make Space-Line 
def make_space_line(numSpaces, numChars):
    spaces = "_" * numSpaces
    chars = "#" * numChars
    return spaces + chars + spaces
print(make_space_line(3, 5))





# Part 2 C -- Make Isosceles Triangle





# Part 3 -- Make a Diamond






