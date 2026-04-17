import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My First Window")
window.geometry("400x300")  # width x height

# Add a label
label = tk.Label(window, text="Hello from Ubuntu!")
label.pack(pady=20)

# Add a button
def on_click():
    label.config(text="Button clicked!")

button = tk.Button(window, text="Click Me", command=on_click)
button.pack()

# Run the window
window.mainloop()