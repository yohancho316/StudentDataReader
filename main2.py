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
root.geometry('220x100')
root.resizable(False,False)
root.config(bg='grey')

# Create Frame # 1 (Entry Frame)
id_prompt_frame = ttk.Frame(root,padding=(20,10,20,0))
id_prompt_frame.grid()

root.columnconfigure(0,weight=1)
root.rowconfigure(1,weight=0)

# Create ID Input Prompt Label Widget
student_id_label = tk.Label(id_prompt_frame,text='Student ID: ').grid(ipadx=0,padx=(0,5),ipady=0,pady=0,row=0,column=0)

# Create Entry Widget
id_number = tk.StringVar()
id_entry_obj = ttk.Entry(id_prompt_frame,width=15,textvariable=id_number).grid(ipadx=0,padx=0,ipady=0,pady=0,row=0,column=1)

# Create Frame # 2 (Button Frame)
input_button_frame = ttk.Frame(root,padding=(20,10))
input_button_frame.grid(ipadx=0,padx=0,ipady=0,pady=0,row=1,column=0,sticky='EW')

input_button_frame.columnconfigure(0,weight=1)
input_button_frame.columnconfigure(1,weight=1)

# Create ID Confirm Button Widget
def print_id_number():
  print(f"ID # Entered: {str(id_number.get() or None)}")
id_confirm_button = ttk.Button(input_button_frame,text='confirm',command=print_id_number).grid(ipadx=0,padx=0,ipady=0,pady=0,row=0,column=0,sticky='EW')

# Create Quit Button Widget
quit_button = ttk.Button(input_button_frame,text='quit',command=root.destroy).grid(ipadx=0,padx=0,ipady=0,pady=0,row=0,column=1,sticky='EW')

# Start TKinter Event Loop & Pause Python Executible Flow
root.mainloop()

