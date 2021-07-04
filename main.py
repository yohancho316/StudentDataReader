################################# Python Imported Libraries ######################################

from tkinter.constants import E
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
root.title('Student Data Reader Application')
root.geometry('450x100')
root.resizable(False,False)
# root.config(bg='grey')


# Create Input Frame
input_frame =ttk.Frame(root)
input_frame.grid(ipadx=0,ipady=0,padx=0,pady=0,row=0,column=0,sticky='w')


# ID & DOB Label Widgets
l1 = ttk.Label(input_frame,text="Student ID: ")
l2 = ttk.Label(input_frame,text="DOB: ")

l1.grid(ipadx=0,ipady=0,padx=0,pady=0,row=0,column=0,sticky='we')
l2.grid(ipadx=0,ipady=0,padx=0,row=1,column=0,sticky='we')


#  Student ID & DOB Entry Widgets
student_id = tk.StringVar()
student_dob = tk.StringVar()
e1 = ttk.Entry(input_frame,width=15,textvariable=student_id)
e2 = ttk.Entry(input_frame,width=15,textvariable=student_dob)

e1.grid(ipadx=0,ipady=0,padx=0,row=0,column=1,sticky='e')
e2.grid(ipadx=0,ipady=0,padx=0,row=1,column=1,sticky='e')

e1.focus()
e2.focus()


# Create Frame # 2 (Button Frame)
input_button_frame = ttk.Frame(root)
input_button_frame.grid(ipadx=0,padx=0,ipady=0,pady=0,row=1,column=0,sticky='EW')

input_button_frame.columnconfigure(0,weight=1)
input_button_frame.columnconfigure(1,weight=1)


# Print to Terminal Student ID & DOB Whenever Button is Activated
def confirm_button_click():
  print(f"Student ID Number: {student_id.get() or None}\nStudent DOB: {student_dob.get() or None}")


# Confirm & Quit Button Widgets
confirm_button = ttk.Button(input_frame,text='Confirm',command=confirm_button_click)
confirm_button.grid(ipadx=0,ipady=0,padx=0,row=2,column=0,columnspan=2,sticky='we')

quit_button = ttk.Button(input_frame,text='Quit',command=root.destroy)
quit_button.grid(ipadx=0,ipady=0,padx=0,row=3,columnspan=2,sticky='we')


# Create Info Frame
info_frame = ttk.Frame(root)
info_frame.grid(ipadx=0,ipady=0,padx=0,pady=0,row=0,column=1,sticky='e')

info_label = ttk.Label(info_frame,text='Student Information Goes Here Later')
info_label.grid(ipadx=0,ipady=0,padx=0,pady=0,row=0,column=0,sticky='ew')


# Start TKinter Event Loop & Pause Python Executible Flow
root.mainloop()