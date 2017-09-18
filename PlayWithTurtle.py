'''
This is to try lib turtle
'''

import turtle
import time

#Make something like a progress bar
def progressBar(totalTimeInSecond, totalLength):
    #make the bar forward 10 times
    steps = 10
    oneStepLength = totalLength / steps
    sleepTime  = totalTimeInSecond / steps

    while steps > 0 :
        time.sleep(sleepTime)
        turtle.forward(oneStepLength)
        steps = steps - 1
#Try two turtles, good story turtle race with rabit
def racing():
    rabitSpeed = 10
    RTSpeed = 5
    rabit = turtle.Turtle()
    rTurtle = turtle.Turtle()
    rTurtle.shape("turtle")
    #Run at step of every second
    raceLength = 100
    rabitMove = 0
    RTMove = 0 # rTurtle movement
    while rabitMove < raceLength and RTMove < raceLength:
        if rabitMove >=90 :
            #rabit stopped
            print "Rabit is sleeping"
        else:
            rabit.forward(rabitSpeed)
            rabitMove += rabitSpeed

        rTurtle.forward(RTSpeed)
        RTMove += RTSpeed
        time.sleep(1)
    if rabitMove > RTMove:
        print "Rabit win"
    elif RTMove > rabitMove:
        print "turtle win"
    else:
        print "both win"
    

#This is the window object
window = turtle.Screen()

#Play something here
#progressBar(20, 100)
racing()
#End

#exit the program when you click on the window
window.exitonclick()


