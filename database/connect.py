# imported "sqlite3" as a DataBase
# imported library "random" for the generation random number
import sqlite3
import random

class ManageDataBase:
	def __init__(self): # def Initialization
		# Connect to DB
		self.db = sqlite3.connect('./database/sqlite.db')
		# Take a cursor
		self.s = self.db.cursor()
		# Call Function
		self.create_table_if_not_exists()

	def create_table_if_not_exists(self):
		# Create table if it is not there
		self.s.execute("""CREATE TABLE IF NOT EXISTS 
					  Words(_id INTEGER PRIMARY KEY AUTOINCREMENT,
					  word TEXT)""")
		self.db.commit()

	# Get random word from DataBase
	def get_random_word(self):
		# Learn the number of elements in the DataBase
		count = self.s.execute('SELECT COUNT(*) FROM Words').fetchone()[0]
		if count == 1:
			return self.s.execute('SELECT word FROM Words WHERE _id = (?)', (1,)).fetchone()[0]
		return self.s.execute("""SELECT word FROM Words WHERE _id = (?)""",
							 (random.randint(1, count),)).fetchone()[0]

	# Validation
	def check_length_db(self) -> bool:
		count = self.s.execute('SELECT COUNT(*) FROM Words').fetchone()[0]
		if count == 0:
			return False
		return True

	# Note word in DataBase
	def write_word_in_db(self, word):
		self.s.execute('INSERT INTO Words(word) VALUES (?)', (word,))
		self.db.commit()