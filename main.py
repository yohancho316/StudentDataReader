################################# Python Imported Libraries ######################################

import write_student_file
import generate_student_data
import tkinter as tk
from tkinter import ttk
from tkinter.constants import E

################################# Python Executible Code ######################################

################################# TKinter Executible Code ######################################

# Create Root Window
root = tk.Tk()
root.title('Student Data Reader Application')
root.geometry('500x500')
root.resizable(True,True)
# root.columnconfigure(0,weight=1)
# root.rowconfigure(0,weight=1)

# Variables
total_student = tk.StringVar()
id_query = tk.StringVar()
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
def file_clear_action():
  print('File Clear Button Pressed!\n')

def file_confirm_action():
  total_student = int(file_entry.get())
  student_data = generate_student_data.generate_data(total_student)
  print(f'User wants to create {total_student} number of student records!\n')
  for student in student_data:
    print(student)

def file_generate_action():
  write_student_file.write_student_datafile(student_data)
  print('User wants to generate student CSV data file!')

def search_clear_action():
  print('Search Clear Button Pressed!\n')

def search_confirm_action():
  student_id = int(search_entry.get())
  print(f'User wants to search for student id {student_id}.\n')

def search_find_action():
  print('Search Find Button Pressed!\n')

# Frames
file_frame = ttk.Frame(root)
file_frame.grid(row=0,column=0,padx=7,pady=5,sticky='NW')
search_frame = ttk.Frame(root)
search_frame.grid(row=0,column=1,padx=7,pady=5,sticky='NW')
display_frame = ttk.Frame(root)
display_frame.grid(row=0,column=2,padx=7,pady=5,sticky='NW')

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
search_entry = tk.Entry(search_frame,textvariable=id_query)
search_entry.grid(row=0,column=1,padx=15,pady=15)
file_entry.focus()

# Buttons
file_clear_bttn = ttk.Button(file_frame,text='Clear',command=file_clear_action)
file_clear_bttn.grid(row=1,column=0,padx=15,pady=15)
file_confirm_bttn = ttk.Button(file_frame,text='Confirm',command=file_confirm_action)
file_confirm_bttn.grid(row=1,column=1,padx=15,pady=15)
file_generate_bttn = ttk.Button(file_frame,text='Generate File',command=file_generate_action)
file_generate_bttn.grid(row=2,column=0,padx=15,pady=15,columnspan=2,sticky='WE')
search_clear_bttn = ttk.Button(search_frame,text='Clear',command=search_clear_action)
search_clear_bttn.grid(row=1,column=0,padx=15,pady=15)
search_confirm_bttn = ttk.Button(search_frame,text='Confirm',command=search_confirm_action)
search_confirm_bttn.grid(row=1,column=1,padx=15,pady=15)
search_find_bttn = ttk.Button(search_frame,text='Find Student',command=search_find_action)
search_find_bttn.grid(row=2,column=0,padx=15,pady=15,columnspan=2,sticky='WE')

root.mainloop()
