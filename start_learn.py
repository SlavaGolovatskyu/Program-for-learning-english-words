"""
	* imported library json for the working with.json files
	* Tkinter for the create App
	* database/connect.py imported for the working with DB
	* "time" library need required for timer.
	* imported ControllThread from src for asynchronous programming
""" 

import json
import time
from tkinter import *
from tkinter import messagebox
from src.ControllThread import ControllerThreads
from database.connect import ManageDataBase

class Validation(object):
	"""
		* in advance. if Work == 0 mode don't work
		* else working
		* True and False replaced 1 and 0
	"""
	def checkToStart(self, time) -> bool:
		# upload data
		data = json.load(open('./options/options.json', 'r'))  
		# Learn the number of elements in DataBase
		DBlength = ManageDataBase().check_length_db()
		# number check
		isdigitTime = time.isdigit()
		if isdigitTime:
			if int(time) > 0:
				if data['Work'] == 0:
					if DBlength:
						return True
					else:
						messagebox.showerror('Error', 'В базе данных нет ни единого слова.')
						return False
				else:
					messagebox.showerror('Error', 'Режим уже был запущен.')
					return False
			else:
				messagebox.showerror('Error', 'Некоректное количество секунд.')
				return False
		else:
			messagebox.showerror('Error', 'Вы указали вместо секунд буквы.')
			return False

	# This feature is designed to check if the mode works or not.
	def checkButtonToReturn(self) -> bool:
		data = json.load(open('./options/options.json', 'r'))
		if data['Work'] == 1:
			messagebox.showerror('Ошибка', 'Остановите сначала програму. Затем вы сможете выйти.')
			return False
		return True

	"""
	   * Stopped mode if he is working
	   * else send error.
	"""
	def stop(self):
		data = json.load(open('./options/options.json', 'r'))
		if data['Work'] == 1:
			data['Work'] = 0
			data['Timer'] = 0
			with open('./options/options.json', 'w') as f:
				json.dump(data, f)
			messagebox.showinfo('Success', 'Програма успешно остановленна.')
		else:
			messagebox.showerror('Error', 'Режим изучения слов не включен.')

class StartMode(Validation):
	def init(self):
		# run the function in a separate thread
		self.AsyncStart = ControllerThreads(target = lambda: self.CentrallMode())
		self.AsyncStart.start()

	def CentrallMode(self):
		while True:
			data = json.load(open('./options/options.json', 'r'))
			messagebox.showinfo('Word', f'{ManageDataBase().get_random_word()}')
			time.sleep(data['Timer'])
			data = json.load(open('./options/options.json', 'r'))
			if data['Work'] == 0:
				self.AsyncStart.kill()
				self.AsyncStart.join()
				break

	def startMode(self, time):
		if super(StartMode, self).checkToStart(time):
			data = json.load(open('./options/options.json', 'r'))
			data['Work'] = 1
			data['Timer'] = int(time)
			with open('./options/options.json', 'w') as f:
				json.dump(data, f)
			self.init()

class WindowForStartLearn(StartMode):
	def __init__(self, parent):
		self.ManageDB = ManageDataBase()

		# Width and Height APP
		self.width, self.height = 400, 300

		# Create self variable parent
		self.main = parent

		# Creating daughter window based on the father
		self.root = Toplevel(parent)

		self.root.geometry(f'{self.width}x{self.height}+300+300')
		self.root.title('Learn English')
		self.root['bg'] = '#56ADE7'
		self.root.resizable(False, False)

		bg_for_buttons = '#0f0505'
		fg_for_buttons = '#ffffff'
		bg_for_entry = '#5b6b6b'
		fg_for_entry = '#4de3e3'

		self.enter_3 = Entry(self.root, bg = bg_for_entry,
							fg = fg_for_entry, width = '30',
							font = 'Consolas 12', justify = 'center')
		self.button_back = Button(self.root, text = 'Назад', width = '25', height = '2',
							     bg = bg_for_buttons, fg = fg_for_buttons, command = self.back)
		self.button_stop = Button(self.root, text = 'Остановить', width = '25', height = '2',
							     bg = bg_for_buttons, fg = fg_for_buttons, command = self.stop)
		self.button_start = Button(self.root, text = 'Запустить.', width = '25', height = '2',
							      bg = bg_for_buttons, fg = fg_for_buttons, command = self.start_regime)

		self.enter_3.bind('<Button-1>', self.delete_text)

	def start_regime(self):
		if self.enter_3.get():
			super(WindowForStartLearn, self).startMode(self.enter_3.get())
		else:
			messagebox.showerror('Error', 'Введите данные!')

	def stop(self):
		super(WindowForStartLearn, self).stop()

	def back(self):
		if super(WindowForStartLearn, self).checkButtonToReturn():
			self.root.destroy()
			self.main.deiconify()

	def delete_text(self, event):
		self.enter_3.delete(0, END)

	def run(self):
		self.draw_window()
		self.enter_3.insert(0, 'Установите таймер в секундах.')
		self.root.mainloop()

	def draw_window(self):
		self.enter_3.place(x = self.width/7.7, y = 40)
		self.button_back.place(x = self.width/4, y = 100)	
		self.button_stop.place(x = self.width/4, y = 160)
		self.button_start.place(x = self.width/4, y = 220)


