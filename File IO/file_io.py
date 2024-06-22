"""
data science: working with data sets
-> the new york city crime statictics
-> 1,000 lines in a CSV file

web dev: working with HTML/CSS/JS
and you need to read those file in

-> read text files in python
-> write text files in python
-> use "with" blocks when reading/writing files
-> describe the different ways to open a file
-> Read CSV files in python
-> Write CSV files in python
-> JSON
"""

# read a file with the open function
# open returns a file object to you
# read a file object with read method

file = open("story.txt")
print(file.read())

file.seek(0)

file.readline()

file.seek(0)

arr = file.readlines()

file.closed

file.close()


with open("story.txt") as file:
	data = file.read()

print(data)
print(file.closed)


"""
-> You can also use open to write to a file
-> Need to specify the "w" flag as the second argument

-> r - read a file (no writing) - this is the default
-> w - write to a file (previous constents removed)
-> a - append to a file (previous contents not removed)
"""

with open("story.txt", "w") as file:
	file.write("Writing files is great\n")
	file.write("Here's another line of text\n")
	file.write("Closing now, goodbye!")

with open("story.txt", "a") as file:  # the file does not have to exist
	file.write("Writing files is great\n")
	file.write("Here's another line of text\n")
	file.write("Closing now, goodbye!")

with open("story.txt", "r+") as file:  # the file must exist for this
	file.write(";)")
	file.seek(9)
	file.write(";(")


def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)

def statistics(file):
    dict3 = {"lines": 0, "words": 0, "characters": 0}
    with open(file) as lines:
        dict3["lines"] = len(lines.readlines())
        
    with open(file) as words:
        data = words.read()
        arr = data.split()
        dict3["words"] = len(arr)
        
    with open(file) as words:
        data = words.read()
        char_num = 0
        for char in data:
            char_num += 1
        dict3["characters"] = char_num
        
    return dict3