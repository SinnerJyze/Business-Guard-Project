###################
# https://www.youtube.com/watch?v=vusUfPBsggw
###################

import tkinter
import clipboard
import pyperclip
from tkinter import ttk
from tkinter import messagebox


def enter_data():
	pass
	# accepted = accept_var.get()
	# if accepted == "Accepted":

	# 	print("Business Name: ",business_name, "\n"
	# 		"Contact Number: ",contact, "\n"
	# 		"Title: ", title, "\n"
	# 		"Age: ",age, "\n"
	# 		"BD: ",BD, "\n"
	# 		"# Courses: ",numCourses, "\n"
	# 		"# Semesters: ",numSemesters, "\n"
	# 		"Registration Status: ", registrationStatus)

	# else:
	# 	tkinter.messagebox.showwarning(title = "Warning", message = "ToS not yet accepted")

def copy_data():
		business_name = business_name_entry.get()
		contact_name = contact_name_entry.get()
		contact_number = contact_number_entry.get()
		software = software_combobox.get()
		version = version_combobox.get()
		BD = BD_combobox.get()

		registrationStatus = reg_status_var.get()
		numCourses = numcourses_spinbox.get()
		numSemesters = numsemesters_spinbox.get()
		pyperclip.copy(business_name + " " + contact_name + " " + contact_number + " " + software + version + " " + BD)


# Connected via TV, MAIN PC: downloaded latest V3.16 BD18.08.2022 from Dropbox, Compacted and repaired main data file via TV ftp, checked last inv(11393), IS exporting, no custom inv graphics. 2ND PC: Downloaded latest BD from dropbox, upgraded BD, relinked network. Reminded to backup daily and discussed with Pete the 3rd BG appt which is on 16.Dec.2022 @ 12PM - All good

###############################################
window = tkinter.Tk()
window.title("BG data gathering")

frame = tkinter.Frame(window) #window arg is nesting the frame var
frame.pack() 

#pack allows resizing window while being looking the same; Easiest geo or layout mngr for tkinter

		# Tkinter Geometry or Layout managers -
			# .pack
			# .place
			# .grid

##### USER INFORMATION FRAME #######

software_list 		= ["GBPro Plus", "TRUCKBase Pro", "DVSA Safety Inspection Manager Pro", "TRADESBase Pro", "SALONBase", "FIRSTPoint", "Invoice Pro 1", "DIARYBase", "MOTORWeb", "NETMaster"]
truckbasepro_v 		= ["V4.6", "Auto Workshop Manager"]
gbpro_v 			= ["V2.21", "V3"]
gbpro_v3_bd_list 	= ["V3.15 BD15.06.2022", "V3.16 BD18.08.2022"]
gbpro_v2_bd_list 	= ["NO NEW BUILDS"]

def softwareList(e):
	if software_combobox.get() == "GBPro Plus":
		version_combobox.config(value = gbpro_v)

		if version_combobox.get() == "V3":
			BD_combobox.config(value = gbpro_v3_bd_list)

		else:
			BD_combobox.config(value = gbpro_v2_bd_list)

	# elif version_combobox.get() == "V2.21":
	# 		BD_combobox.config(value = gbpro_v2_bd_list)

	elif software_combobox.get() == "TRUCKBase Pro":
		version_combobox.config(value = truckbasepro_v)


cx_info_frame = tkinter.LabelFrame(frame, text = "User Information")
cx_info_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

#Labels
business_name_label = tkinter.Label(cx_info_frame, text = "Business Name")
business_name_entry = tkinter.Entry(cx_info_frame)
business_name_label.grid(row = 0, column = 0)
business_name_entry.grid(row = 1, column = 0)

contact_name_label = tkinter.Label(cx_info_frame, text = "Contact Name")
contact_name_entry = tkinter.Entry(cx_info_frame)
contact_name_label.grid(row = 0, column = 1)
contact_name_entry.grid(row = 1, column = 1)

contact_number_label = tkinter.Label(cx_info_frame, text = "Contact Number")
contact_number_entry = tkinter.Entry(cx_info_frame)
contact_number_label.grid(row = 0, column = 2)
contact_number_entry.grid(row = 1, column = 2)

software_label = tkinter.Label(cx_info_frame, text = "Software")
software_combobox = ttk.Combobox(cx_info_frame, values = software_list)
software_combobox.bind("<<ComboboxSelected>>", softwareList)
software_label.grid(row = 2, column = 0)
software_combobox.grid(row = 3, column = 0)

version_label = tkinter.Label(cx_info_frame, text = "Version")
version_combobox = ttk.Combobox(cx_info_frame, values = [" "])
version_combobox.bind("<<ComboboxSelected>>", softwareList)
version_label.grid(row = 2, column = 1)
version_combobox.grid(row = 3, column = 1)

BD_label = tkinter.Label(cx_info_frame, text = "BD")
BD_combobox = ttk.Combobox(cx_info_frame, values = [" "])
BD_label.grid(row = 2, column = 2)
BD_combobox.grid(row = 3, column = 2)

#This loop allows to resize all widgets that's using .grid() in the cx_info_frame
for widget in cx_info_frame.winfo_children():
	widget.grid_configure(padx = 10, pady = 5)

##### BG INTERACTION DETAILS #######
courses_frame = tkinter.LabelFrame(frame, text = "BG Interaction Details")
courses_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)

#BG Int labels
registered_label = tkinter.Label(courses_frame, text = "Master Setup")
reg_status_var = tkinter.StringVar(value = "PLEASE DEFINE!!!")
registered_check = tkinter.Checkbutton(courses_frame, text = "Exporting?", variable = reg_status_var, onvalue = "Registered", offvalue = "Not Registered")
registered_label.grid(row = 0, column = 0)
registered_check.grid(row = 1, column = 0)

numcourses_label = tkinter.Label(courses_frame, text = "# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to = "infinity")
numcourses_label.grid(row = 0, column = 1)
numcourses_spinbox.grid(row = 1, column = 1)

numsemesters_label = tkinter.Label(courses_frame, text = "# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to = "infinity")
numsemesters_label.grid(row = 0, column = 2)
numsemesters_spinbox.grid(row = 1, column = 2)

#This loop allows to resize all widgets that's using .grid() in the courses_frame
for widget in courses_frame.winfo_children():
	widget.grid_configure(padx = 10, pady = 5)


#Accept TERMS
terms_frame = tkinter.LabelFrame(frame, text = "Terms & Conditions")
terms_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)

accept_var = tkinter.StringVar(value = "Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text = "I accept the terms and conditions.", variable = accept_var, onvalue = "Accepted", offvalue = "Not Accepted")
terms_check.grid(row = 0, column = 0)


#TERMS button
buttons_frame = tkinter.LabelFrame(frame, text = "Buttons")
buttons_frame.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)

button = tkinter.Button(buttons_frame, text = "Print Data as Output", command = enter_data)
button.grid(row = 0, column = 0, padx = 20, pady = 10)

button2 = tkinter.Button(buttons_frame, text = "Copy Data", command = copy_data)
button2.grid(row = 0, column = 1, padx = 20, pady = 10)

window.mainloop()

###########################################






# from tkinter import *


# btn=Button(window, text="This is Button widget", fg='blue')
# btn.place(x=150, y=100)


# my_label = Label(window, 
# 	text = "Business Name:\nContact number:\nLatest Version:\nCloud / HD BackUp:\nCompact & Repair:\nMap Drive:\nOther Notes:\nYour Name:\nLast Inv:\nInv Graphics:\nNext BG:\n", font=("Helvetica", 15), fg='#00008b', justify="right", bd=1, relief="sunken")

# my_label.place(x=10, y=10)

# txtfld1=Entry(window, text="This is Entry Widget", bd=5)
# txtfld2=Entry(window, text="This is Entry Widget", bd=5)
# txtfld1.place(x=50, y=300)
# txtfld2.place(x=50, y=350)


# window.title('BUSINESS GUARD DETAILS')
# window.geometry("500x400+10+10")
# window.mainloop()


# for i in  (11):
# 	lbl.place(x=10, y=5)
# 	lbl.place(x =+ 5)