from graphics import *
from random import *
from math import *
import cmath as cm

def T(z, c):
	#our function
	return z * z + c

def t(z, c):
	n = random()
	if(n > .5):
		return cm.sqrt(z-c)
	else:
		return -cm.sqrt(z-c)

#Short method that checks if a number is between two others to make checking button presses on GUIs a bit more straightforward 
def isBet(lower, var, upper):
	if(lower > upper): #This is a stupid proofing for myself because I'm stupid
		holder = upper
		upper = lower
		lower = holder
	if(var < upper and var > lower):
		return True
	else:
		return False

#Our user interface
def gui():
	print("Choose a color scheme and click on the graph you'd like to view")
	#Initial Color Values
	global color1
	color1 = 'yellow'
	global color2
	color2 = 'purple'

	gui = GraphWin("GUI", 400, 400)
	gui.setCoords(-200, -200, 200, 200)
	#helper lines
	#Line(Point(-100, -200), Point(-100, 200)).draw(gui);Line(Point(0, -200), Point(0, 200)).draw(gui);Line(Point(100, -200), Point(100, 200)).draw(gui);Line(Point(-200, -100), Point(200, -100)).draw(gui);Line(Point(-200, 0), Point(200, 0)).draw(gui);Line(Point(-200, 100), Point(200, 100)).draw(gui)

	#Title
	title = Text(Point(0, 175), "Super Mandelbrot Explorer");title.setSize(12); title.draw(gui)
	Line(Point(-100, 165), Point(100, 165)).draw(gui)

	#Mandelbrot Button
	mbox1 = Rectangle(Point(-42, 90), Point(42, 110));mbox1.draw(gui)
	mtext = Text(Point(0, 100), "Mandelbrot");mtext.setSize(12);mtext.draw(gui)
	#Exit Box
	ebox = Rectangle(Point(166, 180), Point(202, 198));ebox.draw(gui)
	exit = Text(Point(184, 189), "EXIT");exit.setTextColor('red');exit.draw(gui)
	#Settings Button
	#setBox = Rectangle(Point(-195, 180), Point(-135, 198));setBox.draw(gui)
	#settings = Text(Point(-165, 189), "Settings");settings.draw(gui)
	#Julia Button
	jBox = Rectangle(Point(-32, 40), Point(32, 60));jBox.draw(gui)
	julia = Text(Point(0, 50), "Julia Set");julia.draw(gui)

	#Color Scheme Title
	cs = Text(Point(0, 0), "Color Schemes:"); cs.draw(gui)
	csu = Line(Point(-55, -10), Point(55, -10));csu.draw(gui)
	#red green
	rgbox = Rectangle(Point(-165, -60), Point(-95, -40));rgbox.setFill('gray80');rgbox.setOutline('gray80');rgbox.draw(gui)
	rg = Text(Point(-130, -50), "blue/pink");rg.draw(gui)
	#purple yellow
	pybox = Rectangle(Point(-47, -60), Point(47, -40));pybox.setFill('magenta');pybox.setOutline('purple');pybox.draw(gui)
	py = Text(Point(0, -50), "purple/yellow");py.draw(gui);py.setTextColor('purple')
	#orange blue
	obbox = Rectangle(Point(169, -60), Point(91, -40));obbox.setFill('gray80');obbox.setOutline('gray80');obbox.draw(gui)
	ob = Text(Point(130, -50), "gray scale");ob.draw(gui)

	
	#Click collecting loop
	while(True):
		#Get the user's mouseclick and initialize the coordinates
		click = gui.getMouse();x = click.getX(); y = click.getY()
		#If user clicked exit button, close the window and break from the loop
		if(isBet(166, x, 202) and isBet(180, y, 198)):
			gui.close() #exit the window
			break #break loop to prevent getMouse() in closed window error
		#If user clicked the mBrot button, open a new window asking for user inputs
		if(isBet(-42, x, 42) and isBet(90, y, 110)):
			mBroptions(-3, -3, 3, 3)
		#If user clicks Julia Set button open new window asking for inputs
		if(isBet(-32, x, 32) and isBet(40, y, 60)):
			juliaOpts(-3, -3, 3, 3)
		#User clicked red green
		if(isBet(-165, x, -95) and isBet(-60, y, -40)):
			rgbox.setFill('blue2');rgbox.setOutline('magenta');rg.setTextColor('magenta')
			pybox.setFill('gray80');pybox.setOutline('gray80');py.setTextColor('black')
			obbox.setFill('gray80');obbox.setOutline('gray80');ob.setTextColor('black')
			color1 = 'blue2'
			color2 = 'magenta'
		if(isBet(-47, x, 47) and isBet(-60, y, -40)):
			rgbox.setFill('gray80');rgbox.setOutline('gray80');rg.setTextColor('black')
			pybox.setFill('yellow');pybox.setOutline('purple');py.setTextColor('purple')
			obbox.setFill('gray80');obbox.setOutline('gray80');ob.setTextColor('black')
			color1 = 'yellow'
			color2 = 'purple'
		if(isBet(91, x, 169) and isBet(-60, y, -40)):
			rgbox.setFill('gray80');rgbox.setOutline('gray80');rg.setTextColor('black')
			pybox.setFill('gray80');pybox.setOutline('gray80');py.setTextColor('black')
			obbox.setFill('black');obbox.setOutline('white');ob.setTextColor('white')
			color1 = 'black'
			color2 = 'white'

#sillily named method that opens an option window as a precursor to drawing the mandelbrot set
def mBroptions(xmin, ymin, xmax, ymax):
	print("Leaving step size on auto will optomize the step size for the resolution of the window.")
	exitProgram = False #this is for later :)
	exterior = False #This variable chooses between the simple and complex color scheme for the graph
	#initializing window
	opts = GraphWin("Mandelbrot Options", 200, 200)
	opts.setCoords(-100, -100, 100, 100)
	#Draw title of options screen
	title = Text(Point(0, 80), "Mbrot Options");title.draw(opts)
	underline = Line(Point(-50, 70), Point(50, 70));underline.draw(opts) #underline title
	#Exit Box
	ebox = Rectangle(Point(72, 80), Point(101, 95)); ebox.draw(opts)
	exit = Text(Point(87, 87), "EXIT");exit.setTextColor('red'); exit.setSize(10);exit.draw(opts)
	#Max Iterations Stuff:
	miText = Text(Point(-50, 40), "Max Iterations:");miText.setSize(10);miText.draw(opts)
	miEntry = Entry(Point(50, 40), 4);miEntry.setText("30.0");miEntry.setFill("gray80");miEntry.draw(opts)
	#Step Size Stuff:
	ssText = Text(Point(-40, 10), "Step Size:");ssText.setSize(10);ssText.draw(opts)
	ssEntry = Entry(Point(50, 10), 4);ssEntry.setText("auto");ssEntry.setFill("gray80");ssEntry.draw(opts)
	#Graph Type:
	instructions = Text(Point(0, -20), "Choose graph type below:"); instructions.setSize(10);instructions.draw(opts)
	#Left button (This is already clicked)
	sbox = Rectangle(Point(-97, -41), Point(-13, -59));sbox.setOutline('magenta');sbox.setFill('gray80');sbox.draw(opts)
	simple = Text(Point(-55, -50), "w/o Escaping"); simple.setSize(10);simple.draw(opts)
	#Right button (unclicked)
	cbox = Rectangle(Point(13, -41), Point(97, -59));cbox.setOutline('gray80');cbox.setFill('gray80');cbox.draw(opts)
	comp = Text(Point(55, -50), "w/ Escaping"); comp.setSize(10);comp.draw(opts)
	#Graph button
	gbox = Rectangle(Point(-28, -71), Point(28, -89));gbox.setOutline('green');gbox.setFill('gray80');gbox.draw(opts)
	graph = Text(Point(0, -80), "Graph It!"); graph.setSize(10);graph.draw(opts)
	#collecting clicks
	while(True):
		click = opts.getMouse(); x = click.getX(); y = click.getY() #The usual initialization of click location
		#Check if the exit button was pressed, if so close the window without graphing anything
		if(isBet(72, x, 101) and isBet(80, y, 95)):
			exitProgram = True
			opts.close()
			break
		#Check if one of the two buttons was pressed, 'click' it and change the boolean
		if(isBet(-97, x, -13) and isBet(-41, y, -59)):
			sbox.setOutline('magenta')
			cbox.setOutline('gray80')
			exterior = False
		#Complex button make exterior true and vice versa
		if(isBet(13, x, 97) and isBet(-41, y, -59)):
			cbox.setOutline('magenta')
			sbox.setOutline('gray80')
			exterior = True
		#If the user clicks graph it close the loop
		if(isBet(-28, x, 28) and isBet(-71, y, -89)):
			break
	#If the loop ended without the user pressing exit, continue
	if(not exitProgram):
		#Get values from entry
		maxIt = int(float(miEntry.getText()))
		if(ssEntry.getText() == "auto"):
			stepx = (xmax-xmin)/599 #change in x / number of pixels in window
			stepy = (ymax-ymin)/599 #change in y / number of pixels in window
		else:
			#dum dum method
			stepx = float(ssEntry.getText())
			stepy = stepx
		#Close window
		opts.close()
		#Call mandelbrot with all the inputted stuff
		mandelbrot(xmin, ymin, xmax, ymax, maxIt, stepx, stepy, exterior)

def mandelbrot(xmin, ymin, xmax, ymax, maxIt, stepx, stepy, exterior): #default should be (-3, -3, 3, 3, 30)
	print("Double click on the graph window and click the exit graph button to close this graph.")
	mbrotwin = GraphWin("mBrot", 600, 600, autoflush = False)
	mbrotwin.setCoords(xmin, ymin, xmax, ymax)
	x = xmin
	while (x < xmax):
		y = ymin
		while (y < ymax):
			c = complex(x, y)
			z = complex (0, 0)
			numIters = 0
			while ((abs(z) < 2) and numIters < maxIt):
				z = T(z, c)
				numIters += 1
				
			if(exterior == True):
				if(numIters < maxIt):
					mbrotwin.plot(x, y, getColor(maxIt, numIters, color1))
				else:
					mbrotwin.plot(x, y, 'black')
			else:
				mbrotwin.setBackground(color1)
				if(numIters == maxIt):
					mbrotwin.plot(x, y, color2)
			y += stepy
		x += stepx
	#two click zoom
	while(True):
		#get two clicks and initialize x and y values for them
		click1 = mbrotwin.getMouse();x1 = click1.getX();y1 = click1.getY()
		click2 = mbrotwin.getMouse();x2 = click2.getX();y2 = click2.getY()
		#making x1 and y1 mins so that zoom doesn't flip
		if(x1 > x2):
			holder = x1
			x1 = x2
			x2 = holder
		if(y1 > y2):
			holder = y1
			y1 = y2
			y2 = holder
		#Show the user the area they have selected
		selection = Rectangle(Point(x1, y1), Point(x2, y2));selection.setOutline('magenta');selection.draw(mbrotwin)
		#Prompt the user whether they want to zoom to the selected area or not, it's easiest to do this in another window because the coordinates of this window will be changing
		promptWin = GraphWin("", 200, 100)
		promptWin.setCoords(-100, -100, 100, 100)
		#Text prompting user
		promptText = Text(Point(0, 50), "Would you like to zoom to the");promptText.setSize(10);promptText.draw(promptWin)
		promptText2 = Text(Point(0,20),"selected box?");promptText2.setSize(10);promptText2.draw(promptWin)
		#Affirmative button
		yes = Text(Point(-20, -30), "Yes");yes.setSize(10);yes.draw(promptWin)
		yesBox = Rectangle(Point(-33, -45), Point(-8, -14));yesBox.draw(promptWin)
		#Negative button
		no = Text(Point(20,-30), "No");no.setSize(10);no.draw(promptWin)
		noBox = Rectangle(Point(9, -45), Point(30,-14));noBox.draw(promptWin)
		#Close All Button
		closebox = Rectangle(Point(-35, -63), Point(35, -95));closebox.draw(promptWin)
		close = Text(Point(0, -80), "Exit Graph");close.setSize(10);close.draw(promptWin);
		#Loop that collects clicks
		while(True):
			#get and initialize click
			pClick = promptWin.getMouse();px = pClick.getX(); py = pClick.getY()
			#If the user presses "yes", 
			if(isBet(-33, px, -8) and isBet(-45, py, -14)):
				mbrotwin.close()
				promptWin.close()
				mBroptions(x1, y1, x2, y2)
				return None #break from all loops
			#If the user presses "no", close the prompt window and undraw the selection
			if(isBet(9, px, 30) and isBet(-45, py, -14)):
				promptWin.close()
				selection.undraw()
				break
			#If the user presses the "exit graph" button, close graph and prompt window
			if(isBet(-35, px, 35) and isBet(-63, py, -95)):
				promptWin.close()
				mbrotwin.close()
				return None #break from all

def juliaOpts(xmin, ymin, xmax, ymax):
	print("Leaving step size on auto will optomize the step size for the resolution of the window.")
	exitProgram = False #this is for later :)
	function = 0 #This variable chooses between the simple and complex color scheme for the graph
	#initializing window
	opts = GraphWin("Julia Set Options", 300, 400)
	opts.setCoords(-100, -100, 100, 100)
	#Draw title of options screen
	title = Text(Point(0, 95), "Julia Set Options");title.draw(opts)
	underline = Line(Point(-42, 90), Point(42, 90));underline.draw(opts) #underline title
	#Exit Box
	ebox = Rectangle(Point(77, 89), Point(97, 97)); ebox.draw(opts)
	exit = Text(Point(87, 93), "EXIT");exit.setTextColor('red'); exit.setSize(10);exit.draw(opts)
	#Max Iterations Stuff:
	miText = Text(Point(-30, 60), "Maximum Iterations:");miText.setSize(10);miText.draw(opts)
	miEntry = Entry(Point(30, 60), 4);miEntry.setText("30.0");miEntry.setFill("gray80");miEntry.draw(opts)
	#C Real Stuff:
	crText = Text(Point(-25, 40), "Real Portion of C:");crText.setSize(10);crText.draw(opts)
	crEntry = Entry(Point(30, 40), 4);crEntry.setText("0.00");crEntry.setFill("gray80");crEntry.draw(opts)
	#C Imaginary Stuff:
	ciText = Text(Point(-35, 20), "Imaginary Portion of C:");ciText.setSize(10);ciText.draw(opts)
	ciEntry = Entry(Point(30, 20), 4);ciEntry.setText("0.75");ciEntry.setFill("gray80");ciEntry.draw(opts)
	#Step Size Stuff:
	ssText = Text(Point(-12, 0), "Step Size:");ssText.setSize(10);ssText.draw(opts)
	ssEntry = Entry(Point(30, 0), 4);ssEntry.setText("auto");ssEntry.setFill("gray80");ssEntry.draw(opts)
	#Graph Type:
	instructions = Text(Point(0, -20), "Choose graph type below:"); instructions.setSize(12);instructions.draw(opts)
	#Left button (This is already clicked) two tone
	sbox = Rectangle(Point(-87, -44), Point(-43, -56));sbox.setFill('gray80');sbox.draw(opts)
	simple = Text(Point(-65, -50), "Two tone"); sbox.setOutline('magenta');simple.setSize(12);simple.draw(opts)
	#Middle button (unclicked) inverse
	ibox = Rectangle(Point(-20, -44), Point(20, -56));ibox.setFill('gray80');ibox.setOutline("gray80");ibox.draw(opts)
	inverse = Text(Point(0, -50), "Inverse");inverse.setSize(12);inverse.draw(opts)
	#Right button (unclicked) escaping
	cbox = Rectangle(Point(43, -44), Point(87, -56));cbox.setOutline('gray80');cbox.setFill('gray80');cbox.draw(opts)
	comp = Text(Point(65, -50), "Exterior"); comp.setSize(12);comp.draw(opts)
	#Graph button
	gbox = Rectangle(Point(-28, -71), Point(28, -89));gbox.setOutline('green');gbox.setFill('gray80');gbox.draw(opts)
	graph = Text(Point(0, -80), "Graph It!"); graph.setSize(15);graph.draw(opts)
	#collecting clicks
	while(True):
		click = opts.getMouse(); x = click.getX(); y = click.getY() #The usual initialization of click location
		#Check if the exit button was pressed, if so close the window without graphing anything
		if(isBet(77, x, 97) and isBet(89, y, 97)):
			exitProgram = True
			opts.close()
			break
		#Check if one of the three buttons was pressed, 'click' it and change the boolean
		if(isBet(-87, x, -43) and isBet(-44, y, -56)):
			sbox.setOutline('magenta')
			cbox.setOutline('gray80')
			ibox.setOutline('gray80')
			function = 0
		if(isBet(-20, x, 20) and isBet(-44, y, -56)):
			ibox.setOutline('magenta')
			cbox.setOutline('gray80')
			sbox.setOutline('gray80')
			function = 1
		#Complex button make exterior true and vice versa
		if(isBet(13, x, 97) and isBet(-44, y, -56)):
			cbox.setOutline('magenta')
			sbox.setOutline('gray80')
			ibox.setOutline('gray80')
			function = 2
		#If the user clicks graph it close the loop
		if(isBet(-28, x, 28) and isBet(-71, y, -89)):
			break
	#If the loop ended without the user pressing exit, continue
	if(not exitProgram):
		#Get values from entry
		maxIt = int(float(miEntry.getText()))
		if(ssEntry.getText() == "auto"):
			stepx = (xmax-xmin)/600 #change in x / number of pixels in window
			stepy = (ymax-ymin)/600 #change in y / number of pixels in window
		else:
			#dum dum method
			stepx = float(ssEntry.getText())
			stepy = stepx
		creal = float(crEntry.getText())
		cimag = float(ciEntry.getText())
		#Close window
		opts.close()
		#Call mandelbrot with all the inputted stuff
		if(function == 0):
			juliaSets(xmin, ymin, xmax, ymax, maxIt, stepx, stepy, cimag, creal, False)
		if(function == 1):
			invAlgo(10000, maxIt, creal, cimag)
		if(function == 2):
			juliaSets(xmin, ymin, xmax, ymax, maxIt, stepx, stepy, cimag, creal, True)

def juliaSets(xmin, ymin, xmax, ymax, maxIt, stepx, stepy, cimag, creal, exterior):
	print("Double click on the graph window and click the exit graph button to close this graph.")
	tt = GraphWin("JSets", 600, 600, autoflush = False)
	tt.setCoords(xmin, ymin, xmax, ymax)
	tt.setBackground(color1)
	c = complex(creal, cimag)
	x = xmin
	maxIt = 30
	count = 0
	while (x < xmax):
		y = ymin
		while (y < ymax):
			numIters = 0
			z0 = complex(x, y)
			while ((abs(z0) < 1000) and numIters < maxIt):
				z0 = T(z0, c)
				numIters += 1
			if(numIters == maxIt):
				if(exterior):
					tt.plot(x, y, 'black')
				else:
					tt.plot(x, y, color2)
			elif(exterior):
				tt.plot(x,y, getColor(maxIt, numIters, color1))
			y += stepx
		x += stepy
	while(True):
		#get two clicks and initialize x and y values for them
		click1 = tt.getMouse();x1 = click1.getX();y1 = click1.getY()
		click2 = tt.getMouse();x2 = click2.getX();y2 = click2.getY()
		#making x1 and y1 mins so that zoom doesn't flip
		if(x1 > x2):
			holder = x1
			x1 = x2
			x2 = holder
		if(y1 > y2):
			holder = y1
			y1 = y2
			y2 = holder
		#Show the user the area they have selected
		selection = Rectangle(Point(x1, y1), Point(x2, y2));selection.setOutline('magenta');selection.draw(tt)
		#Prompt the user whether they want to zoom to the selected area or not, it's easiest to do this in another window because the coordinates of this window will be changing
		promptWin = GraphWin("", 200, 100)
		promptWin.setCoords(-100, -100, 100, 100)
		#Text prompting user
		promptText = Text(Point(0, 50), "Would you like to zoom to the");promptText.setSize(10);promptText.draw(promptWin)
		promptText2 = Text(Point(0,20),"selected box?");promptText2.setSize(10);promptText2.draw(promptWin)
		#Affirmative button
		yes = Text(Point(-20, -30), "Yes");yes.setSize(10);yes.draw(promptWin)
		yesBox = Rectangle(Point(-33, -45), Point(-8, -14));yesBox.draw(promptWin)
		#Negative button
		no = Text(Point(20,-30), "No");no.setSize(10);no.draw(promptWin)
		noBox = Rectangle(Point(9, -45), Point(30,-14));noBox.draw(promptWin)
		#Close All Button
		closebox = Rectangle(Point(-35, -63), Point(35, -95));closebox.draw(promptWin)
		close = Text(Point(0, -80), "Exit Graph");close.setSize(10);close.draw(promptWin);
		#Loop that collects clicks
		while(True):
			#get and initialize click
			pClick = promptWin.getMouse();px = pClick.getX(); py = pClick.getY()
			#If the user presses "yes", 
			if(isBet(-33, px, -8) and isBet(-45, py, -14)):
				tt.close()
				promptWin.close()
				juliaOpts(x1, y1, x2, y2)
				return None #break from all loops
			#If the user presses "no", close the prompt window and undraw the selection
			if(isBet(9, px, 30) and isBet(-45, py, -14)):
				promptWin.close()
				selection.undraw()
				break
			#If the user presses the "exit graph" button, close graph and prompt window
			if(isBet(-35, px, 35) and isBet(-63, py, -95)):
				promptWin.close()
				tt.close()
				return None #break from all
#This function gives an even distribution of colors when given a starting color, ending color and max number of iterations
def getColor(maxIt, it, color1):
	if(color1 == 'yellow'):
		start = [255, 255, 0]
		end = [128, 0, 128]
	if(color1 == 'black'):
		start = [0, 0, 0]
		end = [255, 255, 255]
	if(color1 == 'blue2'):
		start = [0, 0, 238]
		end = [255, 0, 255]
	r = int(interpolate(start[0], end[0], maxIt)[it])
	g = int(interpolate(start[1], end[1], maxIt)[it])
	b = int(interpolate(start[2], end[2], maxIt)[it])
	return color_rgb(r, g, b)
#This is a helper for the get color method
def interpolate(start, end, num):
	arr = [0] * num
	step = abs(start-end)/num
	if(start > end):
		step = -step
	for i in range(num):
		arr[i] = round(start + step*i,2)
	return arr

#Draw the julia set by following the inverse of the function to the julius set and iterating around the set.
def invAlgo(numTrans, numIt, creal, cimag):
	print("Click on the window to close this graph.")
	c = complex(creal, cimag)
	win = GraphWin("JSets", 600, 600, autoflush = False)
	win.setCoords(-3, -3, 3, 3)
	win.setBackground(color1)
	#Pick a random point in the complex plane z0
	z0 = complex(randint(0,10), randint(0,10))
	#Iterate under the inverse function for a large transient starting at z0
	for x in range(numTrans):
		z0 = t(z0, c)
		#Circle(Point(z0.real, z0.imag), .01).draw(win) #This let's you see the path of the random point to the julia set, it's not that interesting
	#We can now assume that we're on the julius set so we can iterate further and plot the values we recieve as we go
	for i in range(numIt):
		z0 = t(z0, c)
		win.plot(z0.real, z0.imag, color2)
	win.getMouse()
	win.close()
gui()