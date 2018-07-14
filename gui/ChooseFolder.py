from Tkinter import *
import ttk, tkFileDialog


class ChooseFolder(ttk.Frame):

  def __init__(self, container, label_text='Folder', label_width=10):
    ttk.Frame.__init__(self, container)
    self.label = ttk.Label(self, text=label_text, width=label_width)
    self.entry = ttk.Entry(self)
    self.button = ttk.Button(self, text='Browse', command=self.open_dialog)

    self.label.grid(row=0, column=0)
    self.entry.grid(row=0, column=1)
    self.button.grid(row=0, column=2)


  def open_dialog(self):
    dir_path = tkFileDialog.askdirectory()
    self.entry.delete(0, END)
    self.entry.insert(0, dir_path)


  def get_value(self):
    return self.entry.get()
