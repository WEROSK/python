#creates text file to store all student inputs
#student function to take inputs for name, surname and grade (score)
def student():
    f=open("Student_Score_DB.txt","a")
    name=input("Name: ")
    surname=input("Surname: ")
#if input is not integer or more than 100 error message will occur
    while True:
        try:
            score=int(input("Score: "))
            if score >100:
                print("Test score out of 100!")
            else:
                break
        except ValueError:
            print("Only numbers are accepted!")
#saves inputs of variable name, surname and score as a string in text file
    f.write("Name: "+str(name))
    f.write("\nSurname: "+str(surname))
    f.write("\nScore: "+str(score)+"\n")
    f.close()

#main function to add minimum of 6 students to data base
def main():
    studentADD_count=0
    while True:
#shows the number of student which is being added
        print("Student: "+str(studentADD_count+1))
        student()
        studentADD_count=studentADD_count+1
        if studentADD_count==6:
            print("Student limit add reached!")
            break

#main function is executed
main()
