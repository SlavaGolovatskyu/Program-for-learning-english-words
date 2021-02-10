import asyncio
from tkinter import *
from tkinter import messagebox
from database.connect import ManageDataBase
from add_words import WindowForAddWords

__author__ = 'Slava Golovatskyu'
__version__ = 'V-0.1'

width, height = 300, 250

class Program:
	def __init__(self, width, height):
		self.ManageDB = ManageDataBase()
		self.root = Tk()
		self.root.geometry(f'{width}x{height}+300+300')
		self.root.title('Learn English')
		self.root['bg'] = '#56ADE7'
		self.root.resizable(False, False)

		bg_for_buttons    = '#0f0505'
		fg_for_buttons    = '#ffffff'

		self.button_add_word = Button(text = 'Добавить слова', font = 'Consolas 13',
								     fg = fg_for_buttons, bg = bg_for_buttons,
								     relief = 'solid', activebackground = '#6e6f73',
								     activeforeground = '#eff5c9', width = '25',
							         height = '2', command = self.add_words)
		self.button_start = Button(text = 'Запустить', font = 'Consolas 13',
							      fg = fg_for_buttons, bg = bg_for_buttons,
								  relief = 'solid', activebackground = '#6e6f73',
								  activeforeground = '#eff5c9', width = '25',
								  height = '2')

		self.button_all_words = Button(text = 'Список всех слов', font = 'Consolas 13',
							      	  fg = fg_for_buttons, bg = bg_for_buttons,
								      relief = 'solid', activebackground = '#6e6f73',
								      activeforeground = '#eff5c9', width = '25',
								      height = '2')

	def add_words(self):
		self.root.withdraw()
		WindowForAddWords(self.root).run()

	def run(self):
		self.draw_window()
		self.root.mainloop()

	def draw_window(self):
		self.button_add_word.place(x = width/8, y = 40)
		self.button_start.place(x = width/8, y = 100)
		self.button_all_words.place(x = width/8, y = 160)

if __name__ == '__main__':
	Program(width, height).run()