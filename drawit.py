#!/usr/bin/python3

import turtle

r = 50
a = 45
speed = 0

turtle.speed(speed)

def drawarc(num, direction):
	if direction:
		for i in range(0,num):
			turtle.circle(r,a)
	else:
		for i in range(0,num):
			turtle.circle(-r,a)

def goforward(num):
	for i in range(0,num):
		turtle.forward(r)

# number 8
def test1():
	print(turtle.position())
	drawarc(6,True)
	goforward(2)
	drawarc(6,False)
	goforward(2)
	print(turtle.position())

def test2():
	print(turtle.position())
	drawarc(4,True)
	goforward(2)
	drawarc(4,True)
	goforward(2)
	print(turtle.position())

# circle
def test3():
	print(turtle.position())
	drawarc(8,True)
	print(turtle.position())

def test4():
	print(turtle.position())
	drawarc(5,True)
	drawarc(1,False)
	drawarc(5,True)
	drawarc(1,False)
	print(turtle.position())

# doesn't quite get back to 0
def test5():
	print(turtle.position())
	drawarc(4,True)
	drawarc(1,False)
	drawarc(3,True)
	goforward(1)
	drawarc(3,True)
	drawarc(1,False)
	print(turtle.position())

def test6():
	print(turtle.position())
	drawarc(3,True)
	goforward(1)
	drawarc(2,True)
	drawarc(1,False)
	drawarc(3,True)
	goforward(1)
	drawarc(2,True)
	drawarc(1,False)
	print(turtle.position())

# doesn't quite get back to 0
def test7():
	print(turtle.position())
	p = ['4c', '2s', '3c', '1s', '2c', '-1c']
	drawarc(4,True)
	goforward(2)
	drawarc(3,True)
	goforward(1)
	drawarc(2,True)
	drawarc(1,False)
	print(turtle.position())

test7()

turtle.exitonclick()
