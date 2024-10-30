from graphics import Window, Line, Point


def main():
    line1 = Line(Point(2,34), Point(20, 134))
    line2 = Line(Point(132, 123), Point(20, 134))
    line3 = Line(Point(542,421), Point(20, 134))
    line4 = Line(Point(452,12), Point(20, 134))
    win = Window(800, 600)
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.draw_line(line3, "green")
    win.draw_line(line4, "blue")
    win.wait_for_close()

main()