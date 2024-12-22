from tkinter import filedialog
from tkinter import *


def directorySelector():
    root = Tk()
    root.withdraw()
    custom_nodes_path = filedialog.askdirectory()
    print(custom_nodes_path)