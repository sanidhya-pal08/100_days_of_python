from turtle import Turtle,Screen
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
screen=Screen()
screen.listen()

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.current_direction = RIGHT
        self.leng=len(STARTING_POSITIONS)
        self.head=self.segments[0]
        
    
    def increase_size(self):
        tail = self.segments[-1]
        new_segment = Turtle("circle")
        new_segment.penup()
        new_segment.color("green")
        new_segment.goto(tail.position())
        self.segments.append(new_segment)
    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment=Turtle("circle")
            segment.penup()
            segment.color("green")
            segment.goto(position)
            self.segments.append(segment)


    def go_up(self):
        if self.current_direction != DOWN:
            self.segments[0].setheading(UP)
            self.current_direction = UP

    def go_down(self):
        if self.current_direction != UP:
            self.segments[0].setheading(DOWN)
            self.current_direction = DOWN

    def go_left(self):
        if self.current_direction != RIGHT:
            self.segments[0].setheading(LEFT)
            self.current_direction = LEFT

    def go_right(self):
        if self.current_direction != LEFT:
            self.segments[0].setheading(RIGHT)
            self.current_direction = RIGHT
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(20)
    