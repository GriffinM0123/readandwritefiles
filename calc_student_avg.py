import csv

students = open("Student_Scores.csv", "r")

outfile = open("student_avg.csv", "w")

student_file = csv.reader(students, delimiter=",")

for record in student_file:
    
    outfile.write('Name: ' + record[0] + "\n")
    stu_avg = (float(record[1]) + float(record[2]) + float(record[3]))/(3)
    outfile.write('Average Score: ')
    outfile.write("{:.2f}". format(stu_avg) + "\n")

outfile.close()