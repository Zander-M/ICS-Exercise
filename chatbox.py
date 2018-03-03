from tkinter import *
import socket


class Chatbox:
	def __init__(self, name):
		self.name = name
		self.root = Tk()  # initialize the window
		root_wid = self.root.winfo_width()
		root_hgt = self.root.winfo_height()
		screen_wid, screen_hgt = self.root.maxsize()
		self.root.geometry('300x150+{}+{}'.format((screen_wid - root_wid) // 2, (screen_hgt - root_hgt) // 2))
		self.root.title("{}".format(self.name))
		self.label = Label(self.root, text="Local Chatting System")
		self.label.pack()
		self.canvas = Canvas(self.root, width=200, height=70)
		self.canvas.pack()
		self.button = Button(self.canvas, text="LOG IN", command=self.click)
		self.button.pack(side=RIGHT, fill='y')
		self.username = Entry(self.canvas, width=20)
		self.username.pack(padx=0)
		self.username.insert(0, "your username here")
		self.password = Entry(self.canvas, width=20)
		self.password.pack(padx=0)
		self.password.insert(0, "your password here")

		self.root.mainloop()

	def click(self):
		# a function that gets the input of the user
		print(self.username.get(),self.password.get())
		self.username.delete(0,END)
		self.password.delete(0,END)


cb1 = Chatbox("Chatbox")



