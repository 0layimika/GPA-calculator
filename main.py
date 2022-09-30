# calculator for gpa
Student_name = input('enter students name:')
Department = input('enter department:')
Level = int(input('Level:'))
Matric_no = input('Matric Number:')
print(f'we will now calculate the GPA for {Student_name}')
Offered_courses = int(input('number of courses offered by student:'))
Total_Unit = int(input('Total units offered:'))

while True:
    Total_Weighted_grade=0
    for i in range (1,Offered_courses+1):
        course_name = input(f'name of course{i}:')
        Score = int(input(f'enter student score for {course_name}:'))
        Unit = int(input('How many units?'))
        if Score >= 70 and Score<=100:
            grade_weight = 5
        elif Score >= 60 and Score<= 69:
            grade_weight = 4
        elif Score >= 50 and Score<= 59:
            grade_weight = 3
        elif Score>= 45 and Score<= 49:
            grade_weight = 2
        elif Score < 45:
            grade_weight = 0
        else:
            print('invalid score.')
        Weighted_grade = Unit * grade_weight
        Total_Weighted_grade = Total_Weighted_grade + Weighted_grade
    GPA = Total_Weighted_grade/Total_Unit
    print(f'Your GPA for this semester is {GPA}')
    Redo = input('Would you like to go again? Yes/ No')
    if Redo.lower() == 'yes':
        continue
    else:
        print('Thanks for using.')
        break









