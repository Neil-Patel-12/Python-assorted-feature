import sqlite3
conn = sqlite3.connect("users.db")

c = conn.cursor()

c.execute("CREATE TABLE users (username TEXT, password TEXT);")

insert_query = "INSERT INTO users VALUES ('Neil', 'runner');"
c.execute(insert_query)

u = input("please enter your username...")
p = input("please enter your password...")
c = conn.cursor()

# THE BAD WAY!
# query = f"SELECT * FROM users WHERE username='{u}' AND password = '{p}'"

# THE MUCH SAFER WAY
query = f"SELECT * FROM users WHERE username=? AND password =?"
c.execute(query,(u,p))

result = c.fetchone()
if(result):
	print("WELCOME BACK")
else:
	print("FAILED LOGIN")

conn.commit()
conn.close()

