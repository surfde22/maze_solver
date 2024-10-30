from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.has_right_wall = True
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2,y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top_left = Point(min(x1, x2), min(y1, y2))
        bottom_left = Point(min(x1, x2), max(y1, y2))
        top_right = Point(max(x1, x2), min(y1, y2))
        bottom_right = Point(max(x1, x2), max(y1, y2))
        if(self.has_left_wall):
            left_wall = Line(top_left, bottom_left)
            self._win.draw_line(left_wall)
        if(self.has_right_wall):
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall)
        if(self.has_top_wall):
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall)
        if(self.has_bottom_wall):
            bottom_wall = Line(bottom_right, bottom_left)
            self._win.draw_line(bottom_wall)
