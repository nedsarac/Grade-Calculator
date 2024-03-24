# File: GradeCalculator.py
# Name: Nedim Sarac
# Date: 03/01/2024
# Description of Program: This program calculates and displays the grade report for a student based on their homework, project, and exam grades.

HW_ERROR_MESSAGE    = "    Grade must be in range [0..10]. Try again."
PR_EX_ERROR_MESSAGE = "    Grade must be in range [0..100]. Try again."

def HomeWorks():
    hwSum = 0
    for i in range(1,4):
        HW = int(input(" " * 4 + "Enter HW" + str(i) + " grade: "))
        while HW > 10 or HW < 0:
            print(HW_ERROR_MESSAGE)
            HW = int(input(" " * 4 + "Enter HW" + str(i) + " grade: "))
        hwSum += HW
    hwAvg = (hwSum / 3) * 10
    hwAvg = format(hwAvg, "0.2f")
    return float(hwAvg)

def Projects():
    prSum = 0
    for i in range(1,3):
        pr = int(input(" " * 4 + "Enter Pr" + str(i) + " grade: "))
        while pr > 100 or pr < 0:
            print(PR_EX_ERROR_MESSAGE)
            pr = int(input(" " * 4 + "Enter pr" + str(i) + " grade: "))
        prSum += pr
    prAvg = (prSum / 2)
    prAvg = format(prAvg, "0.2f")
    return float(prAvg)

def Exams():
    exSum = 0
    for i in range (1,3):
        ex = int(input(" " * 4 + "Enter Ex" + str(i) + " grade: "))
        while ex > 100 or ex < 0:
            print(PR_EX_ERROR_MESSAGE)
            ex = int(input(" " * 4 + "Enter Ex" + str(i) + " grade: "))
        exSum += ex
    exAvg = exSum / 2
    exAvg = format(exAvg, "0.2f")
    return float(exAvg)

def GradeReport(hwAvg, prAvg, exAvg):
    studAvg = (hwAvg * .3 + prAvg * .3 + exAvg * .4)
    hwAvg_str = format(hwAvg, "0.2f")
    prAvg_str = format(prAvg, "0.2f")
    exAvg_str = format(exAvg, "0.2f")
    studAvg_str = format(studAvg, "0.2f")
    crsGrd = ""
    if studAvg >= 90:
        crsGrd = "A"
    elif studAvg < 90 and studAvg >= 80:
        crsGrd = "B"
    elif studAvg < 80 and studAvg >= 70:
        crsGrd = "C"
    elif studAvg < 70 and studAvg >= 60:
        crsGrd = "D"
    elif studAvg < 60:
        crsGrd = "F"
    print(" " * 4 + "Homework average (30% of grade):", hwAvg_str)
    print(" " * 4 + "Project average (30% of grade):", prAvg_str)
    print(" " * 4 + "Exam average (40% of grade):", exAvg_str)
    print(" " * 4 + "Student course average:", studAvg_str)
    print(" " * 4 + "Course grade (CS303E: Spring, 2024):", crsGrd)

def main():
    studentName = input("Enter the student's name (or 'stop'): ")
    while studentName != "stop":
        print()
        print("HOMEWORKS:")
        hwAvg = HomeWorks()
        print()
        print("PROJECTS:")
        prAvg = Projects()
        print()
        print("EXAMS:")
        exAvg = Exams()
        print()
        print("Grade report for:", studentName)
        GradeReport(hwAvg, prAvg, exAvg)
        print()
        studentName = input("Enter the student's name (or 'stop'): ")
    print("Thanks for using the grade calculator! Goodbye.")
    print()

main()
















        

        
