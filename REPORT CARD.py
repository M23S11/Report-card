#Defining grades
def grade(g):
  if g>=90:
    return "A"
  elif g>=80 and g<90:
   return "B"
  elif g>=70 and g<80:
    return "C"
  elif g>=60 and g<70:
    return "D"
  elif g<60:
   return "F"
    
#Defining average marks

def average(m,p,c):
  avg=(p+c+m)/3
  return avg
#Defining if passes or failed

def pf(x):
  if x>=50:
    print("You have passed your exams.Congrats! ")
  else:
    print("Your have failed your exams.Try again :) ")


name=input("What is your name? ")
print("Hi",name)
m=int(input("What is your math grade? "))
print(m)
p=int(input("What is your physics grade? "))
print(p)
c=int(input("What is your chemistry grade? "))
print(c)

#Grades of individual subjects

print("Your Grade in maths is ",grade(m))
print("Your Grade in physics is ",grade(p))
print("Your Grade in chemistry is ",grade(c))

#Checking average marks

print("Average marks is ",average(m,p,c))


#Checking if passed or failed

pf(average(m,p,c))



  

