# arguments, parameter, variable scope and return values

def myFunction(name):
    print("Your name is: " + name)

def getName():
    name = input("What is your name:")  #Local variable scope
    return name

def runit():
    print("Start the app ...")
    myFunction(getName())

#run the program
runit()

#Global variable scope
name = getName()
print(name)
