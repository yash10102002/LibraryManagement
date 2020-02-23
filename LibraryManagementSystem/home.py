
from Library import *

s1 = StudentBorrow()
while True:
    print("Login as")
    print("1.Student")
    print("2.Librarian")
    print("3.Register Student")
    print("4.Exit")
    ch = int(input("Enter Choice :- "))

    if ch == 1:
        id = str(input("Username:"))
        pas = str(input("password:"))
        #name of file containing all student id's is Studid
        studi = open("Studid.txt",'r')
        #name of file containing all passwords of student is Studpass
        studp = open("Studpass.txt",'r')

        #this loop validates student id
        for i in studi:
            if id == i:
                chk1 = True
            else:
                chk1 = False
        #this loop validates password
        for i in studp:
            if pas == i:
                chk2 = True
            else:
                chk2 = False
        if chk1 == True and chk2 == True:
            while True:
                s1.in_b_nm_check()
                ch = str(input("Do you want To log out(y/n)?"))
                if ch == "y":
                    break
        elif chk1 == True and chk2 == False:
            print("Incorrect password")
        elif chk1 == False and chk2 == True:
            print("Incorrect username")
        else:
            print("Incorrect Details")

    elif ch == 2:
        #This is librarian account
        while True:
            print("\n1.add new Book\n2.check book availability \n3.delete book record")
            ch = int(input("Enter your choice :-"))
            if ch == 1:
                s1.inp()
            elif ch == 2:
                s1.check()
            else:
                s1.delb()
            ch = str(input("Do you want to log out(y/n)?"))
            if ch == "y":
                break


    elif ch == 3:
        #In this we will register new student and save his details in files
        name = str(input("Enter Student name :- "))
        roll = int(input("Enter Roll no:"))
        uid = str(input("Enter User id you want:"))
        while True:
            p1 = str(input("Enter password:"))
            p2 = str(input("Conform password:"))
            if p1 != p2:
                pass
            else:
                break
        file = open("StudData",'a')
        file.write(name)
        file.write("\n"+str(roll))
        file.write("\n"+uid)
        file.write("\n"+p1)
    else:
        break



