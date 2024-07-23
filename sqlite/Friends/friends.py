import sqlite3

# create connection
conn = sqlite3.connect('my_friends.db')

# create cursor object
c = conn.cursor()

# execute some sql with cursor
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# inserting with python
insert_query = "INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7)"
c.execute(insert_query)

data = ('Steve', 'Irwin', 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)

# Bulk insert with python
peoples = [
	('Roald', 'Amundsen', 5),
	('Rose', 'Parks', 8),
	('Harry', 'Potter', 10),
	('Elon', 'Musk', 10),
	('Brad', 'Pitt', 9)
]

for people in peoples:
	c.execute("INSERT INTO friends VALUES (?,?,?)", people)
	print("inserting now...")

# commit changes
conn.commit()

conn.close