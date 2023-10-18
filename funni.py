import tkinter as tk
import random

def move_away(event):
    # Get the current position of the window
    x, y = root.winfo_x(), root.winfo_y()
    
    # Calculate the new position, making sure the window stays on the screen
    new_x = max(0, min(root.winfo_screenwidth() - root.winfo_width(), x + random.randint(-50, 50)))
    new_y = max(0, min(root.winfo_screenheight() - root.winfo_height(), y + random.randint(-50, 50)))
    
    # Move the window to the new position
    root.geometry(f"+{new_x}+{new_y}")

def close_window(event):
    root.destroy()

root = tk.Tk()
root.title("XD")
root.protocol("WM_DELETE_WINDOW", close_window)

# Create a label with the close button
label = tk.Label(root, text="Move the mouse near the close button", font=("Arial", 14))
label.pack(pady=20)

# Bind the mouse enter event to move_away function
label.bind("<Enter>", move_away)

root.mainloop()