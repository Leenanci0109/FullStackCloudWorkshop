class student:
    def __init__(self,sid,sname,sgrade):
        self.sid=sid
        self.sname=sname
        self.sgrade=sgrade
    def getsid(self):
        return self.sid
    def getsname(self):
        return self.sname
    def getsgrade(self):
        return self.sgrade
    def setsname(self,sname):
        self.sname=sname
    def setsgrade(self,sgrade):
        self.sgrade=sgrade
grades=[] # type:student
def viewGrades(sid): #use student id
    global grades
    for i in grades:
        if(i.sid==sid):
            print("name: ",i.sname)
            print("grades: ",i.sgrade)
def deleteGrades(sid):
    global grades
    for i in grades:
        if(i.sid==sid):
            grades.remove(i)
def updateGrades(sid,usname,usgrade): # updated student name and grade
    global grades
    for i in grades:
        if(i.sid==sid):
            i.setsname(usname)
            i.setsgrade(usgrade)
def addGrades(sid, sname, sgrade):
    global grades
    sg=student(sid,sname,sgrade)
    grades.append(sg)

##    
addGrades(1,"Leenancy",90)
addGrades(2,"Mili",90)
print(grades)
updateGrades(1,"Leenanci",97)
print(grades)
deleteGrades(1)
print(grades)
addGrades(1,"Leenancy",90)
viewGrades(1)
print(grades)