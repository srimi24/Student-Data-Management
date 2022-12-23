import tkinter

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from StudentProgram import *

mainwindow = tkinter.Tk()
mainwindow.title("Student Database Management")

mainwindow.geometry("600x500")

labelUSN = Label(mainwindow, text = "USN").place(x=30, y=50)
usnStr = StringVar()
entryUSN = Entry(mainwindow, textvariable=usnStr)
entryUSN.place(x=150, y=50)

labelFN = Label(mainwindow, text = "First Name").place(x=30, y=90)
fnStr = StringVar()
entryFN = Entry(mainwindow, textvariable=fnStr)
entryFN.place(x=150, y=90)

labelMI = Label(mainwindow, text = "MI").place(x=30, y=130)
miStr = StringVar()
entryMI = Entry(mainwindow, textvariable=miStr)
entryMI.place(x=150, y=130)

labelLN = Label(mainwindow, text = "Last Name").place(x=30, y=170)
lnStr = StringVar()
entryLN = Entry(mainwindow, textvariable=lnStr)
entryLN.place(x=150, y=170)

labelMM = Label(mainwindow, text = "Mathematics Marks").place(x=30, y=210)
mmStr = StringVar()
entryMM = Entry(mainwindow, textvariable = mmStr)
entryMM.place(x=150, y=210)

labelPM = Label(mainwindow, text = "Physics Marks").place(x=30, y=250)
pmStr = StringVar()
entryPM = Entry(mainwindow, textvariable = pmStr)
entryPM.place(x=150, y=250)

labelCM = Label(mainwindow, text = "Chemistry Marks").place(x=30, y=290)
cmStr = StringVar()
entryCM = Entry(mainwindow, textvariable = cmStr)
entryCM.place(x=150, y=290)

labelCSM = Label(mainwindow, text = "Computer Sc. Marks").place(x=30, y=330)
csmStr = StringVar()
entryCSM = Entry(mainwindow, textvariable = csmStr)
entryCSM.place(x=150, y=330)

labelEM = Label(mainwindow, text = "English Marks").place(x=30, y=370)
emStr = StringVar()
entryEM = Entry(mainwindow, textvariable = emStr)
entryEM.place(x=150, y=370)

labelSM = Label(mainwindow, text = "Semester").place(x=30, y=410)
semisterValues = ('Semester-1', 'Semester-2', 'Semester-3', 'Semester-4', 'Semester-5', 'Semister-6', 'Semester-7', 'Semester-8')
semisterStr = StringVar()
comboboxSM = Combobox(mainwindow, values=semisterValues, textvariable = semisterStr, state='readonly')
comboboxSM.place(x=150, y=410)


    
def createbuttonclicked():
    if not usnStr.get().isdigit():
        messagebox.showinfo("USN Error", "Please enter only numerics")
        entryUSN.focus()
        return
    
    if not fnStr.get().isalpha():
        messagebox.showinfo("First Name Error", "Please enter only alphabets")
        entryFN.focus()
        return

    if miStr.get():
        if not miStr.get().isalpha():
            messagebox.showinfo("MI Error", "Please enter only alphabets")
            entryMI.focus()
            return

    if not lnStr.get().isalpha():
        messagebox.showinfo("Last Name Error", "Please enter only alphabets")
        entryLN.focus()
        return

    if not mmStr.get().isdigit():
        messagebox.showinfo("Mathematics marks Error", "Please enter only numerics")
        entryMM.focus()
        return

    if not pmStr.get().isdigit():
        messagebox.showinfo("Physics marks Error", "Please enter only numerics")
        entryPM.focus()
        return

    if not cmStr.get().isdigit():
        messagebox.showinfo("Chemistry marks Error", "Please enter only numerics")
        entryCM.focus()
        return

    if not csmStr.get().isdigit():
        messagebox.showinfo("Computer Sc. marks Error", "Please enter only numerics")
        entryCSM.focus()
        return

    if not emStr.get().isdigit():
        messagebox.showinfo("English marks Error", "Please enter only numerics")
        entryEM.focus()
        return

    if "".__eq__(semisterStr.get()):
        messagebox.showinfo("Semester Error", "Please select semester")
        comboboxSM.focus()
        return

    studentRecord = ""
    studentRecord = usnStr.get() + ","  \
                    + fnStr.get() + "," \
                    + miStr.get() + "," \
                    + lnStr.get() + "," \
                    + mmStr.get() + "," \
                    + pmStr.get() + "," \
                    + cmStr.get() + "," \
                    + csmStr.get() + ","    \
                    + emStr.get() + "," \
                    + semisterStr.get() \
                    + "\n"

    #print(studentRecord)

    sl = StudentList()
    student = sl.search_student_record(usnStr.get())

    if(student == None):
        sl.create_student_record(studentRecord)
        messagebox.showinfo("USN Success", "Student created successfully")
    else:
        messagebox.showinfo("USN Error", "USN already exists!")
        
def searchbuttonclicked():
    if "".__eq__(usnStr.get()) or not(usnStr.get().isdigit()):
        messagebox.showinfo("USN Error", "Please enter only numerics")
        return
    else:
        sl = StudentList()
        student = sl.search_student_record(usnStr.get())

        if student == None:
            messagebox.showinfo("USN Error", "No USN found!")
        else:
            usnStr.set(student.USN)
            fnStr.set(student.FirstName)
            miStr.set(student.MiddleInitial)
            lnStr.set(student.LastName)
            mmStr.set(student.mathmarks)
            pmStr.set(student.physicsmarks)
            cmStr.set(student.chemistrymarks)
            csmStr.set(student.CSmarks)
            emStr.set(student.englishmarks)
            semisterStr.set(student.semester)

    
def deletebuttonclicked():
    if "".__eq__(usnStr.get()) or not(usnStr.get().isdigit()):
        messagebox.showinfo("USN Error", "Please enter valid USN")
        return
    else:
        sl = StudentList()
        returnVal = sl.delete_student_record(usnStr.get())

        if returnVal == -1:
            messagebox.showinfo("USN Error", "USN does not exists!")
    
        usnStr.set("")
        fnStr.set("")
        miStr.set("")
        lnStr.set("")
        mmStr.set("")
        pmStr.set("")
        cmStr.set("")
        csmStr.set("")
        emStr.set("")
        semisterStr.set("")

def averageofallstudentsbuttonclicked():
    sl = StudentList()
    strReturn = sl.average_of_all_students()
    messagebox.showinfo("", strReturn)

def averagegreaterthanvaluebuttonclicked():
    if not aggvStr.get().isdigit():
        messagebox.showinfo("Avergae greater than given value", "Please enter only numerics")
        entryAGGV.focus()
    else:
        sl = StudentList()
        strReturn = sl.average_of_all_students(int(aggvStr.get()))
        messagebox.showinfo("", strReturn)
        return


def studentswhofailedbuttonclicked():
    sl = StudentList()
    strReturn = sl.students_who_failed_atleast_in_one_subject()
    messagebox.showinfo("", strReturn)

def studentswhopassedbuttonclicked():
    sl = StudentList()
    strReturn = sl.students_who_passed_in_all_subjects()
    messagebox.showinfo("", strReturn)

'''def displaydataclicked():
    sl = StudentList()
    strReturn = sl.displaydata()
    messagebox.showinfo("",strReturn)'''
def displaybuttonclicked():
    sl = StudentList()
    strReturn = sl.displaydata()
    messagebox.showinfo("",strReturn)
            
    


searchButton = Button(mainwindow, text = "Search Student", command = searchbuttonclicked).place(x=320, y=50)
createButton = Button(mainwindow, text = "Create New Student", command = createbuttonclicked).place(x=320, y=120)
deleteButton = Button(mainwindow, text = "Delete Student", command = deletebuttonclicked).place(x=320, y=170)
DisplaystudentButton = Button(mainwindow, text = "Display Data",command = displaybuttonclicked).place(x=320,y=220)
averageofallstudentsButton = Button(mainwindow, text = "Find Average of all Students", command = averageofallstudentsbuttonclicked).place(x=320, y=250)
averagegreaterthanvalueButton = Button(mainwindow, text = "Average greater than given value", command = averagegreaterthanvaluebuttonclicked).place(x=320, y=300)
aggvStr = StringVar()
entryAGGV = Entry(mainwindow, textvariable = aggvStr, width = 3)
entryAGGV.place(x=510, y=300)

studentswhofailedButton = Button(mainwindow, text = "Students who failed in atleast 1 subject", command = studentswhofailedbuttonclicked).place(x=320, y=350)
studentswhopassedButton = Button(mainwindow, text = "Students who passed in all subjects", command = studentswhopassedbuttonclicked).place(x=320, y=400)

mainwindow.mainloop()
