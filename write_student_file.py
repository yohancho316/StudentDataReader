import csv

def write_student_datafile(student_data):
  with open('/Users/johncho/StudentDataReaderApp/StudentDataReader/write_student_data.csv', 'w') as file:
    writer_obj = csv.writer(file)
    user_data = []
    for student in student_data:
      key_arr = student.keys()
      for key in key_arr:
        user_data.append(key)
        user_data.append(student[key])
      writer_obj.writerow(user_data)
      user_data.clear()
















