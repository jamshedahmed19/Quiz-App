# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:41:24 2021

@author: HP
"""

# DATA STRUCTURE CONCEPTS USED
# 1. BUBBLE SORT
# 2. BINARY SEARCH
# 3. STACK
# 4. LINEAR SEARCH
# 5. LINKED LIST
# 6. ARRAY
# 7. SELECTION SORT
# 8. DICTIONARY

import os
import linkedList


class Admin:
    def __init__(self):
        self.Id = 1234
        self.name = 'admin'

    def menu(self):
        stack.push(self.menu)
        while(True):
            print('\t\t\t***********************************************')
            print("\t\t\t           " + self.name.capitalize() + "! Welcome To Quiz App ")
            print('\t\t\t***********************************************')
            menu = {"1": "Generate Quiz", "2": "Delete Quiz", "3": "Log Out"}
            for key, value in menu.items():
                print("\t\t\t {}. {}".format(key, value))
            select = input("\tEnter Your Selection (1-4): ")
            if select == '1':
                self.generateQuiz()
            elif select == '2':
                self.deleteQuiz()
            elif select == '3':
                stack.pop()()
            else:
                print("Invalid Selection")

    def generateQuiz(self):
        quizname = str(input("Enter Quiz Name ? "))
        fx = open("quizzes.txt", "a+")
        fx.write(quizname + ",")
        fx.close()
        f = open(quizname + ".txt", "a+")
        numOfQs = int(input("How many Questions you want to add?"))
        for i in range(numOfQs):
            question = str(
                input("Enter Question Number " + str(i+1) + " out of 5 "))
            choice1 = str(input("Enter Choice Number 1 out of 4 "))
            choice2 = str(input("Enter Choice Number 2 out of 4 "))
            choice3 = str(input("Enter Choice Number 3 out of 4 "))
            choice4 = str(input("Enter Choice Number 4 out of 4 "))
            answer = str(input("Enter Correct Answer "))

            f.write(str(quizname) + ","
                    + str(question) + ","
                    + str(choice1) + ","
                    + str(choice2) + ","
                    + str(choice3) + ","
                    + str(choice4) + ","
                    + str(answer) + ","
                    + "\n")

        print("Quiz Successfully Generated")

    def deleteQuiz(self):
        data = []
        if(os.path.exists("quizzes.txt")):
            for line in open("quizzes.txt", "r").readlines():
                data = line.split(',')

                for i in range(len(data)-1):
                    print("\t" + str(i+1) + ". " + str(data[i]))

            select = int(input("\tEnter Your Option:"))
            quizName = data[select-1]
            prompt = input("\tDo you really want to delete? y or n")
            if(prompt == "y"):
                newdata = []
                if(os.path.exists(quizName+".txt")):
                    os.remove(quizName+".txt")
                    os.remove("quizzes.txt")
                    del data[select-1]
                    print(data)
                    print(len(data))
                    if (len(data) != 0):
                        filename = "quizzes.txt"
                        f = open(filename, "a+")
                        for i in range(len(newdata)):
                            f.write(str(newdata[i]) + ",")
        else:
            print("\tNo Quiz is Available")


class User:
    leaderBoard = linkedList.LinkedList()

    def __init__(self, userid, name, email, quizattempts, quizwon):
        self.userid = userid
        self.name = name
        self.email = email
        self.quizattempts = quizattempts
        self.quizwon = quizwon

    def userHome(self):
        stack.push(self.userHome)
        while(True):
            print('\n\t\t***********************************************')
            print("\t\t          " + self.name.capitalize() +
                  "! Welcome To Quiz App ")
            print('\t\t***********************************************')
            menu = {"1": "Start Quiz", "2": "Your Quizzes History", "3": "LeaderBoard", "4": "Log Out"}
            for key, value in menu.items():
                print("\t\t {}. {}".format(key, value))
            select = input("\tEnter Your Selection (1-4): ")
            if select == '1':
                self.selectQuiz()
            elif select == '2':
                self.showQuizHistory()
            elif select == '3':
                self.showLeaderboard()
            elif select == '4':
                stack.pop()()
            else:
                print('NOTE: SELECT CORRECT ACTION\n')

    def register(self):
        # will create Users.txt file it doen't already exists
        file = open("Users.txt", "a+")
        if(self.userAlreadyExist() == False):
            file.write(str(self.userid)
                       + "," + str(self.name) + ","
                       + str(self.email) + ","
                       + str(self.quizattempts)
                       + "," + str(self.quizwon) + "\n")
            print("\tSuccessFully Registered")
            file.close()
        else:
            print('\tThis ID is Already in Use')

    def userAlreadyExist(self):
        usersids = []

        if os.path.exists("Users.txt"):
            for line in open("Users.txt", "r").readlines():
                data = line.split(',')
                usersids.append(data[0])
        else:
            stack.pop()()

        # -------------- BUBBLE SORT USED HERE --------------
        bubbleSort(usersids)
        # -------------- BINARY SEARCH USED HERE --------------
        if(binarySearch(usersids, 0, len(usersids) - 1, self.userid) == False):
            return False
        else:
            return True

    def login(self):
        flag = 404
        admin = Admin()
        if(int(self.userid) == int(admin.Id) and str(self.name) == str(admin.name)):
            admin.menu()
        else:
            if(os.path.exists("Users.txt")):
                for line in open("Users.txt", "r").readlines():
                    data = line.split(',')
                    if(self.userid == data[0] and self.name == data[1]):
                        self.userid = data[0]
                        self.name = data[1]
                        self.email = data[2]
                        self.quizattempts = data[3]
                        self.quizwon = data[4]
                        self.userHome()
                    else:
                        flag = 404
            else:
                print("Error: No user found")
                stack.pop()()
        if(flag == 404):
            print("User doesn't Exist")

    def isAlreadyAttempted(self, quizname):
        file = str(self.userid) + "history.txt"
        if(os.path.exists(file)):
            for line in open(file, "r").readlines():
                data = line.split(',')
                if(quizname == data[0]):
                    return True
                else:
                    return False
        else:
            return False

    def showLeaderboard(self):
        for line in open("quizzes.txt", "r").readlines():
            data = line.split(',')

            for i in range(len(data)-1):
                print("\t" + str(i+1) + ". " + str(data[i]))
        # -------------- LINKED LIST USED HERE --------------
        self.leaderBoard = linkedList.LinkedList()
        self.getallmarks()
        # -------------- SELECTION SORT USED HERE --------------
        self.leaderBoard.selectionSort()
        select = int(input("\tEnter Your Option:"))
        quizname = data[select-1]
        for i in range(self.leaderBoard.getCount() - 1):
            for line in open("lb.txt", "r").readlines():
                datax = line.split(',')
                if(quizname == datax[0]):
                    if(str(self.leaderBoard.returnNthfromfirst(i+1)) == str(datax[3])):
                        print("\t" + str(datax[1]) + "   |   " +
                              str(datax[2])+"   |   " + str(datax[3]))
        choice = int(input("Press 1. Search By ID\n Press 2. Back: \n"))
        if(choice == 1):
            ids = []
            if os.path.exists("lb.txt"):
                for line in open("lb.txt", "r").readlines():
                    data = line.split(',')
                    ids.append(int(data[1]))
            ID = int(input("\t Enter Your ID"))
            if(linearsearch(ids, ID) == -1):
                print("\tNot Found")
            else:
                for line in open("lb.txt", "r").readlines():
                    datax = line.split(',')

                    if(int(datax[1]) == ID):
                        print("\t" + str(datax[1]) + "   |   " +
                              str(datax[2])+"   |   " + str(datax[3]))

    def getallmarks(self):
        if(os.path.exists("lb.txt")):
            for line in open("lb.txt", "r").readlines():
                data = line.split(",")
                self.leaderBoard.push(int(data[3]))

    def LeaderBoard(self, quizname, score):
        file = "lb.txt"
        f = open(file, "a+")
        f.write(str(quizname) + "," +
                str(self.userid) + "," +
                str(self.name) + "," +
                str(score) + ",\n")

    def showQuizHistory(self):
        file = str(self.userid) + "history.txt"
        print("\n")
        if(os.path.exists(file)):
            for line in open(file, "r").readlines():
                data = line.split(',')
                print("\t" + str(data[0]) + "   |   " + str(data[1]))
                self.searchQuizHistory(data)
        else:
            print('\tNo Quiz History Found Please attempt any Quiz')

        str(input("\n\tPress Any Key"))

    def searchQuizHistory(self, data):
        value = input("Enter Name of the Quiz")
        file = str(self.userid) + "history.txt"
        print("\n")
        if(os.path.exists(file)):
            for line in open(file, "r").readlines():
                data = line.split(',')
                # -------------- LINEAR USED HERE --------------
                if(linearsearch(data[0], value) != False):
                    print(linearsearch(data[0], value))
                else:
                    print("Value not found")
        else:
            print('\tNo Quiz History Found Please attempt any Quiz')

        str(input("\n\tPress Any Key"))

    def saveQuizHistory(self, quizname, score):
        filename = str(self.userid) + "history.txt"
        f = open(filename, "a+")
        f.write(str(quizname) + "," + str(score) + ",\n")

    def selectQuiz(self):
        i = 0
        for line in open("quizzes.txt", "r").readlines():
            data = line.split(',')

            for i in range(len(data)-1):
                print("\t" + str(i+1) + ". " + str(data[i]))

        select = int(input("\tEnter Your Option:"))
        if(select < i+1):
            if(self.isAlreadyAttempted(data[select-1]) == True):
                print("\tYou have Already Attempted This Quiz Please Try another")
                str(input("\tPress Any Key "))
                self.userHome()
            else:
                str(input("\tDo You Really want to Start ? "))
                quizname = data[select-1]
                filename = data[select-1] + ".txt"
                questionnumber = 0
                marks = 0
                if(os.path.exists(filename)):
                    for line in open(filename, "r").readlines():
                        data = line.split(',')
                        questionnumber += 1
                        print("\tQuestion Number " + str(questionnumber))
                        print("\t" + data[1])
                        print("\t\t1.  " + data[2])
                        print("\t\t2.  " + data[3])
                        print("\t\t3.  " + data[4])
                        print("\t\t4.  " + data[5])
    
                        answer = int(input("\tEnter Your Option Number: "))
                        answer += 1
                        if(data[answer] == data[6]):
                            marks += 1
                else:
                    print("Quiz doesn't Exist")
                result = int((marks/questionnumber) * 100)
                self.LeaderBoard(quizname, result)
                self.saveQuizHistory(quizname, result)
                print("\t Your Result is: " + str(result))
        else:
            print("Select correct option")
            


def start():
    stack.push(start)
    while(True):
        print('\t\t\t*****************************')
        print("\t\t\t           Main Menu")
        print('\t\t\t*****************************')
        menu = {"1": "Login", "2": "Register", "3": "LeaderBoard"}
        for key, value in menu.items():
            print("\t\t\t {}. {}".format(key, value))
        if(stack.isEmpty() == True):
            print("\n\t4. Back")
        print()
        select = input("Enter Your Selection (1-5): ")
        if select == '1':
            user = User(
                input("\tEnter Your ID:"),
                input("\tEnter Your Name:"),
                'none',
                0,
                0)
            user.login()
        elif select == '2':
            user = User(
                input("\tEnter Your ID:"),
                input("\tEnter Your Name:").lower(),
                input("\tEnter Your Email:"),
                0,
                0)
            user.register()
        elif select == '3':
            user = User(None, None, "None", None, None)
            user.showLeaderboard()
        elif select == '4':
            stack.pop()()
        elif select == '5':
            break
        else:
            print('NOTE: SELECT CORRECT ACTION\n')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False

    def push(self, data):
        if(self.isEmpty()):
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if(self.isEmpty()):
            print("is empty")
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if(self.isEmpty()):
            return None
        else:
            return self.head.data


def linearsearch(arr, value):

    for i in range(len(arr)):

        if int(arr[i]) == int(value):
            return i

    return False


def binarySearch(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if int(arr[mid]) == int(x):
            return arr[mid]
        elif int(arr[mid]) > int(x):
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
        return False


def insertionSort(arr):
    for i in range(1, len(arr)):
        currentVal = arr[i]
        position = i
        while position < 0 and arr[position - 1] < currentVal:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = currentVal

def bubbleSort(arr):
    for _pass in range(len(arr) - 1, 0, -1):
        for step in range(_pass):
            if( arr[step] > arr[step + 1]):
                temp = arr[step]
                arr[step] = arr[step + 1]
                arr[step + 1] = temp

stack = Stack()

print('\t*******************************************************')
print('\t\t       Q U I Z  A P P L I C A T I O N ')
print('\t*******************************************************')
# APP STARTS HERE
start()

