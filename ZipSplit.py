import os
import shutil
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

DEFAULT_SPLIT_SIZE_MB = 4650  # 4650 MB

class ZipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zip Splitter and Merger")

        self.split_size_label = tk.Label(root, text="Split size (MB):")
        self.split_size_label.pack()

        self.split_size_var = tk.StringVar()
        self.split_size_var.set(DEFAULT_SPLIT_SIZE_MB)

        self.split_size_entry = tk.Entry(root, textvariable=self.split_size_var)
        self.split_size_entry.pack()

        self.split_button = tk.Button(root, text="Split a ZIP file", command=self.split_zip)
        self.split_button.pack()

        self.merge_button = tk.Button(root, text="Merge ZIP parts", command=self.merge_parts)
        self.merge_button.pack()

        self.progress = tk.Label(root, text="")
        self.progress.pack()

    def split_zip(self):
        filename = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
        if not filename:
            return

        split_size_mb = self.split_size_var.get()
        try:
            split_size_mb = int(split_size_mb)
        except ValueError:
            messagebox.showerror("Error", "Invalid split size.")
            return

        split_size = split_size_mb * 1024 * 1024

        with open(filename, 'rb') as f:
            part_num = 1
            chunk = f.read(split_size)
            while chunk:
                part_filename = f"{filename}.{part_num}"
                with open(part_filename, 'wb') as f_part:
                    f_part.write(chunk)
                part_num += 1
                chunk = f.read(split_size)
        self.progress.config(text=f"Split into {part_num - 1} parts.")

    def merge_parts(self):
        filename = filedialog.askopenfilename()
        if not filename:
            return

        base = filename.rsplit('.', 1)[0]
        if not base.endswith('.zip'):
            messagebox.showerror("Error", "Not a part of a zip file.")
            return

        with open(base, 'wb') as f:
            part_num = 1
            while True:
                part_filename = f"{base}.{part_num}"
                if not os.path.isfile(part_filename):
                    break
                with open(part_filename, 'rb') as f_part:
                    shutil.copyfileobj(f_part, f)
                os.remove(part_filename)
                part_num += 1
        self.progress.config(text=f"Merged into {base}.")

root = tk.Tk()
app = ZipApp(root)
root.mainloop()
