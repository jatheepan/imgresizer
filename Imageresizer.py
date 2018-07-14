import ttk
import tkFileDialog
from Tkinter import *
from gui.choose_folder import ChooseFolder
from gui.settings import sizing_options

master = Tk()


def browse(target_input):
    filename = tkFileDialog.askdirectory()
    target_input.delete(0, END)
    target_input.insert(0, filename)


main_wrapper = ttk.Frame(master)
main_container = ttk.Frame(main_wrapper)
title = ttk.Label(main_container, text='Image Resizer')
input_folder = ChooseFolder(main_container, **{'label_text': 'Input Directory', 'label_width': 15})
output_folder = ChooseFolder(main_container, **{'label_text': 'Output Directory', 'label_width': 15})
size_option = sizing_options(main_container)
separator = ttk.Separator(main_container)


def resize_action():
    print(input_folder.get_value())


resize_button = ttk.Button(main_container, text='Resize', command=resize_action)

title.grid(row=0, column=0, columnspan=3, ipady=10)

input_folder.grid(row=1, columnspan=3, sticky=W)
output_folder.grid(row=2, columnspan=3, sticky=W)

separator.grid(row=3, columnspan=3, sticky='news', ipady=20)
size_option.grid(row=4, columnspan=3, ipady=20)
resize_button.grid(row=5, columnspan=3)

main_wrapper.grid(ipady=10, ipadx=10)
main_container.grid(columnspan=3)
main_wrapper.grid_columnconfigure(0, weight=1)
main_wrapper.grid_rowconfigure(0, weight=1)
master.title('Resize Images')
master.configure(background=master.cget('background'))
master.resizable(False, False)
master.mainloop()
