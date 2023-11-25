import tkinter as tk
import pyautogui

class RunawayDialog:
    def __init__(self, root):
        self.root = root
        self.root.title("Runaway Dialog")
        self.root.geometry("300x100")

        self.label = tk.Label(root, text="Try to close me!")
        self.label.pack(pady=20)

        self.root.bind("<Delete>", self.close_dialog)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.move_away()

    def move_away(self):
        screen_width, screen_height = pyautogui.size()
        dialog_width, dialog_height = 300, 100

        # Get the initial position of the dialog
        x, y = (screen_width - dialog_width) // 2, (screen_height - dialog_height) // 2

        # Move the dialog away from the mouse cursor
        while True:
            cursor_x, cursor_y = pyautogui.position()
            if cursor_x == x and cursor_y == y:
                continue  # Avoid infinite loop if the dialog is already at the cursor position

            x_direction = 1 if cursor_x > x else -1
            y_direction = 1 if cursor_y > y else -1

            x += x_direction
            y += y_direction

            self.root.geometry(f"300x100+{x}+{y}")
            self.root.update()

    def close_dialog(self, event):
        self.root.destroy()

    def on_close(self):
        pass  # Prevent closing by clicking the close button

if __name__ == "__main__":
    root = tk.Tk()
    dialog = RunawayDialog(root)
    root.mainloop()
