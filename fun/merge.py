# -*- coding: utf-8 -*-

"""
Created: 2022/08/25
Version: 2022/08/26
@AP: Wei
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
# from tkiner import tk

def merge():

    print("")
    # Choose files
    file_n = int(input("How many files you want to convert? "))
    file_list = []
    for i_file in range(file_n):
        path = input("Path %s :" % str(i_file + 1))
        file_list.append(path)

    # Read it and merge it
    output_name = input("Output file's name(*.pdf):")
    new_file = PdfFileWriter()
    for i_file in range(file_n):
        old_file = PdfFileReader(file_list[i_file])
        file_pages_n = old_file.getNumPages()
        for i_page in range(file_pages_n):
            new_file.addPage(old_file.getPage(i_page))

    with open(f"./output/{output_name}.pdf", "wb") as f:
        new_file.write(f)
    
    print(f"Export to './output/{output_name}.pdf'")


if __name__ == "__main__":
    merge()

    