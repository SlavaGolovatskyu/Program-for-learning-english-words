import sqlite3
import random

class ManageDataBase:
	def __init__(self):
		self.db = sqlite3.connect('./database/sqlite.db')
		self.s = self.db.cursor()
		self.create_table_if_not_exists()

	def create_table_if_not_exists(self):
		self.s.execute("""CREATE TABLE IF NOT EXISTS 
			      Words(_id INTEGER PRIMARY KEY AUTOINCREMENT,
			      word TEXT)""")
		self.db.commit()

	def get_random_word(self):
		count = self.s.execute('SELECT COUNT(*) FROM Words').fetchone()[0]
		if count == 1:
			return self.s.execute('SELECT word FROM Words WHERE _id = (?)', (1,)).fetchone()[0]
		return self.s.execute("""SELECT word FROM Words WHERE _id = (?)""",
				     (random.randint(1, count + 1),)).fetchone()[0]

	def write_word_in_db(self, word):
		self.s.execute('INSERT INTO Words(word) VALUES (?)', (word,))
		self.db.commit()
