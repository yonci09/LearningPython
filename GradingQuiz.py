# grading scale is as follows:
#student_score of 90 or above is an A
# student_score of 80 or above is a B
# student_score of 70 or above is a C
# student_score of 60 or above is a D
# student_score any lower is an F

student_score = int(input("could you please enter the student_score? "))
 
if student_score >= 90:
    print("your student_score = " + str(student_score) + " = A.")
else:
    if student_score >= 80:
        print("your student_score =  " + str(student_score) + "= B.")
    else:
        if student_score >= 70:
            print("your student_score = " + str(student_score) + " =C.")
        else:
            if student_score >= 60:
                print("your student_score = " + str(student_score) + " = D.")
            else:
                print("your student_score =  " + str(student_score) + "  = F.")