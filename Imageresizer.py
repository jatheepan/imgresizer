from Tkinter import *
import ttk, tkFileDialog

# print(dir(ttk.Style.configure))
master = Tk()


def browse(target_input):
  filename = tkFileDialog.askdirectory()
  target_input.delete(0, END)
  target_input.insert(0, filename)


main_wrapper = ttk.Frame(master)
main_container = ttk.Frame(main_wrapper)
title = ttk.Label(main_container, text='Image Resizer')
input_label = ttk.Label(main_container, text='Input Directory')
input_entry = ttk.Entry(main_container)
input_button = ttk.Button(main_container, text='Browse', command=lambda:browse(input_entry))

output_label = ttk.Label(main_container, text='Output Directory')
output_entry = ttk.Entry(main_container)
output_button = ttk.Button(main_container, text='Browse', command=lambda:browse(output_entry))

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
resize_button.grid(row=4, columnspan=3)

main_wrapper.grid(ipady=10, ipadx=10)
main_container.grid(columnspan=3)
main_wrapper.grid_columnconfigure(0, weight=1)
main_wrapper.grid_rowconfigure(0, weight=1)
master.title('Resize Images')
master.configure(background=master.cget('background'))
master.resizable(False, False)
master.mainloop()