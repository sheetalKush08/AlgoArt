import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

t.speed(0)
n = 70
h = 0

# Use tracer for faster drawing
turtle.tracer(10)

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1/n
    if h > 1:  # Reset hue to avoid exceeding 1
        h -= 1
    t.color(c)
    
    t.left(1)
    t.forward(1)
    
    for j in range(2):
        t.left(2)
        t.circle(100)
        
# Update the screen only after the loop ends
turtle.update()


turtle.done()
