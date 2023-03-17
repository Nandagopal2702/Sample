""" Take the input marks from user using input() function and find out the grade of the students. 
    Note the grading will be in this manner - (100 - 91) - A1,(90-81) - A2, (80-71) - B1, (70-61) - B2, 
    (60-51) - C1 (50-40) - C2 and less than 40 students will 'Fail'. 
    Also make sure user should input the marks in the range 0<=marks<=100, 
    if user will input some other marks in should print invalid marks. """

marks = int(input())

if marks < 0 or marks > 100:
    print("Invalid Marks:Enter the correct marks")
elif marks >= 91 and marks <= 100:
    print('A1')
elif marks >= 81 and marks <= 90:
    print('A2')
elif marks >= 71 and marks <= 80:
    print('B1')
elif marks >= 61 and marks <= 70:
    print('B2')
elif marks >= 51 and marks <= 60:
    print('C1')
elif marks >= 40 and marks <= 50:
    print('C2')
elif marks < 40:
    print("Fail")