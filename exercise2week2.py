def grade(grades, ch):
    if(ch==0):
        key1=input("enter student name:")
        for i in grades:
            if(i[0]==key1):
                print("grades: ",i[1])         
    elif(ch==1):
        key1=str(input("enter student name to add:"))
        value1=int(input("enter grades to add:"))
        grades.append([key1,value1])
    elif(ch==2):
         key1=str(input("enter student name to delete:"))
         for i in grades:
            if(i[0]==key1):
                grades.remove(i)
    elif(ch==3):
        key1=str(input("enter student name to change data:"))
        for i in grades:
            if(i[0]==key1):
                s=str(input("enter n to change name"))
                if (s=="n"):
                    name=str(input("enter new name:"))
                    ind=grades.index(i)
                    grades[ind][0]=name
                s=str(input("enter g to change grade"))
                if(s=="g"):
                    gr=int(input("enter changed grade:"))
                    ind=grades.index(i)
                    grades[ind][1]=gr
    return grades
    
    
grades=[]
print("enter 0-search grades. 1-add names and grade, 2-delete ,3- update data , 4 - quit")
s=int(input())

while(s!=4):
    grades=grade(grades,s)
    print(grades)
    s=int(input("Choice>>"))
