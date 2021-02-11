"""
	* imported library configparser for the working with.ini files
	* Tkinter for the create App
	* database/connect.py imported for the working with DB
""" 
import configparser
from tkinter import *
from tkinter import messagebox
from database.connect import ManageDataBase

class Validation(object):
	def __init__(self):
		self.config = configparser.ConfigParser()  # create object parser's
		self.config.read("./options/options.ini") # read data from ./options/options.ini

	# 
	def back_return_bool(self) -> bool:
		if self.config['Work']['work'] == 'True':
			messagebox.showerror('Ошибка', 'Остановите сначала програму. Затем вы сможете выйти.')
			return False
		else:
			return True

	# Stopped program if she working
	# else send error.
	def stop(self):
		if self.config['Work']['work'] == 'True':
			self.config['Work']['work'] = 'False'
			messagebox.showinfo('Success', 'Програма успешно остановленна.')
		else:
			messagebox.showerror('Error', 'Режим изучения слов не включен.')

class WindowForStartLearn(Validation):
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

	def stop(self):
		super(WindowForStartLearn, self).stop()

	def back(self):
		if super(WindowForStartLearn, self).back_return_bool():
			self.root.destroy()
			self.main.deiconify()

	def delete_text(self, event):
		self.enter_3.delete(0, END)

	def run(self):
		self.draw_window()
		self.enter_3.insert(0, 'Установите таймер в секундах.')
		self.root.mainloop()

	def draw_window(self):
		self.enter_3.place(x = self.width/7.7, y = 80)
		self.button_back.place(x = self.width/4, y = 160)	


