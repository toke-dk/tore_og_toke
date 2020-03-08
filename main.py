#!/usr/bin/env python3        
import turtle
import math
import random
import time

hej_l = [
  "Hejsa",
  "Halloejsovs",
  "Goddag mr.",
  "Hva saa der",
]

tal_hej_l = random.randint(0, len(hej_l))



#print("Hej og velkommen til vores mega fede program her")
#print("Hvad hedder du?")
#navn = input("")
#print("")
#print(hej_l[tal_hej_l])
#print(navn)
#

#tegner labyrint
t = turtle.Turtle()
t.speed(0)



#bygger labyrint
t.goto(0, 0)
t.left(100)
for i in range(10):
  t.forward(50)
  t.left(90)
  t.forward(10)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(10)
  t.left(90)
t.right(100)
t.forward(100)
t.left(90)
t.forward(30)
t.left(90)
t.forward(140)
t.left(90)
  # slut labyrint
t.goto(-213.648177667, 984.807753012)
t.setheading(260)
t.pendown()
for i in range(10):
  t.forward(50)
  t.left(90)
  t.forward(10)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(10)
  t.left(90)

#for j in range(2):
#  for i in range(10):
#    t.forward(100+j*10)
#    t.left(90)
#    t.forward(100+j*10)
#    t.right(90)
#  t.right(180)

#spiller
p = turtle.Turtle()
p.penup()
p.speed(1000)
placeringx = 0
placeringy = 0

print("Hvilken retning?")
print("w = op")
print("a = venstre")
print("s = ned")
print("d = venstre")

while True:
  retning = input("")


  if retning.lower() == "w":
    p.goto(p.xcor(), p.ycor()+50.0)
    p.setheading(90)
  elif retning.lower() == "a":
    p.goto(p.xcor() - 50.0, p.ycor())
    p.setheading(180)
  elif retning.lower() == "s":
    p.goto(p.xcor(), p.ycor() - 50.0)
    p.setheading(270)
  elif retning.lower() == "d":
    p.goto(p.xcor() + 50.0, p.ycor())
    p.setheading(0)

  else:
    print("Ugyldig komando")


