import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import os
import sys

def run_batch_file(fps_value):
    batch_file_path = os.path.join(dependencies_folder, f"fpsUnlock{fps_value}.bat")
    if os.path.exists(batch_file_path):
        try:
            subprocess.run([batch_file_path], check=True)
            messagebox.showinfo("Success", f"FPS changed to {fps_value} successfully.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to change FPS to {fps_value}.\n{e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    else:
        messagebox.showerror("Error", f"Batch file 'fpsUnlock_{fps_value}.bat' not found in the dependencies folder.")

def main():
    global dependencies_folder
    if getattr(sys, 'frozen', False):
        base_path = sys.executable
    else:
        base_path = os.path.abspath(__file__)

    dependencies_folder = os.path.join(os.path.dirname(base_path), 'dependencies')

    root = tk.Tk()
    root.title("WW FPS Unlocker")
    
    icon_path = os.path.join(dependencies_folder, 'ww.ico')
    if os.path.exists(icon_path):
        try:
            root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Error setting icon: {e}")
            messagebox.showerror("Error", f"Failed to set icon: {e}")
    else:
        print("Icon file 'ww.ico' not found.")
        messagebox.showerror("Error", "Icon file 'ww.ico' not found in the dependencies folder.")
        return

    fps_limit_label = ttk.Label(root, text="Select your FPS/Monitor Refresh Rate Limit")
    fps_limit_label.grid(column=0, row=0, padx=10, pady=10, columnspan=3)  # Span across 3 columns

    fps_60_button = ttk.Button(root, text="FPS 60", command=lambda: run_batch_file(60))
    fps_60_button.grid(column=0, row=1, padx=10, pady=10)

    fps_90_button = ttk.Button(root, text="FPS 90", command=lambda: run_batch_file(90))
    fps_90_button.grid(column=1, row=1, padx=10, pady=10)

    fps_120_button = ttk.Button(root, text="FPS 120", command=lambda: run_batch_file(120))
    fps_120_button.grid(column=2, row=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()