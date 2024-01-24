# Algorithm cource final project 

Table of content 
1. [Linked lists](#1-linked-lists)
2. [Build Pythagoras Tree using recursion](#2-build-pythagoras-tree-using-recursion)
3. [Dijkstra with heap](#3-dijkstra-with-heap)
4. [Heap visualisation](#4-heap-visualisation)

## 1. Linked lists

Added following fucnctions:
* Reverce linked list, [link](01/linked_list.py#L65)
* Sort list (incertion sort), [link](01/linked_list.py#L75)
* Merge and sort linked lists, [link](01/linked_list.py#L85)

Tests can be found [here](01/tests.py)

## 2. Build Pythagoras Tree using recursion

Code on [02/pythagoras_tree.py](02/pythagoras_tree.py) draws fractal Pythagoras Tree using Turtle lib. 

User has ability to set complexity of drowing using command line prompt. 

### Requirements

Python 3, below 3.9.

### Usage

Launch:
```
python3 02/pythagoras_tree.py
```
Set complexity of drawing for start.

Exit: by clossing Python GUI window or by keyboard interruption (Ctrl+C).

## 3. Dijkstra with heap

Added [Dijkstra algorithm](03/dijkstra_with_heap.py) that uses heap for calculations.  

## 4. Heap visualisation 

Code on [04/heap.py](04/heap.py) uses functions from example for visualization heap and [this functions](04/heap.py#L53-L70) for converting provided list to heap and prepare it for usage on visualization functions.   

## 5. DFS & BFS visualisation

Added opportunity for visualisation DFS and BFS for binary trees.
* [DFS](05/dfs.py)
* [BFS](05/bfs.py)

Node colors are changed using node order returned by DFS or BFS respectively. Colors are changed using RGB tuples generated on [comprehension](05/draw_methods.py#L53) 
```
step = 0.8 / len(data)
{element: (0.8, step * index, step * index) for index, element in enumerate(data)}  
```
