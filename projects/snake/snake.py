from turtle import Turtle

START = ((20, 0), (0, 0), (-20, 0))
STEP = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]
        
    def create_segment(self, pos):
        snake_seg = Turtle(shape = "square")
        snake_seg.color("white")
        snake_seg.pu()
        snake_seg.goto(pos)
        self.snake_segments.append(snake_seg)
        
    def create_snake(self):
        for pos in START:
            self.create_segment(pos)
            
    def snake_move(self):
        for seg_num in range(len(self.snake_segments) -1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_head.fd(STEP)
        
    def extend_snake(self):
        self.create_segment(self.snake_segments[-1].pos())

        
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)