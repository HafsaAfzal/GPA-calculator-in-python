# ***  GPA CALCULATOR  ****

# INPUT OF SCORES
n=int(input("enter number of courses :"))
print("____________________________________________________________________")
marks=[]
for i in range (n):
    h=float(input("enter marks of course  " +str(i+1)+" :"))
    marks.append(h)
print("____________________________________________________________________")
# CALCULATING GRADE POINT EQUIVALENT TO SCORES
l=len(marks)
#print(l)
GradePoint=[]
for m in range(l):
    if marks[m] >= 90 :
       GradePoint.append(4.0) 
    if marks[m] >= 85  and  marks[m] <= 89 :
       GradePoint.append(4.0) 
    if marks[m] >= 80  and  marks[m] <= 84 :
        GradePoint.append(3.8)
    if marks[m] >= 75  and  marks[m] <= 79 :
        GradePoint.append(3.4)    
    if marks[m] >= 71  and  marks[m] <= 74 :
       GradePoint.append( 3.0)
    if marks[m] >= 68  and  marks[m] <= 70 :    
        GradePoint.append(2.8)
    if marks[m] >= 64  and  marks[m] <= 67 :
        GradePoint.append(2.4)
    if marks[m] >= 61  and  marks[m] <= 63 :
        GradePoint.append(2.0)
    if marks[m] >= 57  and  marks[m] <= 60 :
        GradePoint.append(1.8)
    if marks[m] >= 53  and  marks[m] <= 56 :
        GradePoint.append(1.4)
    if marks[m] >= 50  and  marks[m] <= 52 :
        GradePoint.append(1.0)
    if marks[m] >=50 :
        GradePoint.append(0.0)
    #print("marks[m]=",marks[m])
   # GradePoint.append(s)   
#print(GradePoint)    

# MULTIPLYING EACH GRADE POINT TO CREDIT HOURS
list=[]
for i in range(len(GradePoint)):
    s=GradePoint[i]*3
    list.append(s)
#print(list)

#ADDING THE ELEMENTS OF LIST AND DIVIDING BY TOTAL NUMBER OF CREDIT HOURS
sum=0
for j in range (len(list)):
    sum+=list[j]
#print (sum)    

#CALCULATING GPA
gpa=sum/(n*3)
print("your GPA is ","%1.2f"%gpa)
print()
if gpa >=2.8 or gpa >=4.0 :
    print("keep it up")
else:
    print("you need some hardwork")    