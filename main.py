# Import Python Libraries
from faker import Faker
from faker_vehicle import VehicleProvider
import write_student_file

# Create Faker Object
fake = Faker()
fake.add_provider(VehicleProvider)

# Populate Student Data
student_data = []
for x in range(10):
  car = fake.vehicle_year_make_model().split()
  temp = {
    "ID" : "".join(fake.ssn().split('-')),
    "fname" : fake.first_name(),
    "lname" : fake.last_name(),
    "address" : fake.address(),
    "DOB" : fake.date_of_birth(),
    "Employer" : fake.company(),
    "title" : fake.job(),
    "year" : car[0],
    "make": car[1],
    "model": car[2],
  }
  student_data.append(temp)

# Invoke File Writer Option
write_student_file.write_student_datafile(student_data)
