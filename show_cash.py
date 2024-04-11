import tkinter as tk
import os

#pyinstaller --onefile --windowed --add-data "1.png" --add-data "2.png:." --add-data "5.png:." --add-data "10.png:." --add-data "20.png:." --add-data "50.png:." --add-data "100.png:." --add-data "200.png:." show_cash.py
#pyinstaller --onefile --windowed show_cash.py                       - that works to create an exe file 

# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)

class Bank():
	def __init__(self):
		self.tab = [1, 2, 5, 10, 20, 50, 100, 200]
		self.coins = 3
		self.images = ["1.png", "2.png", "5.png", "10.png", "20.png", "50.png", "100.png", "200.png"]
		self.sizes = [23, 21, 24, 60, 63, 66, 69, 72]
		self.images_list = [] #shown on the screen
		self.labels_list = []

		self.account = [0 for _ in range(len(self.tab))]
		self.value = 0
		self.updateCash()

		
		self.w = tk.Tk()
		self.w.title("Cash Displayer")
		# self.w.geometry('1400x1000')
		self.showOnScreen()
		# self.canvas = tk.Canvas(self.w)
		# self.canvas.grid()
		self.w.mainloop()
		
	def setValue(self, value):
		self.value = value

	def digit_count(number):
		digit_count = 0
		while number != 0:
			digit_count += 1
			number //= 10
		return digit_count

	def updateCash(self, value = -1):
		if value == -1:
			value = self.value
		for banknot in range(len(self.tab)-1, -1, -1):
			self.account[banknot] = value // self.tab[banknot]
			value = value % self.tab[banknot]
			#if self.account[banknot] != 0:
			#	print(str(self.account[banknot])+"x "+str(self.tab[banknot]), end="  ")

	def showCash(self):
		stringCash = ""
		for i in range(len(self.account)-1, -1, -1):
			if self.account[i] != 0:
				stringCash = stringCash + str(self.account[i])+"x "+str(self.tab[i])+"  "
		return stringCash
	
	def printCash(self):
		print(self.showCash())
	
	def resize_image(self, path, new_height):
		# Calculate the width while maintaining the aspect ratio
		image = tk.PhotoImage(file=path)   # resource_path means that all images will be included in exe file
		original_width = image.width()
		original_height = image.height()
		aspect_ratio = original_width / original_height
		new_width = int(new_height * aspect_ratio)

		# Resize the image
		resized_image = image.subsample(round(original_width / new_width), round(original_height / new_height))

		return resized_image
	
	def showAllImages(self):
		row_index = 5
		column_index = 0
		columns = len(str(self.value))
		for i in range(len(self.tab)-1,-1,-1):
			for _ in range(self.account[i]):
				resized_image = self.resize_image(self.images[i], self.sizes[i])
				self.images_list.append(resized_image)
				self.labels_list.append(tk.Label(self.w, image=self.images_list[-1]))
				self.labels_list[-1].grid(row=row_index, column=column_index)
				column_index += 1
				if column_index == columns:  # Reset column index and increment row index after every third image
					column_index = 0
					row_index += 1

	# def showOnCanvas(self):
	# 	self.images_list.append(PhotoImage(file=self.images[0]))
	# 	self.canvas.create_image((0, 0), image=self.images_list[0], anchor='nw')
	
	def clean_gui(self): # remove all images
		self.images_list = []
		for label in self.labels_list:
			label.destroy()

	def showOnScreen(self):
		def newValue(event):
			#res.configure(text = "Result: " + str(eval(entry.get()))) - this line help to show entry input on the screen, can compute things (eval)
			self.clean_gui()
			self.value = int(entry.get())
			self.updateCash(self.value)
			res.configure(text=self.showCash())        # print number of bills in gui
			self.showAllImages()

		# Place the widgets using grid to control layout precisely
		tk.Label(self.w, text="Dawaj kase:").grid(row=0, column=0)
		entry = tk.Entry(self.w)
		entry.bind("<Return>", newValue)
		entry.grid(row=0, column=1)
		res = tk.Label(self.w)
		res.grid(row=1, column=0, columnspan=2)

		# Remove the empty space after the entry by setting sticky to 'we' (west and east)
		entry.grid(sticky='nw')
		res.grid(sticky='nw')
		


bank = Bank()