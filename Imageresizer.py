from Tkinter import *
import ttk

# print(dir(ttk.Style.configure))
master = Tk()

# def browse_action():
#     global folder_path
#     filename = filedialog.askdirectory()
#     folder_path.set(filename)
#     print(filename)

main_wrapper = ttk.Frame(master)
main_container = ttk.Frame(main_wrapper)
title = ttk.Label(main_container, text='Image Resizer')
input_label = ttk.Label(main_container, text='Input Directory')
input_entry = ttk.Entry(main_container)
input_button = ttk.Button(main_container, text='Browse')

output_label = ttk.Label(main_container, text='Output Directory')
output_entry = ttk.Entry(main_container)
output_button = ttk.Button(main_container, text='Browse')

separator = ttk.Separator(main_container)

resize_button = ttk.Button(main_container, text='Resize')

title.grid(row=0, column=0, columnspan=3, ipady=10)
input_label.grid(row=1, column=0, sticky=W)
input_entry.grid(row=1, column=1)
input_button.grid(row=1, column=2)

output_label.grid(row=2, column=0, sticky=W)
output_entry.grid(row=2, column=1)
output_button.grid(row=2, column=2)

separator.grid(row=3, columnspan=3, sticky='news', ipady=20)
resize_button.grid(row=4, columnspan=2)

main_wrapper.grid(ipady=10, ipadx=10)
main_container.grid(columnspan=3)
master.grid_columnconfigure(0, weight=1)
master.grid_rowconfigure(0, weight=1)

master.mainloop()