# file manipulation and exception handling: try, except, else


##with open('system_config.txt') as file_object:
##    contents = file_object.read()
##    print(contents)

#open file function hard code file name
def openFile():
    with open('system_config.txt') as file_object:
        contents = file_object.read()
        print(contents)

#open file function with argumen
def openFile2(file):
    with open(file) as file_object:
        contents = file_object.read()
        print(contents)


class Filer():
    
    def openFile(self):
        with open('system_config.txt') as file_object:
            contents = file_object.read()
            print(contents)




    def openFile2(self, file):
        try:
            with open(file) as file_object:
                contents = file_object.read()
                print(contents)
        except FileNotFoundError:
            print("\nERROR: We had trouble reading the file.")
        else:
            print("\nWe were able to access the file.") 


    def writeFile(self, textfilename, textToInsert):
        try:
            with open(textfilename, 'w') as file_object:
                file_object.write(textToInsert)

        except FileNotFoundError:
            print("\nERROR: We had trouble writing to the file.")
        else:
            print("\nFile written to.  This is what we wrote: " + textToInsert)



    def addtoFile(self, textfilename, textToInsert):
        try:
            with open(textfilename, 'a') as file_object:
                file_object.write(textToInsert)

        except FileNotFoundError:
            print("\nERROR: We had trouble writing to the file.")
        else:
            print("\nFile written to.  This is what we wrote: " + textToInsert)

    

myWriter = Filer()
##myWriter.writeFile('myfile.txt','Big Fish')
##myWriter.openFile2('myfile.txt')
##myWriter.addtoFile('myfile.txt','... Love big fish!')
myWriter.openFile2('myfile.txt')
