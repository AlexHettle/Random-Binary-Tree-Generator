from tkinter import *
import random
#Function used when program is opened to create a full Binary tree
def starting_node(x,y,xdifference):
    if y<=300:
        the_canvas.create_oval(x,y,x+10,y+10,fill="green",outline="")
        newy=y+50
        newx=x-xdifference
        if y+50<=300:
            the_canvas.create_line(x+5,y+5,newx+5,newy+5,fill="green")
        starting_node(newx,newy,xdifference/2)
        newx=x+xdifference
        if y+50<=300:
            the_canvas.create_line(x+5,y+5,newx+5,newy+5,fill="green")
        starting_node(newx,newy,xdifference/2)
#function used to create a new randomly generated binary tree.
#throughout its creation each node is randomly chosen to either have a left
#child, a right child, or both.
def make_node(choice,x,y,xdifference):
    if y<=300:
        the_canvas.create_oval(x,y,x+10,y+10,fill="green")
        if(choice==1):
            newx=x-xdifference
            newy=y+50
            if y+50<=300:
                the_canvas.create_line(x+5,y+5,newx+5,newy+5,fill="green")
            make_node(random.randint(1,4),newx,newy,xdifference/2)
        if(choice==2):
            newx=x+xdifference
            newy=y+50
            if y+50<=300:
                the_canvas.create_line(x+5,y+5,newx+5,newy+5,fill="green")
            make_node(random.randint(1,4),newx,newy,xdifference/2)
        if(choice==3):
            newx=x-xdifference
            newy=y+50
            if y+50<=300:
                the_canvas.create_line(x+5,y+5,newx+5,newy+5,fill="green")
            make_node(random.randint(1,4),newx,newy,xdifference/2)
            newx=x+xdifference
            if y+50<=300:
                the_canvas.create_line(x+5,y+5,newx+5,newy+5,fill="green")
            make_node(random.randint(1,4),newx,newy,xdifference/2)
#A function called everytime the generate button is pressed.
#clears the screen and makes a new randomly generated binary Tree
#by calling make_node
def create_binary_tree():
    the_canvas.create_rectangle(-5,-5,505,375,fill="white")
    the_canvas.create_rectangle(-1,-1,5501,70,outline="",fill="#5f5f5f")
    the_canvas.create_rectangle(-1,-1,20,371,outline="",fill="#5f5f5f")
    the_canvas.create_rectangle(480,-1,501,371,outline="",fill="#5f5f5f")
    the_canvas.create_rectangle(0,301,501,371,outline="",fill="#5f5f5f")
    make_node(3,240,80,100)
#This chunk of code sets up the gui
window=Tk()
window.title("Binary-Tree-Generator")
window.geometry("500x370")
window.resizable(False, False)
the_canvas=Canvas(window,width=500,height=500, highlightthickness=0,bg="white")
the_button=Button(text="GENERATE",font=("fixedsys",20),command=create_binary_tree)
the_button.pack(side=BOTTOM)
the_canvas.place(x=0,y=0)
title_label=Label(text="Binary-Tree-Generator",font=("fixedsys",30),bg="#5f5f5f",fg="white")
title_label.pack(side=TOP)
the_canvas.create_rectangle(-1,-1,5501,70,outline="",fill="#5f5f5f")
the_canvas.create_rectangle(-1,-1,20,371,outline="",fill="#5f5f5f")
the_canvas.create_rectangle(480,-1,501,371,outline="",fill="#5f5f5f")
the_canvas.create_rectangle(0,301,501,371,outline="",fill="#5f5f5f")
starting_node(240,80,100)
window.mainloop()
