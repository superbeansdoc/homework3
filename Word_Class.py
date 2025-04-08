import tkinter as tk
import random
class word:
    def __init__(self,text,speed,x_postion):
        self.text = text
        self.speed = speed
        self.x_postion = x_postion
    def display(self):
        print(self.text)
        print(self.speed)
        print(self.x_postion)

the_word = word("hi",20,20) 
the_word.display()