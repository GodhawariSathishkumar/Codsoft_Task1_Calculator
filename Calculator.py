import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if current == "Error":
        clear_display()
        current = ""
    if symbol == "C":
        clear_display()
    elif symbol == "=":
        try:
            result = eval(current)
            display_var.set(str(result))
        except Exception:
            display_var.set("Error")
    else:
        display_var.set(current + symbol)

def clear_display():
    display_var.set("")

root = tk.Tk()
root.title("Calculator")

button_bg = "#f0f0f0"
button_fg = "#000000"
button_active_bg = "#d9d9d9"
display_bg = "#ffffff"
display_fg = "#000000"
font_display = ("Arial", 18)
font_buttons = ("Arial", 14)

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=font_display, bd=10, insertwidth=4,
                   width=14, justify="right", bg=display_bg, fg=display_fg)
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for i in range(4):
    for j in range(4):
        btn = tk.Button(root, text=buttons[i][j], font=font_buttons, padx=20, pady=20,
                        bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                        relief="raised", command=lambda symbol=buttons[i][j]: button_click(symbol))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()
