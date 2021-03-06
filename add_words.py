from tkinter import *
from tkinter import messagebox
from database.connect import ManageDataBase

class WindowForAddWords:
	def __init__(self, parent):
		self.width = 400
		self.height = 300
		self.main = parent
		self.root = Toplevel(parent)
		self.ManageDB = ManageDataBase()
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
		self.button_note_word = Button(self.root, text = 'Записать слово', width = '25', height = '2',
							          bg = bg_for_buttons, fg = fg_for_buttons, command = self.add_word)

		self.enter_3.bind('<Button-1>', self.delete_text)

	def add_word(self):
		self.ent = self.enter_3.get()
		if self.ent:
			self.ManageDB.write_word_in_db(self.ent)
			messagebox.showinfo('Success', 'Успешно записано.')
		else:
			messagebox.showerror('Error', 'Вы не указали слово!')

	def back(self):
		self.root.destroy()
		self.main.deiconify()

	def delete_text(self, event):
		self.enter_3.delete(0, END)

	def run(self):
		self.draw_window()
		self.enter_3.insert(0, 'Введите слово с переводом')
		self.root.mainloop()

	def draw_window(self):
		self.enter_3.place(x = self.width/7.7, y = 80)
		self.button_back.place(x = self.width/4, y = 160)
		self.button_note_word.place(x = self.width/4, y = 240)		


