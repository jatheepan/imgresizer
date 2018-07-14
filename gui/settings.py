from Tkinter import *
import ttk


def size_widget(container):
    frame = ttk.Frame(container)
    label_height = ttk.Label(frame, text='Height')
    entry_height = ttk.Entry(frame)
    label_width = ttk.Label(frame, text='Width')
    entry_width = ttk.Entry(frame)
    label_height.grid(row=0, column=0)
    entry_height.grid(row=0, column=1)
    label_width.grid(row=1, column=0)
    entry_width.grid(row=1, column=1)
    return frame


def sizing_options(container):
    frame = ttk.Frame(container)
    label = ttk.Label(frame, text='Select % or px')
    option_value = StringVar()
    option_perntge = ttk.Radiobutton(frame, text='%', variable=option_value, value='%')
    option_pixel = ttk.Radiobutton(frame, text='px', variable=option_value, value='px')
    size = size_widget(frame)
    option_value.set('%')

    label.grid(row=0, columnspan=2)
    option_perntge.grid(row=1, column=0)
    option_pixel.grid(row=1, column=1)
    size.grid(row=2, column=1)

    return frame


