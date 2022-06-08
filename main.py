import turtle#imports python vizual
import time
def microscuff():
	t = turtle.Turtle()
	t.hideturtle()
	t.speed(100)
	t.pu()
	t.goto(100,100)
	t.pd()
	t.begin_fill()
	for count in range(4):
		t.color('orange')
		t.width(10)
		t.fd(100)
		t.rt(90)
	t.end_fill()
	
	
	t.pu()
	t.fd(100)
	t.width(10)
	t.color('blue')
	t.pd()
	t.begin_fill()
	for count in range(4):
		t.fd(100)
		t.rt(90)
	t.end_fill()
	t.begin_fill()
	t.lt(90)
	t.color('red')
	for count in range(4):
		t.fd(100)
		t.rt(90)
	t.end_fill()
	t.begin_fill()
	t.lt(90)
	t.color('green')
	for count in range(4):
		t.fd(100)
		t.rt(90)
	t.end_fill()
	time.sleep(0.25)
	t.clear()



	
#is a function
def welcome():
	t = turtle.Turtle()
	t.speed(10)
	t.hideturtle()
	t.color('blue')
	t.width(5)
	t.rt(90)
	t.fd(50)
	t.bk(25)
	t.lt(90)
	t.fd(25)
	t.rt(90)
	t.fd(25)
	t.bk(50)

	t.pu()
	t.lt(90)
	t.fd(25)

	t.pd()
	t.rt(90)
	t.fd(50)
	time.sleep(0.5)
	t.clear()
	
	


	

def uhh1():
	t = turtle.Turtle()
	t.hideturtle()
	t.speed(10)
	t.pu()
	t.lt(90)
	t.fd(30)
	t.lt(90)
	t.color('blue')
	t.width(10)
	t.fd(30)
	t.pd()
	t.begin_fill()
	for count in range(8):
		t.fd(50)
		t.rt(45)
	t.color('black')
	t.end_fill()
	t.pu()
	t.color('green')
	t.fd(125)
	t.pd()
	t.begin_fill()
	for count in range(8):
		t.fd(50)
		t.rt(45)

	t.color('cyan')

	t.end_fill()
	time.sleep(0.5)
	t.clear()







def uhh2():
	t = turtle.Turtle()
	t.hideturtle()
	t.speed(10)
	t.width(10)
	t.pu()
	t.rt(90)
	t.fd(120)
	t.pd()
	t.fd(1)
	t.color('black')
	t.begin_fill()
	for count in range(16):
		t.fd(25)
		t.rt(22.5)
	t.color('blue')
	t.end_fill()
	t.lt(90)
	t.pu()
	t.fd(50)
	t.pd()
	t.begin_fill()
	for count in range(16):
		t.fd(25)
		t.rt(22.5)	
	t.color('black')
	t.end_fill()
	time.sleep(0.5)
	t.clear()

	
	







	
def uhh3():
	t = turtle.Turtle()
	t.hideturtle()
	t.pu()
	t.goto(145,333)
	t.width(10)
	t.speed(100)
	t.color('red')
	t.pd()
	t.begin_fill()
	for count in range(32):
		t.fd(12.5)
		t.rt(11.25)
	t.color('orange')
	t.end_fill()
	time.sleep(0.5)
	t.clear()
	





def uhh4():
	t = turtle.Turtle()
	for count in range(2):
		t.width(10)
		t.speed(50)
		t.pu()
		t.rt(180)
		t.fd(125)
		t.pd()
		t.color('blue')
		t.begin_fill()
		for count in range(32):
			t.fd(12.5)
			t.rt(11.25)
		t.color('cyan')
	
		t.end_fill()
	t.fd(10)
	for count in range(2):
	
		t.width(10)
		t.speed(10)
		t.pu()
		t.rt(180)
		t.fd(125)
		t.pd()
		t.color('red')
		t.begin_fill()
		for count in range(32):
			t.fd(12.5)
			t.rt(11.25)
		t.color('green')
	
		t.end_fill()
	t.fd(10)
	for count in range(2):
	
		t.width(10)
		t.speed(10)
		t.pu()
		t.rt(180)
		t.fd(125)
		t.pd()
		t.color('cyan')
		t.begin_fill()
		for count in range(32):
			t.fd(12.5)
			t.rt(11.25)
		t.color('red')
	
		t.end_fill()
	t.fd(10)
	for count in range(2):
	
		t.width(10)
		t.speed(10)
		t.pu()
		t.rt(180)
		t.fd(125)
		t.pd()
		t.color('black')
		t.begin_fill()
		for count in range(32):
			t.fd(12.5)
			t.rt(11.25)
		t.color('blue')
	
		t.end_fill()
	t.rt(90)
	for count in range(2):
	
		t.width(10)
		t.speed(10)
		t.pu()
		t.rt(180)
		t.fd(125)
		t.pd()
		t.color('yellow')
		t.begin_fill()
		for count in range(32):
			t.fd(12.5)
			t.rt(11.25)
		t.color('purple')
	
		t.end_fill()
	t.fd(10)
	for count in range(2):
	
		t.width(10)
		t.speed(10)
		t.pu()
		t.rt(180)
		t.fd(125)
		t.pd()
		t.color('pink')
		t.begin_fill()
		for count in range(32):
			t.fd(12.5)
			t.rt(11.25)
		t.color('dark green')
	
		t.end_fill()
	t.fd(10)
	time.sleep(0.5)
	t.clear()
	t.begin_fill()
	t.color('purple')
	for count in range(4):
		t.fd(250)
		t.rt(90)
	t.end_fill()
	time.sleep(1)
	
	
	t.rt(90)
	t.fd(10)
	t.color('purple')
	t.begin_fill()
	for count in range(4):
		t.fd(250)
		t.rt(90)
	t.end_fill()
	t.clear()
	

	





















def uhh5():
	t = turtle.Turtle()
	t.hideturtle()
	t.width(13)
	t.speed(5)
	t.pu()
	t.goto(0,0)
	t.pd()
	t.color('blue')
	t.pu()
	t.fd(100)
	t.pd()
	t.speed(10)
	for count in range(1):
		for count in range(320):
			t.fd(1.25)
			t.rt(1.125)
		t.fd(9)
	t.pu()
	t.goto(0,0)
	t.color('green')
	t.bk(100)
	t.pd()
	for count in range(1):
		for count in range(320):
			t.fd(1.25)
			t.rt(1.125)
		t.fd(9)
	t.pu()
	t.goto(0,126)
	t.color('red')
	t.fd(100)
	t.pd()
	for count in range(1):
		for count in range(320):
			t.fd(1.25)
			t.rt(1.125)
		t.fd(9)
	t.pu()
	t.goto(0,126)
	t.bk(100)
	t.color('orange')
	t.pd()
	for count in range(1):
		for count in range(320):
			t.fd(1.25)
			t.rt(1.125)
		t.fd(9)
	t.clear()
	
	
	
	

	



def uhh6():
	t = turtle.Turtle()
	s = turtle.Screen()
	s.bgcolor ("black")
	t.hideturtle()
	t.width(12)
	t.speed(100)
	for count in range(23):
		t.color('cyan')
		for count in range(32):
				t.fd(12.5)
				t.rt(11.25)

		t.rt(15)
		for count in range(32):
			t.fd(12.5)
			t.rt(11.25)		
	for count in range(23):
		t.color('red')
		for count in range(32):
				t.fd(12.5)
				t.rt(11.25)

		t.rt(15)
		for count in range(32):
			t.fd(12.5)
			t.rt(11.25)

			
		for count in range(23):
			t.color('red')
			for count in range(32):
				t.fd(12.5)
				t.rt(11.25)

			t.rt(15)
			for count in range(32):
				t.fd(12.5)
				t.rt(11.25)
	
	
#welcome()
#microscuff()
#uhh1()
#uhh2()
#uhh3()
#uhh4()
#uhh5()
				
uhh6()




