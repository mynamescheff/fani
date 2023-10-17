import tkinter as tk
import random

class MovingPopupWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Popup Window")
        self.root.geometry("200x100")
        self.label = tk.Label(root, text="Move your mouse close to the 'Close' button!")
        self.label.pack(padx=20, pady=20)
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.root.bind("<Motion>", self.move_away)

    def move_away(self, event):
        x, y = event.x, event.y
        new_x = random.randint(0, self.root.winfo_screenwidth() - 200)
        new_y = random.randint(0, self.root.winfo_screenheight() - 100)
        self.root.geometry(f"200x100+{new_x}+{new_y}")

    def close_window(self):
        self.root.destroy()

root = tk.Tk()
popup = MovingPopupWindow(root)
root.mainloop()
