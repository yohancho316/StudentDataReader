################################# Python Imported Libraries ######################################


import write_student_file
import read_student_data
import tkinter as tk
from tkinter import ttk
from tkinter.constants import E
from faker import Faker
from faker_vehicle import VehicleProvider


################################# Python Executible Code ######################################


################################# TKinter Executible Code ######################################


# Create Root Window
root = tk.Tk()
root.title('Student Data Reader Application')
root.geometry('800x700')
root.resizable(True,True)
# root.columnconfigure(0,weight=1)
# root.rowconfigure(0,weight=1)


# Variables
total_student = tk.StringVar()
id_find = tk.StringVar()
student_id = tk.StringVar()
student_name = tk.StringVar()
student_address = tk.StringVar()
student_dob = tk.StringVar()
student_employer = tk.StringVar()
student_job_title = tk.StringVar()
student_car_year = tk.StringVar()
student_car_make = tk.StringVar()
student_car_model = tk.StringVar()
student_data = []


# Methods
def file_confirm_action():
  fake = Faker()
  fake.add_provider(VehicleProvider)
  total_student = int(file_entry.get())
  for x in range(total_student):
    car = fake.vehicle_year_make_model().split()
    address = fake.address()
    address = address.replace(',',' ')
    address = address.replace("\n",' ')
    temp = {
      "student_id" : "".join(fake.ssn().split('-')),
      "name" : ("" + fake.first_name() + ' ' + fake.last_name()),
      "address" : address,
      "dob" : fake.date_of_birth(),
      "employer" : fake.company(),
      "title" : fake.job(),
      "year" : car[0],
      "make": car[1],
      "model": car[2],
    }
    student_data.append(temp)

def file_generate_action():
  write_student_file.write_student_datafile(student_data)

def search_confirm_action():
  student_id = str(id_find.get())
  print(f'The ID you want to search is: {student_id}')

def search_find_action():
  print(f'The ID being searched for is {id_find.get()}\n')
  flag = False
  bucket = []
  student_data = read_student_data.read_student_file()
  for student in student_data:
    if student['student_id'] == str(id_find.get()):
      flag = True
      bucket = student
      break

  student_id.set(bucket['student_id'])
  student_name.set(bucket['name'])
  student_address.set(bucket['address'])
  student_dob.set(bucket['dob'])
  student_employer.set(bucket['employer'])
  student_job_title.set(bucket['title'])
  student_car_year.set(bucket['year'])
  student_car_make.set(bucket['make'])
  student_car_model.set(bucket['model'])
  root.update()

def file_clear():
  file_entry.delete(0,'end')

def search_clear():
  search_entry.delete(0,'end')

# Frames
file_frame = ttk.Frame(root)
file_frame.grid(row=0,column=0,padx=7,pady=5,sticky='NW')
search_frame = ttk.Frame(root)
search_frame.grid(row=0,column=1,padx=7,pady=5,sticky='NW')
display_frame = ttk.Frame(root)
display_frame.grid(row=1,column=0,padx=7,pady=5,sticky='WE')

# Labels
file_label = ttk.Label(file_frame,text='Enter Total Students:')
file_label.grid(row=0,column=0,padx=15,pady=15)
search_label= ttk.Label(search_frame,text='Enter Student ID:')
search_label.grid(row=0,column=0,padx=15,pady=15)
display_frame_id_prompt = ttk.Label(display_frame,text='Student ID:')
display_frame_id_prompt.grid(row=0,column=0,padx=15,pady=15,sticky='W')
display_frame_id_value = ttk.Label(display_frame,textvariable=student_id)
display_frame_id_value.grid(row=0,column=1,padx=15,pady=15,sticky='W')
display_frame_name_prompt = ttk.Label(display_frame,text='Student Name:')
display_frame_name_prompt.grid(row=1,column=0,padx=15,pady=15,sticky='W')
display_frame_name_value = ttk.Label(display_frame,textvariable=student_name)
display_frame_name_value.grid(row=1,column=1,padx=15,pady=15,sticky='W')
display_frame_address_prompt = ttk.Label(display_frame,text='Student Address:')
display_frame_address_prompt.grid(row=2,column=0,padx=15,pady=15,sticky='W')
display_frame_address_value = ttk.Label(display_frame,textvariable=student_address)
display_frame_address_value.grid(row=2,column=1,padx=15,pady=15,sticky='W')
display_frame_dob_prompt = ttk.Label(display_frame,text='Student DOB:')
display_frame_dob_prompt.grid(row=3,column=0,padx=15,pady=15,sticky='W')
display_frame_dob_value = ttk.Label(display_frame,textvariable=student_dob)
display_frame_dob_value.grid(row=3,column=1,padx=15,pady=15,sticky='W')
display_frame_employer_prompt = ttk.Label(display_frame,text='Student Employer:')
display_frame_employer_prompt.grid(row=4,column=0,padx=15,pady=15,sticky='W')
display_frame_employer_value = ttk.Label(display_frame,textvariable=student_employer)
display_frame_employer_value.grid(row=4,column=1,padx=15,pady=15,sticky='W')
display_frame_job_title_prompt = ttk.Label(display_frame,text='Student Job Title:')
display_frame_job_title_prompt.grid(row=5,column=0,padx=15,pady=15,sticky='W')
display_frame_job_title_value = ttk.Label(display_frame,textvariable=student_job_title)
display_frame_job_title_value.grid(row=5,column=1,padx=15,pady=15,sticky='W')
display_frame_car_year_prompt = ttk.Label(display_frame,text='Student Car Year:')
display_frame_car_year_prompt.grid(row=6,column=0,padx=15,pady=15,sticky='W')
display_frame_car_year_value = ttk.Label(display_frame,textvariable=student_car_year)
display_frame_car_year_value.grid(row=6,column=1,padx=15,pady=15,sticky='W')
display_frame_car_model_prompt = ttk.Label(display_frame,text='Student Car Model:')
display_frame_car_model_prompt.grid(row=7,column=0,padx=15,pady=15,sticky='W')
display_frame_car_model_value = ttk.Label(display_frame,textvariable=student_car_model)
display_frame_car_model_value.grid(row=7,column=1,padx=15,pady=15,sticky='W')
display_frame_car_make_prompt = ttk.Label(display_frame,text='Student Card Make:')
display_frame_car_make_prompt.grid(row=8,column=0,padx=15,pady=15,sticky='W')
display_frame_car_make_value = ttk.Label(display_frame,textvariable=student_car_make)
display_frame_car_make_value.grid(row=8,column=1,padx=15,pady=15,sticky='W')

# Entry
file_entry = tk.Entry(file_frame,textvariable=total_student)
file_entry.grid(row=0,column=1,padx=15,pady=15)
search_entry = tk.Entry(search_frame,textvariable=id_find)
search_entry.grid(row=0,column=1,padx=15,pady=15)
file_entry.focus()

# Buttons
file_clear_bttn = ttk.Button(file_frame,text='Clear',command=file_clear)
file_clear_bttn.grid(row=1,column=0,padx=15,pady=15)
file_confirm_bttn = ttk.Button(file_frame,text='Confirm',command=file_confirm_action)
file_confirm_bttn.grid(row=1,column=1,padx=15,pady=15)
file_generate_bttn = ttk.Button(file_frame,text='Generate File',command=file_generate_action)
file_generate_bttn.grid(row=2,column=0,padx=15,pady=15,columnspan=2,sticky='WE')
search_clear_bttn = ttk.Button(search_frame,text='Clear',command=search_clear)
search_clear_bttn.grid(row=1,column=0,padx=15,pady=15)
search_confirm_bttn = ttk.Button(search_frame,text='Confirm',command=search_confirm_action)
search_confirm_bttn.grid(row=1,column=1,padx=15,pady=15)
search_find_bttn = ttk.Button(search_frame,text='Find Student',command=search_find_action)
search_find_bttn.grid(row=2,column=0,padx=15,pady=15,columnspan=2,sticky='WE')

root.mainloop()