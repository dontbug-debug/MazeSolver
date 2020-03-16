# using tkinter to show how the maze is being solved

import tkinter as tk
from tkinter import *
import time as time


# def create_maze(height, width , canvas):
#     """
#     creats n number of rectangles in the canvas
#
#     :param n: a postive number
#             canvas: the canvas on which the rectangle needs to be drawn
#     :return:
#     """
#
#



class draw_maze(Frame):

    def __init__(self, maze, path, startPoint, endPoint):
        super().__init__()
        self.Maze = maze
        self.Path = path
        self.sp = startPoint
        self.ep = endPoint
        self.create_maze()

    def create_maze(self):

        self.master.title("Maze Solver")

        canvas = Canvas(bg = 'black')
        maze_height = len(self.Maze)
        maze_width = len(self.Maze[0])

        rectangle_height = 75
        rectangle_width = 75


        # draw the maze
        for h in range(0, maze_height):
            for w in range(0, maze_width):
               if self.Maze[h][w] == 1:
                   canvas.create_rectangle(w * rectangle_width, h * rectangle_height, (w + 1) * rectangle_width,
                                          (h + 1) * rectangle_height, outline='grey', width=0.0)
               elif self.Maze[h][w] == 0:

                   canvas.create_rectangle(w * rectangle_width, h * rectangle_height, (w + 1) * rectangle_width,
                                           (h + 1) * rectangle_height, fill= 'grey', outline='black', width=0.0)

               if (h,w)== self.sp:
                   canvas.create_oval(w * rectangle_height, h * rectangle_width, (w + 1) * rectangle_height,
                                      (h + 1) * rectangle_width, fill="green", width=0.0)
               if (h,w)== self.ep:
                   canvas.create_oval(w * rectangle_height, h * rectangle_width, (w + 1) * rectangle_height,
                                      (h + 1) * rectangle_width, fill="green", width=0.0)

               if self.Path[h][w] == "P":
                   canvas.create_oval(w * rectangle_height, h * rectangle_width, (w + 1) * rectangle_height,
                                      (h + 1) * rectangle_width, fill="red", width=0.0)

        canvas.pack(fill=BOTH, expand=1)

class call:


    def __init__(self, maze, path,startPoint, endPoint):
        self.Maze = maze
        self.Path = path
        self.sp = startPoint
        self.ep = endPoint
        self.draw_maze()

    def draw_maze(self):
        root = Tk()
        Height = len(self.Maze)
        Width = len(self.Maze[0])
        draw_maze(self.Maze, self.Path, self.sp, self.ep)
        root.config(bg='black')
        root.minsize(height=Height*75 , width=Width*75)
        root.maxsize(height=Height*75 , width=Width*75)
        root.geometry(("%dx%d")%(Width*75, Height*75))
        root.mainloop()
