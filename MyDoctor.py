# Class Skeleton

# Create class and three methods in that class

class MyDoctor():
    '''-> MyDoctor class docstring ... tell programmers about your class.'''

    def sayHi(self):
        print("Hi!")
        
    def sayBye(self):
        '''->sayBye() doctring ...'''
        print("Bye!")

    def askDocQuestion(self):
        question = input("Do you want a health tip? (yes or no) ")

        #if yes, python says: Good! Eat less sugar.
        #if !yes, python says, OK, see you next time.
        
        if question == "yes" or question == "Yes":
            print("\nGood! Eat less sugar.")
        else:
            print("\nOK, see you next time.")


SeeDoctor = MyDoctor()

print(SeeDoctor.__doc__)
print(SeeDoctor.sayBye.__doc__)

SeeDoctor.sayHi()
SeeDoctor.askDocQuestion()
SeeDoctor.sayBye()


