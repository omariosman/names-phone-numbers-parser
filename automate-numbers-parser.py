# This script can be used to separate names from numbers so that you can import contacts easily on whatsapp hook

# Get input from the user
input_str = """
Angel,12012000080
Sayed,12012000404
Aly,12012001111
"""

# Split the input string by newline and then by comma
input_list = [item.split(",") for item in input_str.strip().split("\n")]
print("input list: ", input_list)

# Iterate over the list and take only the second element (which is the number) and add it to a new list
numbers_list = [item[1] for item in input_list]
print("numbers list: ", numbers_list)

# Write the numbers to a file
with open("output.txt", "w") as f:
    f.write("\n".join(numbers_list))
    
 """
 Output:
12012000080
12012000404
12012001111
 """
