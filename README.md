# maze_solver

This is a simple program to build and solve a maze using ***python*** and ***Tkinter***

This is part of the [boot.dev](https://boot.dev) trainig and is a semi guided project on their site.

1. Make sure ***python3*** and ***Tkiner*** are installed
2. Connect to your GitHub repository, using `git clone <*repository url*>`
3. Created a `Window` class
    1. Constructor takes in width and height
    2. Creates a root widget using `Tk()`
    3. Hardcodes the `title` property for the `Window`
    4. Creates and packs a `Canvas` for the `Window` where the maze will be drawn
    5. Created a `redraw()` function for the `Window` to tell the system when to draw it
    6. Created a `wait_for_close()` functionthat will redraw the `Window` as long as it is running
    7. Created a `close()` function that tells the `wait_for_close()` function to stop redrawing
4. Create `main()` function to test and execute `maze_solver`
5. Created `Point` class
    1. `Point` is a simple point on the `Window` storing an x- and y-coordinate
    2. Constructor takes in x-coordinate and y-coordinate of the `Point`
6. Created `Line` class
    1. `Line` is a black line connecting two `Points` with width of 2
    2. Contructor takes in two `Points`
    3. Created `draw()` function to draw a line connection the two points
        1. Function takes in a `Canvas` and `fill_color` for the `Line`
            1. The `fill_color` defaults to ***black***
        2. Uses the `Canvas.create_line()` function to draw a black line
7. Tested the `Point` and `Line` classes by adding a few lines to the `Window`
8. Created new class for `Cell`
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
