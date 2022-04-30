from BirdBrain import Finch
from time import sleep
bird = Finch()

def exercise1():
    bird.setBeak(100,0,100)
    sleep(2)
    bird.setBeak(0,100,100)
    sleep(2)
    bird.setBeak(100,0,100)
    sleep(2)
    
def exercise3():
    bird.setTail(1,0,0,100)
    bird.setTail(4,0,0,100)
    sleep(2)
    bird.stopAll()

def exercise4():
    bird.setBeak(100,0,0)
    bird.setTail(1,100,100,0)
    bird.setTail(2,0,100,100)
    bird.setTail(3,0,100,0)
    bird.setTail(4,0,0,100)
    sleep(5)
    bird.stopAll()

def exercise5():
    userResponse = input("Which tail light (1-4) should be red ")
    number = int(userResponse)
    bird.setTail(number,100,0,0)
    sleep(2)
    bird.stopAll()

def exercise6():
    userResponse = input("how much red do you want?")
    redColor = int(userResponse)
    userResponse = input("how much green do you want?")
    greenColor = int(userResponse)
    userResponse = input("how much blue do you want?")
    blueColor = int(userResponse)
    bird.setBeak(redColor,greenColor,blueColor)
    sleep(3)
    bird.stopAll()
    

    
#exercise1()
#exercise3()
#exercise4()
#exercise5()
exercise6()
