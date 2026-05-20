import tkinter as tk

window = tk.Tk()
window.title("My Calculator")
window.geometry("400x600")
window.config(bg="#1a1a2e")

screen = tk.Entry(
    window,
    width=20,
    font=("Arial", 28, "bold"),
    bg="#16213e",
    fg="white",
    bd=0,
    justify="right"
)
screen.grid(row=0, column=0, columnspan=4, padx=20, pady=30)

def button_click(value):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, current + str(value))

def clear():
    screen.delete(0, tk.END)

def calculate():
    try:
        result = eval(screen.get())
        screen.delete(0, tk.END)
        screen.insert(0, str(result))
    except:
        screen.delete(0, tk.END)
        screen.insert(0, "Error")

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "",  "",  ""],
]

for row_index, row in enumerate(buttons):
    for col_index, button_text in enumerate(row):

        if button_text == "":
            continue

        if button_text == "=":
            bg_color = "#e94560"
        elif button_text == "C":
            bg_color = "#e94560"
        elif button_text in ["+", "-", "*", "/"]:
            bg_color = "#0f3460"
        else:
            bg_color = "#16213e"

        if button_text == "=":
            cmd = calculate
        elif button_text == "C":
            cmd = clear
        else:
            cmd = lambda x=button_text: button_click(x)

        btn = tk.Button(
            window,
            text=button_text,
            font=("Arial", 20, "bold"),
            bg=bg_color,
            fg="white",
            activebackground="#e94560",
            activeforeground="white",
            width=5,
            height=2,
            bd=0,
            cursor="hand2",
            command=cmd
        )

        btn.grid(
            row=row_index + 1,
            column=col_index,
            padx=5,
            pady=5
        )

window.mainloop()