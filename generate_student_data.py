from faker import Faker
from faker_vehicle import VehicleProvider

def generate_data(total_students):

  # Create Faker Object
  fake = Faker()
  fake.add_provider(VehicleProvider)

  # Populate Student Data
  student_data = []
  for x in range(total_students):
    car = fake.vehicle_year_make_model().split()
    temp = {
      "student_id" : "".join(fake.ssn().split('-')),
      "fname" : fake.first_name(),
      "lname" : fake.last_name(),
      "address" : fake.address(),
      "dob" : fake.date_of_birth(),
      "employer" : fake.company(),
      "title" : fake.job(),
      "year" : car[0],
      "make": car[1],
      "model": car[2],
    }
    student_data.append(temp)
  # Return List of Student Dicts
  return student_data