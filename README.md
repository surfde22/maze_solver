# maze_solver

This is a simple program to build and solve a maze using python and Tkinter

This is part of the boot.dev trainig and is a semi guided project on their site.

- Make sure python3 and Tkiner are installed
- Connect to your GitHub repository, using `git clone <*repository url*>`
- Created a Window class that pops up a basic window with a white background
- Created classes for Point and Line
    - Point is a simple point on the Window storing an x- and y-coordinate
    - Line is a black line connecting two Points with width of 2
- Tested the Point and Line classes by adding a few lines to the window
- Created new class for Cell
- A maze is just a series of connected cell, with some side existing and others not
- Cell class takes in Window, where it will be drawn
- Stores boolean value for each side defining if it exists or not, default to True
- Stores coordinates for two Points, top left and bottom right, deafault to None
- Cell has draw method that takes in coordinates for the two points used in drawing the cell
- Tested cell by adding several Cells to Window with some sides missing
