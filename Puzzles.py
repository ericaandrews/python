#Combine lists
	activities = ['reading', 'walking', 'cooking', 'driving', 'hanging out']
	print(activities)
	foods = ['pastas', 'sushi', 'tacos', 'sandwitches', 'salads']
	print(foods)
	favorites = (activities + foods)
	print (favorites)

#Pickle
	import pickle
	favorites = [ 'PlayStation', 'Toffee', 'Movies', 'Python' ]
	f = open('favorites.dat', 'wb')
	pickle.dump(favorites, f)
	f.close()
	
	#Restart console	
	import pickle
	f = open('favorites.dat', 'rb')
	favorites = pickle.load(f)
	print(favorites)	

#Variable substitution
	ninjas = 3 * 25
	print (ninjas)
	samurai = 2 * 40
	print (samurai)
	total_in_battle= ninjas + samurai
	print (total_in_battle)
	print ((3*25) + (2*40))

	roofs = 3
	ninjas_per_roof = 25
	tunnels = 2
	samurai_per_tunnel = 40
	print ((roofs * ninjas_per_roof) + (tunnels * samurai_per_tunnel))


#Placeholders
	first_name = "FirstName"
	last_name = "LastName"
	print('"Hi there, %s %s"' % (first_name, last_name))

	space = ' '*25
	print ('%s 12 Name Street'% space)
	print ('%s Twinkle Heath'% space)
	print ('%s West Sno'% space)
	print ()
	print ('Dear Sir')
	print ()
	print ('I wish to report that tiles are missing from the')
	print ('outside roof.')
	print ('I think it was wind the other night that blew them away.')
	print ()
	print ('Regards')
	print ('Malcolm Dithering')


#If statements
	amount = 800
	if (amount >= 100 and amount <= 500) or (amount >= 1000 and amount <= 5000):
	    print('amount is between 100 & 500 or between 1000 & 5000')
	amount = 400
	if (amount >= 100 and amount <= 500) or (amount >= 1000 and amount <= 5000):
	    print('amount is between 100 & 500 or between 1000 & 5000')
	amount = 3000
	if (amount >= 100 and amount <= 500) or (amount >= 1000 and amount <= 5000):
	    print('amount is between 100 & 500 or between 1000 & 5000')

	ninjas = 5
	if ninjas < 10:
	    print("I can fight those ninjas!")
	elif ninjas < 30:
	    print("It'll be a struggle, but I can take 'em")
	elif ninjas < 50:
	    print("That's too many")

	twinkies = 600
	if twinkies < 100 or twinkies > 500:
	    print('Too few or too many')    


#For loops
	for a in range (1,30,2):
	    print (a)
    
	for x in range(2, 16, 2):
	    print(x)

	for a in range (0, 30):
	    if (a % 2 == 1):
		print(a) 

	ingredients=['snails', 'leeches', 'gorilla belly-button lint', 'catepillar eyebrows', 'centipede toes']
	for i in range (len(ingredients)):
	    print (i,ingredients[i])  

	ingredients=['snails', 'leeches', 'gorilla belly-button lint', 'catepillar eyebrows', 'centipede toes']
	x = 1
	for i in ingredients:
	    print ('%s %s' % (x,i))
	    x = x + 1

	
#Defined function
	def dear_sir_letter():
		space = (" ") * 25
		print()
		print()
		print("%s 12 Name Street" %space)
		print("%s Twinkle Health " %space)
		print("%s West Sno " %space)
		print()
		print()
		print("Dear Sir")
		print()
		print("I wish to report that tiles are missing from the ")
		print("outside roof")
		print("I think it was wind the other night that blew them away.")
		print()
		print("Regards")
		print("Malcolm Dithering")
		print()
		print()
		print()
	print(dear_sir_letter())


#Functions with parameters
	def savings(pocket_money, paper_route, spending):
	    return pocket_money + paper_route - spending
	print(savings(10, 10, 5))

	def spaceship_building(cans):
	    total_cans = 0
	    for week in range(1,53):
		total_cans = total_cans + cans
		print('Week %s = %s cans' % (week, total_cans))      
	spaceship_building(2)
	spaceship_building(13)
 	
	def testfunc(myname):
	    print('hello %s' % myname)
	testfunc('MyName')

	def testfunc(fname, lname):
	    print('Hello %s %s' % (fname, lname))
	testfunc('FirstName', 'LastName')
	firstname = 'FirstName'
	lastname = 'LastName'
	testfunc(firstname, lastname)

	
#sys.stdin.readline()
	def your_age():
	    print('How old are you?')
	    age = int(sys.stdin.readline())
	    if age >= 10 and age <= 13:
		print('What is 13 + 49 + 84 + 155 + 97? A headache!')
	    else:
		print('Huh?')
	your_age()


#Absolute function
	print(abs(10))
	print(abs(-10))

	a = abs(10) + abs(-10)
	print(a)

	b = abs(-10) + -10
	print(b)

	steps = -3
	if abs(steps) > 0:
	    print('Character is moving')
	else: 
	    print('Character is not moving')
    
	steps = -3
	if (steps) > 0:
	    print('Character is moving')    
	else: 
	    print('Character is not moving')


#Random
import random
	deserts= ['cookies', 'ice cream', 'sundaes', 'brownies','cake']
	print(random.choice(deserts))
	print(random.choice(deserts))

	random.shuffle(deserts)
	print(deserts)
	random.shuffle(deserts)
	print(deserts)


#Keyword
import keyword
	print(keyword.kwlist)
	
	#Check if word is keyword
	print(keyword.iskeyword('if'))
	print(keyword.iskeyword('else'))
	print(keyword.iskeyword('keyword'))


#Tuple
	fibs = (0,1,1,2,3)
	print (fibs [4])
	print (fibs [3])
	print (fibs [2])
	print (fibs [1])
	print (fibs [0])


#Map
favorite_sports= {'Ralph Williams' : 'Football',
                  'Michael Tippett' : 'Basketball',
                  'Edward Elgar' :  'Baseball',
                  'Rebecca Clarke' :  'Netball',
                  'Ethel Smyth' : 'Badminton',
                  'Frank Bridge' :  'Rugby'}

	#Printing value of item in map
	print (favorite_sports['Rebecca Clarke'])
	print (favorite_sports)
	
	#Deleting item in map
	del favorite_sports ['Ethel Smyth']
	print (favorite_sports)
	
	#Changing items value in map
	favorite_sports ['Ralph Williams'] = 'Ice Hockey'
	print (favorite_sports)


#System exit
	import sys
	sys.exit()


#Quotes in strings
	silly_strings = '''He said, "Aren't can't shouldn't wouldn't."'''
	print (silly_strings)

#Animation
import time
from tkinter import *

	tk = Tk()
	canvas = Canvas(tk, width=400, height=200)
	canvas.pack()
	canvas.create_polygon(10, 10, 10, 60, 50, 35)
	for x in range(0, 60):
	   canvas.move(1, 5, 0)
	   tk.update()
	   time.sleep(0.05)

	tk = Tk()
	canvas = Canvas(tk, width=400, height=400)
	canvas.pack()
	canvas.create_polygon(10, 10, 10, 60, 50, 35)
	for x in range(0, 60):
	    canvas.move(1, 5, 5)
	    tk.update()
	    time.sleep(0.05)
	for x in range(0, 60):
	    canvas.move(1, -5, -5)
	    tk.update()
	    time.sleep(0.05)


#Animated Game
#Use left and right keys to move paddle
from tkinter import *
import random
import time

	tk = Tk()
	tk.title("Game")
	tk.resizable(0, 0)
	tk.wm_attributes("-topmost", 1)
	canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
	canvas.pack()
	tk.update()

	class Ball:
	    def __init_
	    _(self, canvas, paddle, color):
		self.canvas = canvas
		self.paddle = paddle
		self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
		self.canvas.move(self.id, 245, 100)
		starts = [-3, -2, -1, 1, 2, 3]
		random.shuffle(starts)
		self.x = starts[0]
		self.y = -3
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()
		self.hit_bottom = False

	    def draw(self):
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
		    self.y = 3
		if self.hit_paddle(pos) == True:
		    self.y = -3
		if pos[3] >= self.canvas_height:
		    self.hit_bottom = True
		if pos[0] <= 0:
		    self.x = 3
		if pos[2] >= self.canvas_width:
		    self.x = -3

	    def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
		    if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
			return True
		return False

	class Paddle:
	    def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
		self.canvas.move(self.id, 200, 300)
		self.x = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
		self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

	    #Speed of paddle
	    def turn_left(self, evt):
		self.x = -3

	    def turn_right(self, evt):
		self.x = 3

	    def draw(self):
		self.canvas.move(self.id, self.x, 0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
		    self.x = 0
		elif pos[2] >= self.canvas_width:
		    self.x = 0

	paddle = Paddle(canvas, 'blue')
	ball = Ball(canvas, paddle, 'red')

	while 1:
	    if ball.hit_bottom == False:
		ball.draw()
		paddle.draw()
	    tk.update_idletasks()
	    tk.update()
	    time.sleep(0.01)

#Graphics

	#Car
	import turtle
	t = turtle.Pen()
	t.color(1,0,0) 
	t.begin_fill() 
	t.forward(100) 
	t.left(90) 
	t.forward(20) 
	t.left(90) 
	t.forward(20) 
	t.right(90) 
	t.forward(20) 
	t.left(90) 
	t.forward(60) 
	t.left(90) 
	t.forward(20) 
	t.right(90) 
	t.forward(20) 
	t.left(90) 
	t.forward(20) 
	t.end_fill()
	t.color(0,0,0)
	t.up() 
	t.forward(10) 
	t.down()
	t.begin_fill() 
	t.circle(10) 
	t.end_fill()
	t.setheading(0) 
	t.up() 
	t.forward(90) 
	t.right(90)
	t.forward(10) 
	t.setheading(0)
	t.begin_fill() 
	t.down() 
	t.circle(10) 
	t.end_fill()

	#Box
	import turtle
	t = turtle.Pen()
	t.forward(50)
	t.left(45)
	t.up()
	t.forward(50)
	t.down()
	t.left(45)
	t.forward(50)
	t.left(45)
	t.up()
	t.forward(50)
	t.down()
	t.left(45)
	t.forward(50)
	t.left(45)
	t.up()
	t.forward(50)
	t.down()
	t.left(45)
	t.forward(50)
	t.left(45)
	t.up()
	t.forward(50)
	t.down()
	t.left(45)

	#Isosceles
	import turtle
	t = turtle.Pen()
	t.forward(50)
	t.left(104.47751218592992)
	t.forward(100)
	t.left(151.04497562814015)
	t.forward(100)
	t.left(104.47751218592992)

	#Rectangle
	import turtle
	t = turtle.Pen()
	t.forward(100)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(50)

	#Triangle
	import turtle
	t = turtle.Pen()
	t.forward(100)
	t.left(120)
	t.forward(100)
	t.left(120)
	t.forward(100)

	#Pitch Fork
	import turtle
	t1 = turtle.Pen()
	t2 = turtle.Pen()
	t3 = turtle.Pen()
	t4 = turtle.Pen()
	t1.forward(100)
	t1.left(90)
	t1.forward(50)
	t1.right(90)
	t1.forward(50)
	t2.forward(110)
	t2.left(90)
	t2.forward(25)
	t2.right(90)
	t2.forward(25)
	t3.forward(110)
	t3.right(90)
	t3.forward(25)
	t3.left(90)
	t3.forward(25)
	t4.forward(100)
	t4.right(90)
	t4.forward(50)
	t4.left(90)
	t4.forward(50)

	#Octagon
	import turtle
	t = turtle.Pen()
	def octagon(size, filled):
	    if filled == True:
		t.begin_fill()
	    for x in range(1,9):
		t.forward(size)
		t.right(45)
	    if filled == True:
		t.end_fill()

	t.color(1, 0.85, 0)
	octagon(40, True)
	t.color(0, 0, 0)
	octagon(40, False)
