# Exercise 6.9
dataFile = 0
def openFile(op):
    global dataFile
    if op == 'r':
        dataFile = open("studentInfo.dat", 'r')
    elif op == 'a':
        dataFile = open("studentInfo.dat", 'a')
    elif op == 'w':
        dataFile = open("studentInfo.dat", 'w')
def saveFile():
    global dataFile
    dataFile.close()

def addItem():
    global dataFile
    openFile('a')
    studentID = int(input("Enter student ID: <9-long-number>: >>> "))
    if studentID < 100000000 or studentID > 999999999:
        return
    studentName = raw_input("Enter student name: >>> ")
    if studentName == '':
        return
    studentAge = int(input("Enter student age: >>> "))
    if studentAge <= 0 or studentAge >= 100:
        return
    dataFile.write(str(studentID) + '\n')
    dataFile.write(str(studentName) + '\n')
    dataFile.write(str(studentAge) + '\n')
    saveFile()

def readItem():
    global dataFile
    allStudent = []
    openFile('r')
    item = 0
    while item != "":
        tempList = []
        for i in range(3):
            item = dataFile.readline()
            tempList.append(item)
        allStudent.append(tempList)
        item = dataFile.readline()
    return allStudent
    saveFile()

def deleteItem():
    ID = input("Input the student's ID you want to delete: >>> ")
    newStudents = []
    students = readItem()
    openFile('w')
    for i in students
        
    return
def searchItem():
    return

def main():
    print "This program can manage students' info."
    while True:
        print "Enter <1> to add an item..."
        print "Enter <2> to delete an item..."
        print "Enter <3> to search an item..."
        print "Enter <4> to quit..."
        operationFlag = raw_input(">>> ")
        if operationFlag == '1':
            addItem()
        elif operationFlag == '2':
            deleteItem()
        elif operationFlag == '3':
            searchItem()
        elif operationFlag == '4':
            break
        print '-------------------------------------'
main()
