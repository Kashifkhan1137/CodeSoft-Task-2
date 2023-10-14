import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.result_var = tk.StringVar()

        # Colors
        button_bg = '#e0e0e0'  # Light gray
        button_fg = 'black'
        button_active_bg = '#d0d0d0'  # Slightly darker gray
        entry_bg = 'white'
        entry_fg = 'black'

        # Create widgets with specified colors
        self.create_widgets(button_bg, button_fg, button_active_bg, entry_bg, entry_fg)

    def create_widgets(self, button_bg, button_fg, button_active_bg, entry_bg, entry_fg):
        entry = tk.Entry(self.master, textvariable=self.result_var, bd=10, insertwidth=1, font=("Arial", 24), justify="right",
                         bg=entry_bg, fg=entry_fg)
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.master, text=text, font=("Arial", 18), bg=button_bg, fg=button_fg,
                               activebackground=button_active_bg, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky='nsew')

        # Configure column and row weights
        for i in range(4):
            self.master.columnconfigure(i, weight=1)

        for i in range(5):
            self.master.rowconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            current_input = self.result_var.get()
            new_input = current_input + value
            self.result_var.set(new_input)

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

# Lets run this code for testing
