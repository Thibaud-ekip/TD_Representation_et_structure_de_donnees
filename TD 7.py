from math import *
from tkinter import *
from random import *
import numpy as np

fenetre = Tk()
fenetre.geometry("500x500")
can = Canvas(fenetre, width = 500, height = 500, bg = 'white')
can.pack()

graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]

pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])

COLOR = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']

col_index = [i for i in range(12)]



def draw(can, graph, pos, col_index):
    N = len(graph)
    for e in can.find_all():
        can.delete(e)
    for i in range(N):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for i in range(N):
        x, y = pos[i]
        can.create_oval(x-6, y-6, x+6, y+6, fill=COLOR[col_index[i]])
        can.create_text(x-12,y,text=f"{i}")


def min_local(i,graph):
    global col_index
    min = col_index[i]
    for j in graph[i]:
        if col_index[j] < min :
            min = col_index[j]
    col_index[i] = min
    for j in graph[i]:
        col_index[j] = min


def comp_connexes(graph,pos,col_index):
    N = len(graph)
    for i in range(N):
        min_local(i,graph)
    draw(can,graph,pos,col_index)


comp_connexes(graph,pos,col_index)


fenetre.bind("<f>",affichage)
fenetre.mainloop()

