# -*- coding: utf-8 -*-

"""
Created: 2022/08/25
Version: 2022/08/26
@AP: Wei
"""
import sys
sys.path.append('./fun')

from merge import merge

def main():

    ask_text_beg = '''
    A. Merge
    B. Devide
    C. Rotate
    Q. Close the windows
    Choose operation: '''
    ask_text_end = "Choose operation(press 'LIST' to show list again.):"

    show_list = True
    while True:
        # Ask
        if show_list:
            operation = input(ask_text_beg).upper()
            show_list = False
        else:
            operation = input(ask_text_end).upper()
        # Do some work by choose
        if operation == "Q":
            print("close it!")
            break
        elif operation == "A":
            merge()
            pass
        elif operation == "B":
            print("do ./fun/devide.py")
            pass
        elif operation == "C":
            print("do ./fun/rotate.py")
            pass
        elif operation == "LIST":
            show_list = True
            continue
        else:
            print("There is no operation '%s' in the list." % operation)
            show_list = True
        
        print("-" * 10)
    
    
if __name__ == "__main__":
    main()
    




