#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import tkinter as tk
from tkinter import filedialog as fd
import PyPDF2 
import os
 
def choose_file():
    file_path_list = fd.askopenfilenames(title='Choose files', initialdir=os.getcwd())
    file_path_list = list(file_path_list)
    file_path_list.sort()
    file_path_list = '|'.join(file_path_list)
    input_entry.insert('0', file_path_list)
    # return list(file_path_list)
 
def choose_dir():
    dir_path = fd.askdirectory(title='Choose directory', initialdir=os.getcwd())
    output_entry.insert('0', dir_path)
    # return dir_path
 
# def load_file(file_path):
#     data = PyPDF2.PdfFileReader(file_path, 'rb')
#     return data
 
def process(file_path_list):
    data_list = PyPDF2.PdfMerger()
    for file_path in file_path_list:
        # read data and add column of grouping tag
        data_list.append(PyPDF2.PdfReader(file_path, 'rb'))
    return data_list
 
def save_file(data_list, output_dir):
    data_list.write(f'{output_dir}/NewMergedFile.pdf')
 
def main():
    file_path_list = input_entry.get()
    file_path_list = file_path_list.split("|")
    output_dir = output_entry.get()
    data_list = process(file_path_list)
    save_file(data_list, output_dir)
    tk.messagebox.showinfo(title = 'Done!', message = "OK")
 
 
# GUI
# Basic window
root_window = tk.Tk()
root_window.geometry("650x130")
root_window.resizable(False, False)
# root_window.resizable(True, True)
root_window.title("PDF Processer")
 
# Some function
input_label = tk.Label(root_window, text='List files:')
input_label.grid(row=0, column=0)
input_entry = tk.Entry(root_window, width=50)
input_entry.grid(row=0, column=1)
 
output_label = tk.Label(root_window, text='Output path:')
output_label.grid(row=1, column=0)
output_entry = tk.Entry(root_window, width=50)
output_entry.grid(row=1, column=1)
 
choose_file_button = tk.Button(root_window, text='Choose lists', command=choose_file)
choose_file_button.grid(row=0, column=3)
 
choose_dir_button = tk.Button(root_window, text='Choose directory', command=choose_dir)
choose_dir_button.grid(row=1, column=3)
 
    
start_button = tk.Button(root_window, text="Merge it", command=main)
start_button.grid(row=2, column=0, columnspan=2)
close_button = tk.Button(root_window, text="Close the window", command=root_window.quit)
close_button.grid(row=3, column=0, columnspan=2)
 
# Run it
root_window.mainloop()
 