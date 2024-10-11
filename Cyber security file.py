import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad")
        self.root.geometry("800x600")

        # Membuat area teks
        self.text_area = tk.Text(self.root, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Membuat menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Membuat menu file
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        # Membuat menu edit
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)

    def new_file(self):
        """Membersihkan teks area untuk membuat file baru"""
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        """Membuka file teks"""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        """Menyimpan file teks"""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def save_as_file(self):
        """Menyimpan file teks dengan nama baru"""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def exit_app(self):
        """Menutup aplikasi"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()

    def cut(self):
        """Memotong teks yang dipilih"""
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        """Menyalin teks yang dipilih"""
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        """Menempelkan teks dari clipboard"""
        self.text_area.event_generate("<<Paste>>")

# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()