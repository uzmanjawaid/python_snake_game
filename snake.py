from turtle import Turtle
STARTING_POSITION=[(0, 0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP = 90
LEFT = 180
DOWN= 270
RIGHT = 360
class Snake:
    def __init__(self):
        self.segments= []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_seg = self.segments[seg_num - 1].xcor()
            y_seg = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_seg, y_seg)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self,position):
        turtle = Turtle()
        turtle.shape("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.segments.append(turtle)

    def snake_touch(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False




