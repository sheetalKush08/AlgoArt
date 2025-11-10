# import turtle
# import random

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.tracer(0)  # Turn off screen updates for smoother animation

# # Create a turtle for drawing bubbles
# bubble = turtle.Turtle()
# bubble.hideturtle()
# bubble.speed(0)
# bubble.penup()

# # Function to create a random bubble
# def create_bubble():
#     bubble.goto(random.randint(-300, 300), random.randint(-300, -100))
#     bubble_size = random.randint(10, 50)
#     bubble_color = (random.random(), random.random(), random.random())  # Random color
#     bubble.color(bubble_color)
#     bubble.dot(bubble_size)

# # Function to move bubbles upwards
# def move_bubbles():
#     bubble.clear()
#     for _ in range(20):  # Create multiple bubbles at once
#         create_bubble()
    
#     # Update the screen
#     screen.update()

# # Main loop to keep bubbles moving
# while True:
#     move_bubbles()
#     screen.update()
#     turtle.time.sleep(0.1)  # Pause to control the speed of the animation

# turtle.done()


import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)  # Turn off screen updates for smoother animation

# Create a class for bubbles
class Bubble:
    def __init__(self):
        self.bubble = turtle.Turtle()
        self.bubble.shape("circle")
        self.bubble.penup()
        self.bubble.speed(0)
        self.bubble.color(random.random(), random.random(), random.random())
        self.size = random.randint(10, 50)
        self.bubble.shapesize(self.size / 20)  # Set size of the bubble
        self.bubble.setx(random.randint(-300, 300))
        self.bubble.sety(random.randint(-300, -200))
        self.speed = random.uniform(0.5, 2)  # Random speed for each bubble

    def move(self):
        # Move the bubble upwards
        self.bubble.sety(self.bubble.ycor() + self.speed)
        # Reset position when bubble goes off the top of the screen
        if self.bubble.ycor() > 300:
            self.bubble.setx(random.randint(-300, 300))
            self.bubble.sety(random.randint(-300, -200))
            self.speed = random.uniform(0.5, 2)
            self.bubble.color(random.random(), random.random(), random.random())  # Change color

# Create multiple bubbles
bubbles = [Bubble() for _ in range(20)]

# Main loop to keep the bubbles moving upwards
while True:
    for bubble in bubbles:
        bubble.move()
    screen.update()  # Update the screen
    turtle.time.sleep(0.02)  # Pause to control animation speed

turtle.done()
