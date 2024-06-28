
input_string = input("Enter a string: ")

# Reverse the string using a loop
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string

# Print the reversed string
print("Reversed string:", reversed_string)
