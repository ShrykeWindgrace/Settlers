from tkinter import (Tk,
                     Menu,
                     IntVar,
                     BooleanVar,
                     # StringVar,
                     # Toplevel,
                     N,
                     S,
                     # W,
                     # E,
                     # END,
                     filedialog,
                     messagebox,
                     )
from tkinter.ttk import (Frame,
                         Button,
                         Label,
                         Radiobutton,
                         # Entry,
                         )
from pydispatch import dispatcher


class GUI():
    def __init__(self):
        self.root = Tk()

        self.settle_frame = Frame(self.root)
        self.new_expense_frame = Frame(self.root)
        self.users_frame = Frame(self.root)

        self.settle_frame.grid(row=10, column=30)
        self.new_expense_frame.grid(row=10, column=20)
        self.users_frame.grid(row=10, column=10)

    def start(self):
        self.root.mainloop()

    def stop(self):
        self.root.quit()

