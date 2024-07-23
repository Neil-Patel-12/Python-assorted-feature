import sqlite3
conn = sqlite3.connect('my_friends.db')

# create cursor object
c = conn.cursor()

c.execute("SELECT * FROM friends")
# c.execute("SELECT * FROM friends WHERE closeness > f ORDER BY closeness")

list_of_friends = []
for people in c:
	list_of_friends.append(people)

print(list_of_friends)

"""
c.fetchall()
c.fetchone()
"""

# commit changes
conn.commit()
conn.close()