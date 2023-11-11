import turtle

turtle.speed(20)
size = 5
for i in range(0, 60):
    turtle.circle(size)
    turtle.left(5)
    size += 10
turtle.mainloop()