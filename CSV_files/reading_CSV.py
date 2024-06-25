# CSV files are a common file format for tabular data
# read just like any other text file
# built-in CSV module to read/write CSVs

# reader - lets you iterate over rows of the CSV as lists
# DictReader - lets you iterate over rows of the CSV as OrderedDicts
from csv import reader
from csv import DictReader

"""

with open("fighters.csv") as file:
	csv_reader = reader(file)
	print(csv_reader)  # <_csv.reader object at 0x000001742204E980>
	next(csv_reader)  # the headers will be removed
	for row in csv_reader:
		print(row)  # each row in a list

with open("fighters.csv") as file:
	csv_reader = reader(file)
	data = list(csv_reader)
	print(data)

"""

with open("fighters.csv") as file:
	csv_dict = DictReader(file)
	for row in csv_dict:
		print(row["Name"])  # each row is an OrderedDict!

with open("fighters.csv") as file:
	csv_reader = reader(file, delimiter="|")
	for row in csv_reader:
		print(row)