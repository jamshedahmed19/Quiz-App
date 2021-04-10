# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:41:24 2021

@author: HP
"""

import os


class Admin:
    
    def __init__(self):
        self.Id=1234
        self.name='admin'
    

    def WelcomeAdmin(self):
        while(True):
            print('\t\t\t***********************************************')
            print("\t\t\t           "+ self.name+ "! Welcome To Quiz App ")
            print('\t\t\t***********************************************')
            
            print ("\t1. Generate Quiz   \n\t2. Delete Quiz \n\t3. Log Out")
            print()
            select=input("\tEnter Your Selection (1-4): ")
            if select=='1':
                self.GenerateQuiz()
            
            elif select=='2':
                
                user= User(
                    input("\tEnter Your ID:"),
                    input("\tEnter Your Name:"),
                    input("\tEnter Your Email:"),
                    0,
                    0)
                user.Register()
                
            elif select=='3':
                break
            
    def GenerateQuiz(self):
        quizname = str(input("Enter Quiz Name ? "))
        fx = open("quizzes.txt","a+")
        fx.write(quizname + ",")
        fx.close()
        f = open(quizname + ".txt","a+")  
        for i in range(5):
            question =str(input("Enter Question Number " + str(i+1) + " out of 5 " ))
            choice1 = str(input("Enter Choice Number 1 out of 4 " ))
            choice2 = str(input("Enter Choice Number 2 out of 4 " ))
            choice3 = str(input("Enter Choice Number 3 out of 4 " ))
            choice4 = str(input("Enter Choice Number 4 out of 4 " ))
            answer = str(input("Enter Correct Answer " ))
            
            f.write(str(quizname) + "," 
                    + str(question)+ "," 
                    + str(choice1) +"," 
                    + str(choice2) +"," 
                    + str(choice3) +"," 
                    + str(choice4) +"," 
                    + str(answer) +"," 
                    + "\n")
            
        print("Quiz Successfully Generated")
            
        
class User:
    def __init__(self,userid,name,email,quizattempts,quizwon):
        self.userid=userid
        self.name=name.lower()
        self.email=email
        self.quizattempts=quizattempts
        self.quizwon=quizwon
    
    def WelcomeUser(self):
        while(True):
            print('\t\t\t***********************************************')
            print("\t\t\t           "+ self.name+ "! Welcome To Quiz App ")
            print('\t\t\t***********************************************')
            
            print ("\t1. Start Quiz   \n\t2. Your Quizzes History \n\t3. LeaderBoard \n\t4. Log Out")
            print()
            select=input("\tEnter Your Selection (1-4): ")
            if select=='1':
                self.SelectQuiz()
            
                
                    
                    
            elif select=='2':
                
                self.ShowQuizHistory()
            elif select=='3':
                self.ShowLeaderBoard()
                
            elif select=='4':
                start()
                break
            else:
                print("\tWrong Input")
                
                
    def Register(self):
        f = open("Users.txt","a+")
        #Searching Algorithm Can Be Applied Here to Search
        if(True):
            f.write(str(self.userid) 
                    + "," + str(self.name)+ "," 
                    + str(self.email) +"," 
                    + str(self.quizattempts) 
                    +"," + str(self.quizwon) + "\n")   
            print("\tSuccessFully Registered")
            f.close() 
        else:
            print('\tThis ID is Already in Use')
            
            
    def Login(self):
        x=''
        admin=Admin()
        if(int(self.userid) == int(admin.Id) and str(self.name)== str(admin.name)):
            admin.WelcomeAdmin()
        else:
            for line in open("Users.txt", "r").readlines():
                data = line.split(',')
                if(self.userid==data[0] and self.name == data[1]):
                    self.userid = data[0]
                    self.name = data[1]
                    self.email =data[2]
                    self.quizattempts = data[3]
                    self.quizwon = data[4]
                    self.WelcomeUser()
                else:
                    x = 'notfound'
        if(x=='notfound'):
            print("\tInvalid ID or Password")
                    
    def IsQuizAttempted(self,quizname):
        file= str(self.userid)+ "history.txt"
        if(os.path.exists(file)):
            for line in open(file, "r").readlines():
                    data = line.split(',')
                    if(quizname==data[0]):
                        return True
                    else:
                        return False
        else:
            return False
    def ShowLeaderBoard(self):
        for line in open("quizzes.txt", "r").readlines():
            data=line.split(',')
           
            for i in range(len(data)-1):
                print("\t"+ str(i+1) +". "+  str(data[i]))
         
        select = int(input("\tEnter Your Option:")) 
        quizname = data[select-1]
        for line in open("lb.txt", "r").readlines():
            data=line.split(',')
            if(quizname==data[0]):
                print("\t"+ str(data[1]) +"   |   "+  str(data[2])+"   |   "+  str(data[3]))
                
        str(input("Press Any Key"))
                
        
    def LeaderBoard(self,quizname,score):
        file= "lb.txt"
        f = open(file,"a+")
        f.write(str(quizname) + "," + 
                str(self.userid)+ "," + 
                str(self.name) +"," + 
                str(score) +"\n" )
        
    def ShowQuizHistory(self):
        file= str(self.userid)+ "history.txt"
        print("\n")
        if(os.path.exists(file)):
            for line in open(file, "r").readlines():
                data=line.split(',')
                print("\t"+ str(data[0]) +"   |   "+  str(data[1]))
        else:
            print('\tNo Quiz History Found Please attempt any Quiz')
        
        str(input("\n\tPress Any Key"))
                
        
    def saveQuizHistory(self,quizname,score):
        filename = str(self.userid) + "history.txt"
        f = open(filename,"a+")
        f.write(str(quizname) + "," + str(score)+ "%\n")
                
        
    def SelectQuiz(self):
        
        for line in open("quizzes.txt", "r").readlines():
            data=line.split(',')
            
            for i in range(len(data)-1):
                print("\t"+ str(i+1) +". "+  str(data[i]))
                
        select = int(input("\tEnter Your Option:"))
        if(self.IsQuizAttempted(data[select-1])==True):
            print("\tYou have Already Attempted This Quiz Please Try another")
            str(input("\tPress Any Key "))
            self.WelcomeUser()
        else:
            str(input("\tDo You Really want to Start ? "))
            quizname= data[select-1]
            filename = data[select-1] + ".txt"
            questionnumber = 0
            marks= 0
            #if path exist
            for line in open(filename, "r").readlines():
                data=line.split(',')
                questionnumber+=1
                print("\tQuestion Number " + str(questionnumber))
                print("\t" + data[1])
                print("\t\t1.  " + data[2])
                print("\t\t2.  " + data[3])
                print("\t\t3.  " + data[4])
                print("\t\t4.  " + data[5])
                
                answer= int(input("\tEnter Your Option Number: "))
                answer+=1
                if(data[answer]==data[6]):
                    marks+=1
            
            result = (marks/questionnumber) *100
            self.LeaderBoard(quizname,result)
            self.saveQuizHistory(quizname,result)
            print("\t Your Result is: " + str(result))
            
            
        
            
                
        
            
    
                 

print('*******************************************************')
print('       Q U I Z            A P P L I C A T I O N')
print('*******************************************************')
def start():
    
    while(1):
        print('\t\t\t*****************************')
        print("\t\t\t           Main Menu")
        print('\t\t\t*****************************')
        
        
        print ("\t1. Login  \n\t2. Register \n\t3. Exit")
        print()
        select=input("Enter Your Selection (1-3): ")
        if select=='1':
            
            user= User(
                input("\tEnter Your ID:"),
                input("\tEnter Your Name:"),
                'none',
                0,
                0)
         
            user.Login()
                
                
            
                
        elif select=='2':
            
            user= User(
                
                input("\tEnter Your ID:"),
                input("\tEnter Your Name:"),
                input("\tEnter Your Email:"),
                0,
                0)
            
            user.Register()
            
        elif select=='3':
            
            break
        
        else:
            print('Wrong Input')
            
            

start()