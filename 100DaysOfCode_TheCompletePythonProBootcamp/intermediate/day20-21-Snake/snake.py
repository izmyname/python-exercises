from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            
        return self.head.fd(MOVE_DISTANCE)
    
    def add_segment(self, pos):

            snake = Turtle(shape = "square")
            snake.color("white")
            snake.pu()
            snake.goto(pos)
            self.segments.append(snake)
        
    
    def extend(self):
        self.add_segment(self.segments[-1].pos())
        
    def reset(self):
        for seg in self.segments:
            seg.goto(999, 999)
            
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
    def up(self):
        if self.head.heading() != DOWN:
            
            return self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            
            return self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
        
            return self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
        
            return self.head.setheading(RIGHT)
    
