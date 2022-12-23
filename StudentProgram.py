class Student:
    def __init__(self,  \
                 USN, \
                 FirstName, \
                 MiddleInitial, \
                 LastName,  \
                 mathmarks,   \
                 physicsmarks,   \
                 chemistrymarks, \
                 CSmarks,  \
                 englishmarks,   \
                 semester):
        self.USN = USN
        self.FirstName = FirstName
        self.MiddleInitial = MiddleInitial
        self.LastName = LastName

        self.mathmarks = mathmarks
        self.physicsmarks = physicsmarks
        self.chemistrymarks = chemistrymarks
        self.CSmarks = CSmarks
        self.englishmarks = englishmarks
        self.semester = semester

        self.mathavg = 0
        self.phyavg = 0
        self.cheavg = 0
        self.csavg = 0
        self.engavg = 0
    
class StudentList:
    def __init__(self):
        self.studentlist=[]


    def fetch_student_records(self):
        self.studentlist = []
        
        file = open("Student Data.txt",'r')
        eof = False
        while not eof:
            filedata=file.readline()
            filedata = filedata.strip()
            #print(filedata)
            if not filedata:
                eof = True
            else:
                
                lst = filedata.split(',')
                #print(lst[0])
                student1 = Student(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9])
                
                self.studentlist.append(student1)

        file.close()

    #def displaydata():
        #s = self.fetch_student_records()
    #print(s)

    def search_student_record(self, usn):
        self.fetch_student_records()
        
        for student in self.studentlist:
            if(int(student.USN) == int(usn)):
                return student
        
        
    def create_student_record(self,s):
#        studentrecord = s.USN + ',' + s.FirstName + ',' + s.MiddleInitial + ',' + s.LastName + ',' + \
#                        str(s.mathmarks) + ',' + str(s.physicsmarks) + ',' + str(s.chemistrymarks) + ',' \
#                        + str(s.CSmarks) + ',' + str(s.englishmarks) + ',' + s.semester
        
        file = open("Student Data.txt",'a')
        filedata=file.write(s)
        file.close()

    def write_student_records(self):
        file = open("Student Data.txt",'w')

        for i in range(0,len(self.studentlist)):
            s=self.studentlist[i]
            
            studentrecord = s.USN + ',' + s.FirstName + ',' + s.MiddleInitial + ',' + s.LastName + ',' + \
                        str(s.mathmarks) + ',' + str(s.physicsmarks) + ',' + str(s.chemistrymarks) + ',' \
                        + str(s.CSmarks) + ',' + str(s.englishmarks) + ',' + s.semester + '\n'
        
            filedata=file.write(studentrecord)

        file.close()

    def displaydata(*self):
        '''file = open("Student Data.txt",'r')
        studentdata = file.read()
        file.close()
        return studentdata'''
        self.fetch_student_records()
        for s in self.studentlist:
            strRet = s.USN + ' '+ s.FirstName + ' ' +s.MI   \
                     + ' ' +s.LastNAme + ' ' + s.mathmarks + ' ' + s.physicsmarks + ' ' \
                     + s.chemistrymarks + ' ' +s.CSmarks + ' ' + s.englishmarks + ' '+ s.semester
            return displaydata()
        
        
    def delete_student_record(self,dUSN):
        self.fetch_student_records()

        popnumber = -1
        
        for i in range(0,len(self.studentlist)):
            s=self.studentlist[i]
            if dUSN == s.USN:
                popnumber = i

        if popnumber != -1:
            self.studentlist.pop(popnumber)
            self.write_student_records()
        else:
            return popnumber

    def find_average_of_all_students(self):
        self.fetch_student_records()

        self.mathavg = 0
        self.phyavg = 0
        self.cheavg = 0
        self.csavg = 0
        self.engavg = 0

        nStudents = len(self.studentlist)
        
        for i in range(0,len(self.studentlist)):
            s=self.studentlist[i]
            
            self.mathavg += int(s.mathmarks)
            self.phyavg += int(s.physicsmarks)
            self.cheavg += int(s.chemistrymarks)
            self.csavg += int(s.CSmarks)
            self.engavg += int(s.englishmarks)
            
        self.mathavg /= nStudents
        self.phyavg /= nStudents
        self.cheavg /= nStudents
        self.csavg /= nStudents
        self.engavg /= nStudents

        #print(self.mathavg)
        #print(self.phyavg)
        #print(self.cheavg)
        #print(self.csavg)
        #print(self.engavg)


    def average_of_all_students(self, givenvalue = -1):
        
        if givenvalue == -1:
            self.find_average_of_all_students()
            mathavg = self.mathavg
            phyavg = self.phyavg
            cheavg = self.cheavg
            csavg = self.csavg
            engavg = self.engavg
        else:
            self.fetch_student_records()
            mathavg = givenvalue
            phyavg = givenvalue
            cheavg = givenvalue
            csavg = givenvalue
            engavg = givenvalue
        
        mathavglist = []
        phyavglist = []
        cheavglist = []
        csavglist = []
        engavglist = []

        for i in range(0,len(self.studentlist)):
            s=self.studentlist[i]
            
            if(int(s.mathmarks) >= mathavg):
                mathavglist.append(s)            
            if(int(s.physicsmarks) >= phyavg):
                phyavglist.append(s)
            if(int(s.chemistrymarks) >= cheavg):
                cheavglist.append(s)    

            if(int(s.CSmarks) >= csavg):
                csavglist.append(s)
            if(int(s.englishmarks) >= engavg):
                engavglist.append(s)

        if givenvalue == -1:
            strReturn = "Students who scored above average:\n\n\n"
        else:
            strReturn = "Students who scored above the given average value:" + str(givenvalue) + "\n\n\n"

        if givenvalue == -1:
            strReturn += "Math avg: " + str(mathavg) + "\n"
        else:
            strReturn += "Math: \n"
        for i in range(0,len(mathavglist)):
            s=mathavglist[i]
            strReturn += ' Name :' + s.FirstName.strip("\"") + ' ' + s.LastName.strip("\"") + ' scored :' + str(s.mathmarks) + "\n"
        

        strReturn += "\n"
        if givenvalue == -1:
            strReturn += "Physics avg: " + str(phyavg) + "\n"
        else:
            strReturn += "Physics: \n"
        for i in range(0,len(phyavglist)):
            s=phyavglist[i]
            strReturn += ' Name :' + s.FirstName.strip("\"") + ' ' + s.LastName.strip("\"") + ' scored :' + str(s.physicsmarks) + "\n"
 
        strReturn += "\n"
        if givenvalue == -1:
            strReturn += "Chemistry avg: " + str(cheavg) + "\n"
        else:
            strReturn += "Chemistry: \n"
        for i in range(0,len(cheavglist)):
            s=cheavglist[i]
            strReturn += ' Name :' + s.FirstName.strip("\"") + ' ' + s.LastName.strip("\"") + ' scored :' + str(s.chemistrymarks) + "\n"

        strReturn += "\n"
        if givenvalue == -1:
            strReturn += "Computer Science avg: " + str(csavg) + "\n"
        else:
            strReturn += "Computer Science:\n"            
        for i in range(0,len(csavglist)):
            s=csavglist[i]
            strReturn += ' Name :' + s.FirstName.strip("\"") + ' ' + s.LastName.strip("\"") + ' scored :' + str(s.CSmarks) + "\n"
        
        strReturn += "\n"

        if givenvalue == -1:
            strReturn += "English avg: " + str(engavg) + "\n"
        else:
            strReturn += "English: \n"        
        for i in range(0,len(engavglist)):
            s=engavglist[i]
            strReturn += ' Name :' + s.FirstName.strip("\"") + ' ' + s.LastName.strip("\"") + ' scored :' + str(s.englishmarks) + "\n"

        return strReturn;

    def students_who_failed_atleast_in_one_subject(self):
        self.fetch_student_records()

        passmarks = 35
        
        studentdict = {}

        for s in self.studentlist:

            name = s.FirstName + s.MiddleInitial + s.LastName

            if(int(s.mathmarks) < passmarks):
                studentdict[name] = 1            
            if(int(s.physicsmarks) < passmarks):
                studentdict[name] = 1            
            if(int(s.chemistrymarks) < passmarks):
                studentdict[name] = 1            
            if(int(s.CSmarks) < passmarks):
                studentdict[name] = 1            
            if(int(s.englishmarks) < passmarks):
                studentdict[name] = 1            

        strReturn = "Students who failed atleast in one subject: \n\n"
        for k in studentdict.keys():
            strReturn += k
            strReturn += "\n"

        return strReturn

    def students_who_passed_in_all_subjects(self):
        self.fetch_student_records()

        passmarks = 35
        
        studentdict = {}

        for s in self.studentlist:

            name = s.FirstName + s.MiddleInitial + s.LastName

            if(int(s.mathmarks) >= passmarks):
                studentdict[name] = 1            
            if(int(s.physicsmarks) >= passmarks):
                studentdict[name] = 1            
            if(int(s.chemistrymarks) >= passmarks):
                studentdict[name] = 1            
            if(int(s.CSmarks) >= passmarks):
                studentdict[name] = 1            
            if(int(s.englishmarks) >= passmarks):
                studentdict[name] = 1            

        strReturn = "Students who passed in all subjects: \n\n"
        for k in studentdict.keys():
            strReturn += k
            strReturn += "\n"

        return strReturn

        
#sl = StudentList()
#s = Student('CS005',"Ranjani","G","J",97,90,91,90,81,'Semester 1')
#sl.createstudent(s)
#sl.deletestudent('CS004')
#s=sl.searchstudent('CS002')
#print(s.USN + ',' + s.FirstName + ',' + s.MiddleInitial + ',' + s.LastName + ',' + \
                        #str(s.mathmarks) + ',' + str(s.physicsmarks) + ',' + str(s.chemistrymarks) + ',' \
                        #+ str(s.CSmarks) + ',' + str(s.englishmarks) + ',' + s.semester + '\n')
    
#sl.average_of_all_students()
