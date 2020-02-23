#from array import *


class LibrarianAdd:
    def __init__(self):
        self.bnm = []
        self.Fullbnmrecord = []
        self.FullAuthRec = []
        self.auth = []
    def inp(self):
        self.bnm.append(str(input("Enter name of book to add in library :- ")))
        self.auth.append(str(input("Enter name of author :- ")))
        self.Fullbnmrecord = list(self.bnm)
        self.FullAuthRec = list(self.auth)
    def check(self,nm):
        for i in self.bnm:
            if i == nm:
                return True
        return False
    def delb(self):
        delnm = str(input("Enter book name to delete from record :- "))
        self.bnm.remove(delnm)


class StudentBorrow(LibrarianAdd):
    def in_b_nm_check(self):
        self.booknm = str(input("Enter Name of book you wanna borrow :- "))
        chk = super().check(self.booknm)
        if chk == True:
            print("Book is available")
            self.borrow()
        else:
            print("Book not available")
    def borrow(self):
        self.BorrowedList = []
        self.BorrowedList.append(self.booknm)
        l = self.bnm.index(self.booknm)
        self.bnm.remove(self.booknm)
        print("You have borrowed book ",self.booknm)
        print("name of author of this book is ",self.auth.__getitem__(l))



