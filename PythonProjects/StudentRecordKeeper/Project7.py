#Ryan Koch

class Student:

    #Student initiator
    def __init__(self, UID, FIRST, LAST, LEVEL, CLASSES):
        self.UID = UID
        self.FIRST = FIRST
        self.LAST = LAST
        self.LEVEL = LEVEL
        self.CLASSES = CLASSES

    #help function to print all the classes of this student
    def printClasses(self, curClass):
        retList = ""
        for i in curClass:
            retList = retList + i + "\n"
        return retList

    #add a new class to a student
    def addClass(self, newClass):
        self.CLASSES.append(newClass)    

    def __str__(self):
        return "UID: " + str(self.UID) \
                + "\nFirst: " + str(self.FIRST) \
                + "\nLast: " + str(self.LAST) \
                + "\nLevel: " + str(self.LEVEL) \
                + "\nCLASSES: \n" + self.printClasses(self.CLASSES) \
                + "..........\n.......... \n\n" 



#Main function, all students are added to dictionary "students" with their UID as the key
students = {}
inData = open("studentRecordsIn.txt", "r")
outData = open("studentRecordsOut.txt", "w")
nxtLine = inData.readline()

while nxtLine:
    splitLine = nxtLine.split()
    classList = splitLine[4:]

    students[splitLine[0]] = Student(splitLine[0], splitLine[1], splitLine[2], splitLine[3], classList)

    nxtLine = inData.readline()

students["222"].addClass("ENG2345")
for x in students:
    outData.write(students[x].__str__())

inData.close()
outData.close()
