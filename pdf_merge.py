#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import tkinter as tk
from tkinter import filedialog as fd
import PyPDF2
import os
 
 
def choose_file_1():
    file_path = fd.askopenfilename(title='Choose file 5', initialdir=os.getcwd())
    input_entry_1.delete(0, tk.END)
    input_entry_1.insert('0', file_path)
 
def choose_file_2():
    file_path = fd.askopenfilename(title='Choose file 5', initialdir=os.getcwd())
    input_entry_2.delete(0, tk.END)
    input_entry_2.insert('0', file_path)
 
def choose_file_3():
    file_path = fd.askopenfilename(title='Choose file 5', initialdir=os.getcwd())
    input_entry_3.delete(0, tk.END)
    input_entry_3.insert('0', file_path)
 
def choose_file_4():
    file_path = fd.askopenfilename(title='Choose file 5', initialdir=os.getcwd())
    input_entry_4.delete(0, tk.END)
    input_entry_4.insert('0', file_path)
 
def choose_file_5():
    file_path = fd.askopenfilename(title='Choose file 5', initialdir=os.getcwd())
    input_entry_5.delete(0, tk.END)
    input_entry_5.insert('0', file_path)
 
def clear_file():
    input_entry_1.delete(0, tk.END)
    input_entry_2.delete(0, tk.END)
    input_entry_3.delete(0, tk.END)
    input_entry_4.delete(0, tk.END)
    input_entry_5.delete(0, tk.END)
   
 
def choose_dir():
    dir_path = fd.askdirectory(title='Choose directory', initialdir=os.getcwd())
    output_entry.delete(0, tk.END)
    output_entry.insert('0', dir_path)
    # return dir_path
 
def process(file_path_list):
    data_list = PyPDF2.PdfMerger()
    for file_path in file_path_list:
        # read data and add column of grouping tag
        data_list.append(PyPDF2.PdfReader(file_path, 'rb'))
    return data_list
 
def save_file(data_list, output_dir, output_file_name):
    print(f'{output_dir}/{output_file_name}.pdf')
    data_list.write(f'{output_dir}/{output_file_name}.pdf')
 
def main():
    file_path_list = [""] * 5
    file_path_list[0] = input_entry_1.get()
    file_path_list[1] = input_entry_2.get()
    file_path_list[2] = input_entry_3.get()
    file_path_list[3] = input_entry_4.get()
    file_path_list[4] = input_entry_5.get()
    file_path_list = [file for file in file_path_list if file != '']
    output_dir = output_entry.get()
    output_file_name = output_file_name_entry.get()
    #print(file_path_list)
    data_list = process(file_path_list)
    save_file(data_list, output_dir, output_file_name)
    tk.messagebox.showinfo(title = 'Done!', message = "OK")
 
 
# GUI
# Basic window
root_window = tk.Tk()
root_window.geometry("680x290")
root_window.resizable(False, False)
# root_window.resizable(True, True)
root_window.title("PDF Merge")
 
# Some function
input_label_1 = tk.Label(root_window, text='File 1:')
input_label_1.grid(row=0, column=0)
input_entry_1 = tk.Entry(root_window, width=50)
input_entry_1.grid(row=0, column=1)
choose_file_button_1 = tk.Button(root_window, text='Choose File', command=choose_file_1)
choose_file_button_1.grid(row=0, column=2)
 
input_label_2 = tk.Label(root_window, text='File 2:')
input_label_2.grid(row=1, column=0)
input_entry_2 = tk.Entry(root_window, width=50)
input_entry_2.grid(row=1, column=1)
choose_file_button_2 = tk.Button(root_window, text='Choose File', command=choose_file_2)
choose_file_button_2.grid(row=1, column=2)
 
input_label_3 = tk.Label(root_window, text='File 3:')
input_label_3.grid(row=2, column=0)
input_entry_3 = tk.Entry(root_window, width=50)
input_entry_3.grid(row=2, column=1)
choose_file_button_3 = tk.Button(root_window, text='Choose File', command=choose_file_3)
choose_file_button_3.grid(row=2, column=2)
 
input_label_4 = tk.Label(root_window, text='File 4:')
input_label_4.grid(row=3, column=0)
input_entry_4 = tk.Entry(root_window, width=50)
input_entry_4.grid(row=3, column=1)
choose_file_button_4 = tk.Button(root_window, text='Choose File', command=choose_file_4)
choose_file_button_4.grid(row=3, column=2)
 
input_label_5 = tk.Label(root_window, text='File 5:')
input_label_5.grid(row=4, column=0)
input_entry_5 = tk.Entry(root_window, width=50)
input_entry_5.grid(row=4, column=1)
choose_file_button_5 = tk.Button(root_window, text='Choose File', command=choose_file_5)
choose_file_button_5.grid(row=4, column=2)
 
clear_button = tk.Button(root_window, text="Clear all file", command=clear_file)
clear_button.grid(row=5, column=0, columnspan=2)
 
output_label = tk.Label(root_window, text='Output path:')
output_label.grid(row=6, column=0)
output_entry = tk.Entry(root_window, width=50)
output_entry.grid(row=6, column=1)
choose_dir_button = tk.Button(root_window, text='Choose directory', command=choose_dir)
choose_dir_button.grid(row=6, column=2)
 
output_file_name_label = tk.Label(root_window, text='Output file name:')
output_file_name_label.grid(row=7, column=0)
output_file_name_entry = tk.Entry(root_window, width=50)
output_file_name_entry.insert(0, 'NewMergedFile')
output_file_name_entry.grid(row=7, column=1)
output_file_name_label = tk.Label(root_window, text='.pdf')
output_file_name_label.grid(row=7, column=2)
 
start_button = tk.Button(root_window, text="Merge it", command=main)
start_button.grid(row=8, column=0, columnspan=2)
 
empty_label = tk.Label(root_window, text='  ')
empty_label.grid(row=9, column=0)
 
close_button = tk.Button(root_window, text="Close the window", command=root_window.quit)
close_button.grid(row=10, column=0, columnspan=2)
 
# Run it
root_window.mainloop()
 
 