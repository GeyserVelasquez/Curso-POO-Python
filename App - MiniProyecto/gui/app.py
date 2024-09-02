import tkinter as tk
from db import DataBase
from .menu import *

class App(tk.Tk):

    frameActivo = None

    bdd = DataBase()

    sideBar= None

    header = None

    # main = None

    def __init__(self,width,height):
        super().__init__()
        self.settings(width,height)

    def run(self):
        self.mainloop()

    def settings(self,vWidth,vHeight):
        self.title("Holick Inventario")
        menubar = MenuBar(self)
        self.config(menu=menubar, width=vWidth, height=vHeight)
        self.resizable(True,True )
        self.pack_propagate(False)
