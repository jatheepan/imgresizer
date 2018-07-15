from Tkinter import *
import ttk


class SizingOptions(ttk.Frame):
    def __init__(self, container):
        ttk.Frame.__init__(self, container)
        selection_widget = SelectionWidget(self, self.on_selection_change)
        self.size_widget = SizeWidget(self)
        self.percentage_widget = PercentageWidget(self)
        selection_widget.grid(row=0, column=0, sticky=E)
        self.size_widget.grid(row=1, column=0)
        self.percentage_widget.grid(row=2, column=0)
        self.size_widget.grid_forget()

    def on_selection_change(self, selection):
        if selection == 'pixel':
            self.percentage_widget.grid_forget()
            self.size_widget.grid()
        elif selection == 'percentage':
            self.size_widget.grid_forget()
            self.percentage_widget.grid()

    def get_value(self):
        return {
            'size': self.size_widget.get_value(),
            'percentage': self.percentage_widget.get_value()
        }


class SelectionWidget(ttk.Frame):
    def __init__(self, container, callback):
        ttk.Frame.__init__(self, container)
        label = ttk.Label(self, text='Measurements in')
        self.option_value = StringVar()
        option_perntge = ttk.Radiobutton(
            self,
            text='Percentage',
            variable=self.option_value,
            value='percentage',
            width=10,
            command=lambda: callback(self.option_value.get())
        )
        option_pixel = ttk.Radiobutton(
            self,
            text='Pixels',
            variable=self.option_value,
            value='pixel',
            width=5,
            command=lambda: callback(self.option_value.get())
        )
        self.option_value.set('percentage')

        label.grid(row=0, column=0)
        option_perntge.grid(row=0, column=1)
        option_pixel.grid(row=0, column=2)

    def get_value(self):
        return self.option_value.get()


class SizeWidget(ttk.Frame):
    def __init__(self, container):
        ttk.Frame.__init__(self, container)
        label_height = ttk.Label(self, text='Height')
        label_height_px = ttk.Label(self, text='px')
        self.entry_height = ttk.Entry(self, width=5)
        label_width = ttk.Label(self, text='Width')
        label_width_px = ttk.Label(self, text='px')
        self.entry_width = ttk.Entry(self, width=5)

        label_height.grid(row=0, column=0, sticky=W)
        self.entry_height.grid(row=0, column=1, sticky=W)
        label_height_px.grid(row=0, column=2, sticky=W)
        label_width.grid(row=1, column=0, sticky=W)
        self.entry_width.grid(row=1, column=1, sticky=W)
        label_width_px.grid(row=1, column=2, sticky=W)

    def get_value(self):
        return self.entry_width.get(), self.entry_height.get()


class PercentageWidget(ttk.Frame):
    def __init__(self, container):
        ttk.Frame.__init__(self, container)
        self.entry = ttk.Entry(self, width=3)
        self.label = ttk.Label(self, text='%')
        self.entry.grid(row=0, column=0)
        self.label.grid(row=0, column=1)

    def get_value(self):
        return self.entry.get()
