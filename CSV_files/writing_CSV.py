# writer - creates a writer object for writing to CSV
# writerow - method on a writer to write a row to the CSV

from csv import writer, DictWriter, DictReader

with open("animals.csv", "w") as file:
	csv_writer = writer(file)
	csv_writer.writerow(["Name", "Age"])
	csv_writer.writerow(["Tiger", 36])
	csv_writer.writerow(["Bird", 70])


# DictWriter - creates a writer object for writing using dictionaries
# fieldnames - kwarg for DictWriter specifying headers
# writeheader - method on a writer to write header row
# writerow - method on a writer to write a row based on a dictionary

with open("animals.csv", "w") as file:
	headers = ["Name", "Breed" , "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})


def cm_to_in(cm):
	return float(cm) * 0.393701

with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	fighters = list(csv_reader)

with open("fighters_inches.csv", "w") as file:
	headers = ("Name", "Country", "Height")
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	for f in fighters:
		csv_writer.writerow({
			"Name": f["Name"],
			"Country": f["Country"],
			"Height": cm_to_in(f["Height (in cm)"])
		})