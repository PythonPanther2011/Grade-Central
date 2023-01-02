from statistics import mean
import os

username = ""
students = {}
do = ""
admins = open("Python rocks.txt", "r").read()
admins = eval(admins)

def replaceGrade(student):
    global username
    name = gettingValue("student", " that you would like to change the grade of?")
    if backstep(name) == "backstep":
        return
    subject = gettingValue("subject", " that you like change the grade in?", name)
    if backstep(subject) == "backstep":
        return
    dic = student[name]
    while len(dic[subject]) == 0:
        print("Sorry, you do not have any grades in this subject.")
        subject = gettingValue("subject", " that you like change the grade in?", name)
        if backstep(subject) == "backstep":
            return

    gradeToReplace = input("What is the grade you would like to replace?: ")
    if backstep(gradeToReplace) == "backstep":
        return
    while gradeToReplace.isalpha():
        print("Sorry, this grade is invalid.")
        gradeToReplace = input("What is the grade you would like to replace/delete?: ")
        if backstep(gradeToReplace) == "backstep":
            return
    else:
        gradeToReplace = int(gradeToReplace)

    while gradeToReplace not in dic[subject]:
        print("Sorry, this student does not have this grade in this subject.")
        gradeToReplace = input("What is the grade you would like to replace?: ")
        if backstep(gradeToReplace) == "backstep":
            return
        if gradeToReplace in dic[subject]:
            break

    grade = input("What grade would you like to replace it with? (You can type d to delete the grade.): ")
    if backstep(grade) == "backstep":
        return
    if grade == "d":
        dic[subject].remove(gradeToReplace)
        return

    while grade.isalpha():
        grade = input("What grade would you like to replace it with? (You can type d to delete the grade.): ")
        if backstep(grade) == "backstep":
            return
        if grade == "d":
            break
    if grade == "d":
        dic[subject].remove(gradeToReplace)
        print("Deleting grade.....")
        return
    elif grade.isdigit():
        grade = int(grade)

    dic[subject].remove(gradeToReplace)
    dic[subject].append(grade)
    saveFile(student, username)
    print("Replacing grade.....")


def IsThereAStudent(what):
    if len(students) == 0:
        if username == "Python rocks":
            print("Sorry, there are no accounts to " + what + ".")
            return "continue"
        else:
            print("Sorry, you do not have any students to " + what + ".")
            return "continue"

def backstep(entry):
    if entry == "B":
        return "backstep"

def Invalid(what):
    print("""Invalid """ + what + """!
Shutting down.....""")
    exit()

def ERROR(special, entry, what, inWhat):
    if backstep(entry) == "backstep":
        return
    while entry not in inWhat:
        print("Sorry, this " + what + " does not exist. Please try another " + what + ".\n")
        entry = input("What is the name of the " + what + special + ":").capitalize()
        if backstep(entry) == "backstep":
            return
        return entry

def whatCanYouDo(what):
    print("Type D to delete a " + what + ".\n")
    print("Type R to look at a " + what + ".\n")
    print("Type S to switch account.\n")
    print("Type E to exit out of Grading system.\n")
    print("(You can always type b if you do not want to do that choice.)")

def saveFile(save, usern):
    editFile = open(usern + ".txt", "w")
    editFile.write(str(save))
    editFile.close()

def gettingValue(what, special, entry = None):
    need = input("What is the name of the " + what + special + ":").capitalize()
    if backstep(need) == "backstep":
        return need

    if what == "subject":
        ERROR(special, need, what, students[entry])
    elif what == "student" or what == "account":
        ERROR(special, need, what, students)
    return need

def create():
    who = input("What is the students name?: ").capitalize()
    if backstep(who) == "backstep":
        return
    if who in students:
        print("Sorry, this student already exists.")
        who = input("What is the students name?: ").capitalize()
        if backstep(who) == "backstep":
            return
    print("Creating student.....")
    students[who] = {"Math": [], "Science": [], "Reading": [], "Social studies": []}
    saveFile(students, username)

def delete():
    if username == "Python rocks":
        who = gettingValue("account", " you would like to delete?")
        if backstep(who) == "backstep":
            return
        print("Deleting account.....")
        del students[who]
        os.remove(who + ".txt")
    else:
        who = gettingValue("student", " you would like to delete?")
        if backstep(who) == "backstep":
            return
        print("Deleting account.....")
        del students[who]
    saveFile(students, username)

def getOut():
    print("Shutting down.....")
    exit()

def add(student):
    who = gettingValue("student", " you would like to add this grade to?")
    if backstep(who) == "backstep":
        return
    subject = gettingValue("subject", " you would like to enter this grade in?", who)
    if backstep(subject) == "backstep":
        return
    grade = input("What is the student's grade?: ")
    if backstep(grade) == "backstep":
        return
    while grade.isalpha():
        print("ERROR! Please enter a valid grade.")
        grade = input("What is the student's grade?: ")
        if backstep(grade) == "backstep":
            return
    print("Adding grade.....")
    grade = int(grade)
    dictionary = student[who]
    dictionary[subject].append(grade)
    saveFile(students, username)

def read(student):
    if username == "Python rocks":
        print(students)
    else:
        who = input("What is the students name (You can put all to read all of the students.)?: ").capitalize()
        if backstep(who) == "backstep":
            return
        if who == "All":
            print(students)
        elif who not in students:
            print("Sorry, this student does not exist. Please try another student.\n")
            who = input("What is the students name?: ")
            if backstep(who) == "backstep":
                return
        else:
            print(student[who])

def average(student):
    name = gettingValue("student", " you would like to get the average of?")
    if backstep(name) == "backstep":
        return
    subject = gettingValue("subject", " you would like to get the average of?", name)
    if backstep(subject) == "backstep":
        return
    dic = student[name]
    avg = mean(dic[subject])
    print("Checking average of student.....")
    print(int(avg))

def user():
    global username
    username = input("Username(or type N to create a new account.): ")
    if username == "N" or username in admins:
        if username == "N":
            newAccount = input("What would you like your username to be?: ")
            while newAccount in admins:
                print("This username is already taken. Please try a different username.")
                newAccount = input("What would you like your username to be?: ")
            newAccountPassword = input("What would you like your password to be?: ")
            admins[newAccount] = newAccountPassword
            write = "{}"
            newFile = open(newAccount + ".txt", "w")
            newFile.write(write)
            newFile.close()
            saveUsers = open("Python rocks.txt", "w")
            saveUsers.write(str(admins))
            saveUsers.close()
            exit()
    else:
        Invalid("Username")

def passw(usern):
    password = input("Password(or type R to reset your password.): ")
    who = admins[usern]
    if password == "R" or who == password:
        if password == "R":
            usernameToUnlock = input("Please type in your username: ")
            while usernameToUnlock not in admins:
                print("Invalid username! Please try again.")
                usernameToUnlock = input("Please type in your username: ")
            newPassword = input("What would you like your new password to be?: ")
            admins[username] = newPassword
            saveFile(admins, "Python rocks")
            exit()
    else:
        Invalid("Password")

def setUp():
    global students
    students = open(username + ".txt", "r").read()
    students = eval(students)

    if username == "Python rocks":
        whatCanYouDo("account")
    else:
        print("Type C to add a student.\n")
        print("Type A to add a grade.\n")
        print("Type Avg to get the average of a student.\n")
        print("Type RD to replace/delete a student's grade.\n")
        whatCanYouDo("student")

def whatWouldYou():
    global do
    print("\n")
    do = input("What would you like to do?").lower()

def switching():
    print("Thank you for using Grade central.\n")
    print("Switching accounts......\n")

while True:
    print("Welcome to Grade Central.")
    user()
    passw(username)
    setUp()

    while True:
        whatWouldYou()

        if do == "c":
            create()

        elif do == "a":
            if IsThereAStudent("add a grade to") == "continue":
                continue
            add(students)

        elif do == "d":
            if IsThereAStudent("delete") == "continue":
                continue
            delete()

        elif do == "avg":
            if IsThereAStudent("check the average of") == "continue":
                continue
            average(students)

        elif do == "r":
            if IsThereAStudent("read the grades of") == "continue":
                continue
            read(students)

        elif do == "rd":
            if IsThereAStudent("replace/delete the grade of") == "continue":
                continue
            replaceGrade(students)

        elif do == "s":
            switching()
            break

        elif do == "e":
            getOut()

        else:
            print("This is not one of the options. Please try a different option.")
