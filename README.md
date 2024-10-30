# maze_solver

This is a simple program to build and solve a maze using ***python*** and ***Tkinter***

This is part of the [boot.dev](https://boot.dev) trainig and is a semi guided project on their site.

1. Make sure ***python3*** and ***Tkiner*** are installed
2. Connect to your GitHub repository, using `git clone <*repository url*>`
3. Created `Window` class in ***graphics.py***
    1. Constructor takes in width and height
    2. Creates a root widget using `Tk()`
    3. Hardcodes the `title` property for the `Window`
    4. Creates and packs a `Canvas` for the `Window` where the maze will be drawn
    5. Created a `redraw()` function for the `Window` to tell the system when to draw it
    6. Created a `wait_for_close()` functionthat will redraw the `Window` as long as it is running
    7. Created a `close()` function that tells the `wait_for_close()` function to stop redrawing
4. Create `main()` function to test and execute `maze_solver`
5. Created `Point` class in ***graphics.py***
    1. `Point` is a simple point on the `Window` storing an x- and y-coordinate
    2. Constructor takes in x-coordinate and y-coordinate of the `Point`
6. Created `Line` class in ***graphics.py***
    1. `Line` is a black line connecting two `Points` with width of 2
    2. Contructor takes in two `Points`
    3. Created `draw()` function to draw a line connection the two points
        1. Function takes in a `Canvas` and `fill_color` for the `Line`
            1. The `fill_color` defaults to ***black***
        2. Uses the `Canvas.create_line()` function to draw a black line
7. Tested the `Point` and `Line` classes by adding a few lines to the `Window`
8. Created `Cell` class in ***cell.py***
    1. A maze is just a series of connected `Cells`, with some side existing and others not
    2. Constructor takes the `Window` where it will be drawn
    3. Stores `boolean` value for each side defining if it exists or not, default to `True`
    4. Stores coordinates for two `Points`, top left and bottom right, deafault to `None`
    5. Added `draw()` method that takes in coordinates for the two `Points` used for drawing the `Cell`
9. Tested `Cell` by adding several `Cells` to `Window` with some sides missing
10. Added `draw_move()` function to `Cell`
    1. Function takes in a `to_cell` and `undo` status
        1. `undo` defaults to `False`
    2. Function draws a `Line` from the center of `self` to center of `to_cell`
    3. `Line` is ***red*** if `undo == False`, otherwise it is ***gray***
11. Tested `draw_move` by adding samples to `main()`
12. Created `Maze` class in ***maze.py***
    1. Constructor takes in following inputs:
        1. x1 - starting x-coordinate of `Maze` - top side of `Maze`
        2. y1 - starting y-coordinate of `Maze` - left side of `Maze`
        3. num_rows - how many rows are in the `Maze`
        4. num_columns - how many columns are in the `Maze`
        5. cell_size_x - width of each `Cell`
        6. cell_size_y - height of each `Cell`
        7. win - `Window` where `Maze` will be drawn
    2. `_create_cells()` function:
        1. Creates a `List` (`self._cells`) of `Cells` for the maze.
        2. The `List` contains a `List` representing each column of `Cells`
        3. Calls `_draw_cells(i, j)` on each `Cell` in `self._cells`
    3. `_draw_cells(i, j)` function:
        1. Calculates the x/y position of the `Cell` using inputs, `cell_size`, and x/y postion of the `Maze`
        2. Draw `Cell` at calculate x/y positions
        3. Call `_animate()` function
    4. `_animate()` function:
        1. Call `self._win.redraw()`
        2. Sleep for short period of time
13. ***tests.py*** used to perform unit testing on the `Maze`
    1. Imported `unittest` to ***tests.py***
    2. Created tests to test `Mazes` of different sizes
14. `Maze` updated to set start `Cell` and end `Cell`
    1. Created `_break_entrance_and_exit()` function
    2. Function draws any wall with exists value equal to `False` white
15. Updating `Maze` to break walls to make complete `Maze`
    1. `_break_walls_r(i, j)` function added
    2. Fuction randomly moves from `Cell` to `Cell` to remove random walls and create the `Maze`
    3. Reset `visited` to `False`
