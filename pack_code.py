################################# Python Imported Libraries ######################################

from faker import Faker
from faker_vehicle import VehicleProvider
import write_student_file
import tkinter as tk
from tkinter import ttk

################################# Python Executible Code ######################################

# Create Faker Object
fake = Faker()
fake.add_provider(VehicleProvider)


# Populate Student Data
student_data = []
for x in range(10):
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


# Invoke File Writer Option
write_student_file.write_student_datafile(student_data)


################################# TKinter Executible Code ######################################

# Create Root Window
root = tk.Tk()

# Create Frame # 1
# Use Pack Layout Manager
# frame_1 = ttk.Frame(root).pack(side='left',fill='x',expand=False)
# Use Grid Layout Manager
id_prompt_frame = ttk.Frame(root,padding=(20,10,20,0))
id_prompt_frame.grid()

# Create ID Input Prompt Label Widget
# Use Pack Layout Manager
# student_id_label = tk.Label(frame_1,text='Enter Student ID #: ',bg='green',fg='white').pack(ipadx=10,ipady=10,side='left',fill='y',expand=False)
# Use Grid Layout Manager
student_id_label = tk.Label(id_prompt_frame,text='Enter Student ID #: ',bg='grey',fg='white').grid(ipadx=10,ipady=10,row=0,column=0,padx=(0,10))

# Create Entry Widget
id_number = tk.StringVar()
# id_entry_obj = ttk.Entry(frame_1,width=15,textvariable=id_number).pack(ipadx=10,ipady=10,side='left',fill='y',expand=False)
id_entry_obj = ttk.Entry(id_prompt_frame,width=15,textvariable=id_number).grid(ipadx=10,ipady=10,row=0,column=1,padx=(0,10))

input_button_frame = ttk.Frame(root,padding=(20,10,20,0))
input_button_frame.grid()

# Create ID Confirm Button Widget
def print_id_number():
  print(f"ID # Entered: {str(id_number.get() or None)}")
# Use Pack Layout Manager
#id_confirm_button = ttk.Button(frame_1,text='Confirm ID Number\nPress Here',command=print_id_number).pack(ipadx=10,ipady=10,side='left',fill='y',expand=False)
# Use Grid Layout Manager
id_confirm_button = ttk.Button(input_button_frame,text='confirm',command=print_id_number).grid(ipadx=10,ipady=10,row=0,column=2,padx=(0,10))

# Start TKinter Event Loop & Pause Python Executible Flow
root.mainloop()

