from BirdBrain import Finch
bird = Finch()
print(bird.getDistance())

def exercise1():
    print("Distance: ", bird.getDistance())
    
def exercise2():
    print("get right Light: ", bird.getLight("R"))
    print("get left Light:",bird.getLight("L"))
    print("get button :",bird.getButton("A"))
    print("get button :",bird.getButton("B"))
    print("get Orientation:",bird.getOrientation())
    print("getEncoder:",bird.getEncoder("R"))
    
def exercise3():
    print(type(birdgetDistince()))
    
#exercise1()
exercise2()
#exercise3()
