# -*- coding: utf-8 -*-

"""
Created: 2022/08/25
Version: 2022/08/26
@AP: Wei
"""
import tkinter as tk

root_window = tk.Tk()
root_window.geometry("550x400")
root_window.title("Pdf operater")


output_path_label  = tk.Label(root_window, text = "Choose output path")
output_path_entry  = tk.Entry(root_window)
output_path_buttom  = tk.Button(root_window, text = "Open", commend=choose_dir)
choose_file_label  = tk.Label(root_window, text = "Choose file")
choose_file_entry  = tk.Entry(root_window)
choose_file_buttom  = tk.Button(root_window, text = "Open", commend=choose_file)
file_list_text = tk.Text()
file_add_buttom  = tk.Button(root_window, text = "Add file", commend=file_add)
file_clear_buttom  = tk.Button(root_window, text = "Add file", commend=file_clear)

file_list = []
def choose_dir():
    dirname = tk.filedialog.askdirectory(title = "Select a directory")
    output_path_entry.insert(0, dirname)

def choose_file():
    filename = tk.filedialog.askopenfilename(
        title = "Select a File",
        filetypes = (("PDF files", "*.pdf*"), ("all files", "*.*"))
        )
    choose_file_entry.insert(0, filename)

def file_add():
    file_list_text.insert(END, filename + "\n")
    file_list.apped(filename)

def file_clear():
    file_list_text.delete('1.0', END)
    file_list = []

def file_merge():
    # Read it and merge it
    file_len = len(file_list)
    new_file = PdfFileWriter()
    for i_file in range(file_len):
        old_file = PdfFileReader(file_list[i_file])
        file_pages_n = old_file.getNumPages()
        for i_page in range(file_pages_n):
            new_file.addPage(old_file.getPage(i_page))

    with open(f"{dirname}/output.pdf", "wb") as f:
        new_file.write(f)
    
    print(f"Export to '{dirname}/output.pdf'")

      
root_window.mainloop() 


