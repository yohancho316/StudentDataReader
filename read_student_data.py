import csv

def read_student_file():
  with open('/Users/johncho/StudentDataReaderApp/StudentDataReader/write_student_data.csv','r') as file:
    student_data = csv.reader(file)
    student_arr = []
    for student in student_data:
      temp = {
        'student_id': student[1],
        'name': student[3],
        'address' : student[5],
        'dob' : student[7],
        "employer" : student[9],
        "title" : student[11],
        "year" : student[13],
        "make": student[15],
        "model": student[17],
      }
      student_arr.append(temp)
  return student_arr