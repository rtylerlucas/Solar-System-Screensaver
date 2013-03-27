#Russell Tyler Lucas
#902821910
#rtylerlucas@gatech.edu
#I worked on this hw assignment alone
#using only class resources
from myro import*
from random import*
import time
from math import*

#The point of this program is to show a nice visual representation/screensaver
#Of our planets orbiting the sun. Each planet's speed is based to they're comparative
#speed in real life to each other. Meaning, that Mercury orbits many of more times
#than Uranus, just as in real life. However there speed is in no way scaled to
#actual planetary orbit.

#It is displayed in the graphics window, using circles as planets and stars.

#These first few functions were used to create the different colors
#of the planets, as well as have a base function for creating circles
def makeCircle (x,y,r):
    return Circle(Point(x,y), r)

def makeWhite ():
    red = randrange(255,256)
    green = randrange(255,256)
    blue = randrange(255,256)
    return color_rgb(red,green,blue)

def makeOrange ():
    red = randrange(255,256)
    green = randrange(126,127)
    blue = randrange(0,1)
    return color_rgb(red,green,blue)


def makeMercury ():
    red = randrange(139,140)
    green = randrange(136,137)
    blue = randrange(120,121)
    return color_rgb(red,green,blue)

def makeVenus ():
    red = randrange(34,35)
    green = randrange(139,140)
    blue = randrange(34,35)
    return color_rgb(red,green,blue)

def makeJupiter ():
    red = randrange(222,223)
    green = randrange(184,185)
    blue = randrange(135,136)
    return color_rgb(red,green,blue)


def makeDBlue ():
    red = randrange(0,1)
    green = randrange(170,171)
    blue = randrange(255,256)
    return color_rgb(red,green,blue)

#Orbit is my main function in which most of the programming work is performed.
#I prompt the user for how long they would like the screensaver to go, create
#the graph window, and then intialize the planetary movement.
def orbit():
    width = 2000
    height = 900
    starList = []
    planetList = []
    print "Welcome to the Solar Screensaver. Watch as the planets orbit at \n they're realistic comparative speeds.\n "
    wait(2.5)
    input = raw_input("How long you would like to watch the planets orbit? \n (It takes approximately 40 seconds for the slowest of planets, Neptune, \n to make a full rotation.)\n Orbital Duration: ")
    
    print "\n"

    try:
        timeV = int(input)
    except ValueError:
        
        print "***Please enter a positive integer*** \n."
        orbit()
            
            
    print "Planets: initiate."
    wait(2)
    myCanvas = GraphWin ("Round n' Round",width,height)

    myCanvas.setBackground ("black")
    N = 50
    for i in range(N):
        x = randrange(0,width)
        y = randrange (0,height)
        r = randrange (2,3)
        star = makeCircle (x,y,r)
        star.setFill(makeWhite())
        star.draw(myCanvas)
        
        
    sun = makeCircle(1650,450,400)
    sun.setFill(makeOrange())
    sun.draw(myCanvas)
    dx = .02
    dy = .02
    mercury = makeCircle(1185,450,10)
    mercury.setFill(makeMercury())
    
    planetList.append(mercury)
    
    venus= makeCircle(1120,450,20)
    venus.setFill(makeVenus())
    
    planetList.append(venus)
    
    earth= makeCircle(1020,450,30)
    earth.setFill("blue")
    
    planetList.append(earth)
    
    mars= makeCircle(920,450,25)
    mars.setFill("red")
    
    planetList.append(mars)
    
    jupiter= makeCircle(790,450,69)
    jupiter.setFill(makeJupiter())
    
    planetList.append(jupiter)

    saturn = makeCircle(630,450,50)
    saturn.setFill("gold")
    
    planetList.append(saturn)

    sRing= Oval(Point(550,450),Point(710,465))
    sRing.setFill("brown")
    
    planetList.append(sRing)
                      
    uranus= makeCircle(480,450,43)
    uranus.setFill("cyan")
    
    planetList.append(uranus)

    neptune= makeCircle(345,450,40)
    neptune.setFill(makeDBlue())
    
    planetList.append(neptune)
    #This for loop was used to draw all the planets from a single
    # list of planets
    for planet in planetList:
        planet.draw(myCanvas)

    #Making the planets orbit the sun was one of the hardest parts of my
    #program, as I used a form of polar coordinate math in order to rotate
    #around a certain point, ( in this case the middle of the sun.)

    #all the planets start at negative pi, being horizontal on the unit circle
    
    mercuryAngle = -1*math.pi
    venusAngle = -1*math.pi
    earthAngle = -1*math.pi
    marsAngle = -1*math.pi
    jupiterAngle = -1*math.pi
    sRingAngle = -1*math.pi
    saturnAngle = -1*math.pi
    uranusAngle = -1*math.pi
    neptuneAngle = -1*math.pi
    
    mercuryR = 465
    venusR = 530
    earthR = 630
    marsR = 730
    jupiterR = 860
    saturnR = 1020
    sRingR1 = 1100
    sRingR2 = 940
    uranusR = 1170
    neptuneR = 1305
    #All the planets have different radius' thus I had to have different
    #ones incorporated into each of their performance
    wait(20)
    mercury.undraw()
    venus.undraw()
    earth.undraw()
    mars.undraw()
    jupiter.undraw()
    saturn.undraw()
    sRing.undraw()
    uranus.undraw()
    neptune.undraw()
    
    #The thought process behind the planet movement is basically
    #To draw each planet in one point, undraw that planet, and then
    #immediately redraw it in a new, slightly moved, position, based on
    # the mathematical formula

    
    while timeRemaining(timeV):
        mercuryY = (mercuryR * math.sin(mercuryAngle)+ 450)
        mercuryX = (mercuryR * math.cos(mercuryAngle) + 1650)
          
        mercury = makeCircle(mercuryX,mercuryY,10)
        mercury.setFill(makeMercury())
        mercury.draw(myCanvas)

        venusY = (venusR * math.sin(venusAngle)+ 450)
        venusX = (venusR * math.cos(venusAngle) + 1650)

        
          
        venus= makeCircle(venusX,venusY,20)
        venus.setFill(makeVenus())
        venus.draw(myCanvas)

        
        earthY = (earthR * math.sin(earthAngle)+ 450)
        earthX = (earthR * math.cos(earthAngle) + 1650)
          
        earth= makeCircle(earthX,earthY,30)
        earth.setFill("blue")
        earth.draw(myCanvas)

        
        marsY = (marsR * math.sin(marsAngle)+ 450)
        marsX = (marsR * math.cos(marsAngle) + 1650)
          
        mars= makeCircle(marsX,marsY,25)
        mars.setFill("red")
        mars.draw(myCanvas)

        
        jupiterY = (jupiterR * math.sin(saturnAngle)+ 450)
        jupiterX = (jupiterR * math.cos(saturnAngle) + 1650)
          
        jupiter = makeCircle(jupiterX,jupiterY,69)
        jupiter.setFill(makeJupiter())
        jupiter.draw(myCanvas)
        
        saturnY = (saturnR * math.sin(saturnAngle)+ 450)
        saturnX = (saturnR * math.cos(saturnAngle) + 1650)
        

        saturn= makeCircle(saturnX,saturnY,50)
        saturn.setFill("gold")
        saturn.draw(myCanvas)
        

        sRingY1 = (sRingR1 * math.sin(sRingAngle)+ 450)
        sRingX1 = (sRingR1 * math.cos(sRingAngle) + 1650)
        sRingY2 = (sRingR2 * math.sin(sRingAngle)+ 450)
        sRingX2 = (sRingR2 * math.cos(sRingAngle) + 1650)
        
        sRing= Oval(Point(sRingX1,sRingY1),Point(sRingX2,sRingY2))
        sRing.setFill("brown")
        sRing.draw(myCanvas)
        
        uranusY = (uranusR * math.sin(uranusAngle)+ 450)
        uranusX = (uranusR * math.cos(uranusAngle) + 1650)
          
        uranus= makeCircle(uranusX,uranusY,44)
        uranus.setFill("cyan")
        uranus.draw(myCanvas)

        
#When I first animated a single planet, there was no apparent flickering
#of the planet as it orbited the sun. #However as I added more planets to
#the orbit, each planet began to rapidly flicker as it moved.
#I added a wait function within the program, which helped a little,
#but Jay seemed to think that there was not a good way to stop the flickering
#completely

#In the end I kind of decided the flickering did not take away from the program
#but actually added a cool flair to the final product
        
        neptuneY = (neptuneR * math.sin(neptuneAngle)+ 450)
        neptuneX = (neptuneR * math.cos(neptuneAngle) + 1650)
          
        neptune = makeCircle(neptuneX,neptuneY,40)
        neptune.setFill(makeDBlue())
        neptune.draw(myCanvas)

        mercuryAngle = mercuryAngle+ (.1)
        venusAngle = venusAngle+ (.085)
        earthAngle = earthAngle+ (.08)
        marsAngle = marsAngle+ (.07)
        jupiterAngle = jupiterAngle+ (.05)
        saturnAngle = saturnAngle + (.04)
        sRingAngle = sRingAngle+ (.04)
        uranusAngle = uranusAngle+ (.035)
        neptuneAngle = neptuneAngle+ (.03)

        
        wait(.01)
        mercury.undraw()
        venus.undraw()
        earth.undraw()        
        mars.undraw()
        jupiter.undraw()
        saturn.undraw()
        sRing.undraw()
        uranus.undraw()
        neptune.undraw() 
    myCanvas.close()
    print "********************"
    print "******ALL DONE******"
    print "********************"
    return None
#The window is then closed and the user is prompted that they are DONE

#This program will start as soon as you run the program.
orbit()
        
         




