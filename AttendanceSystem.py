import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pandas as pd
from datetime import datetime
import sys
from tkcalendar import DateEntry
from datetime import datetime
import time
import openpyxl as xl
from Module import *

def showloadingscreen():
    loading_screen = tk.Toplevel()
    loading_screen.title("Loading")
    loading_screen.geometry("300x100")
    loading_screen.resizable(False, False)
    loading_screen.configure(bg="black")
    loading_screen.overrideredirect(True)
    screen_width = loading_screen.winfo_screenwidth() # Get the screen width and height
    screen_height = loading_screen.winfo_screenheight()
    x = int(screen_width/2 - 150)     # Calculate the x and y coordinates to center the loading screen on the screen
    y = int(screen_height/2 - 50)
    loading_screen.geometry("+{}+{}".format(x, y)) # Set the position of the loading screen
    name_label = tk.Label(loading_screen, text="CYBERX \nATTENDANCE", font=("AkiraExpanded-SuperBold", 20), fg="white", bg="black")
    name_label.pack(pady=1, anchor="center")
    label = tk.Label(loading_screen, text="Loading...", font=("8514oem", 12), fg="white", bg="black")
    label.pack(pady=1, anchor="center")
    loading_screen.update()
    time.sleep(3) # Simulate loading process
    loading_screen.destroy()
    time.sleep(0.5) #Delay after loading

class App:
	def __init__(self, master):
		self.master = master
		self.frames()
		
	def frames(self):
#mainframe
		self.main=tk.Frame(self.master)
		self.main.config(bg="#2b2a2a")
		self.title = tk.Label(self.main, text="CYBERX \nATTENDANCE", font=("Footlight MT Light", 45, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify="center")
		self.title.pack(pady=10)
		self.student = tk.Button(self.main, text="LOG IN AS STUDENT", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.show_camera_frame1)
		self.student.pack(pady=25, padx=25, anchor='center', expand=True)
		self.faculty = tk.Button(self.main, text="LOG IN AS FACULTY", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.show_camera_frame2)
		self.faculty.pack(pady=25, padx=25, anchor='center', expand=True)
		self.exit_button = tk.Button(self.main, text="EXIT", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.exit)
		self.exit_button.pack(pady=25, padx=25, anchor='center', expand=True)
		self.main.pack()
#cameraframe1forstudents
		self.camera_frame1 = tk.Frame(self.master)
		self.camera_frame1.config(bg="#2b2a2a")
		self.title = tk.Label(self.camera_frame1, text="SHOW YOUR IDENTITY CARD", font=("Footlight MT Light", 45, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify="center")
		self.title.pack(pady=10)
		self.cam=tk.Button(self.camera_frame1, text="OPEN CAMERA", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.studentlogin)
		self.cam.pack(pady=25, padx=25, anchor='center', expand=True)
		self.goback=tk.Button(self.camera_frame1, text="BACK", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.show_main)
		self.goback.pack(side=tk.LEFT, pady=25, padx=25, anchor='center', expand=True)
		self.exit_button = tk.Button(self.camera_frame1, text="EXIT", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.exit)
		self.exit_button.pack(side=tk.RIGHT, pady=25, padx=25, anchor='center', expand=True)
		self.camera_frame1.pack_forget()
#cameraframe2forfaculties
		self.camera_frame2 = tk.Frame(self.master)
		self.camera_frame2.config(bg="#2b2a2a")
		self.title = tk.Label(self.camera_frame2, text="SHOW YOUR IDENTITY CARD", font=("Footlight MT Light", 45, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify="center")
		self.title.pack(pady=10)
		self.cam=tk.Button(self.camera_frame2, text="OPEN CAMERA", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.facultylogin)
		self.cam.pack(pady=25, padx=25, anchor='center', expand=True)
		self.goback=tk.Button(self.camera_frame2, text="BACK", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.show_main)
		self.goback.pack(side=tk.LEFT, pady=25, padx=25, anchor='center', expand=True)
		self.exit_button = tk.Button(self.camera_frame2, text="EXIT", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.exit)
		self.exit_button.pack(side=tk.RIGHT, pady=25, padx=25, anchor='center', expand=True)
		self.camera_frame2.pack_forget()
#mainframeforstudents
		self.stdmain=tk.Frame(self.master)
		self.stdmain.config(bg="#2b2a2a")
		self.title1 = tk.Label(self.stdmain, text="CYBERX \nATTENDANCE", font=("Footlight MT Light", 45, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify="center")
		self.title1.pack(pady=10)
		self.addattendance = tk.Button(self.stdmain, text="ADD ATTENDANCE", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.show_frame_details)
		self.addattendance.pack(pady=10, padx=10, anchor='center', expand=True)
		self.modifyattendance = tk.Button(self.stdmain, text="VIEW AND MODIFY ATTENDANCE", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.show_frame_modifyauth)
		self.modifyattendance.pack(pady=10, padx=10, anchor='center', expand=True)
		self.percattendance = tk.Button(self.stdmain, text="VIEW ATTENDANCE RECORDS", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.show_frame_sub)
		self.percattendance.pack(pady=10, padx=10, anchor='center', expand=True)
		self.timetable = tk.Button(self.stdmain, text="VIEW TIMETABLE", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.show_frame_tt)
		self.timetable.pack(pady=10, padx=10, anchor='center', expand=True)
		self.logout_button = tk.Button(self.stdmain, text="LOG OUT", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.show_main)
		self.logout_button.pack(side=tk.LEFT, pady=10, padx=10, anchor='center', expand=True)
		self.exit_button = tk.Button(self.stdmain, text="EXIT", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.exit)
		self.exit_button.pack(side=tk.RIGHT, pady=10, padx=10, anchor='center', expand=True)
		self.stdmain.pack_forget()
#mainframeforfaculty
		self.facmain=tk.Frame(self.master)
		self.facmain.config(bg="#2b2a2a")
		self.title = tk.Label(self.facmain, text="CYBERX \nATTENDANCE", font=("Footlight MT Light", 45, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify="center")
		self.title.pack(pady=10)
		self.percattendance = tk.Button(self.facmain, text="ADD & VIEW ATTENDANCE RECORDS", font=("Garamond",15), width=40, height=1, bg="#786969", fg="#000000", command=self.show_facattrec_frame)
		self.percattendance.pack(pady=10, padx=10, anchor='center', expand=True)
		self.timetable = tk.Button(self.facmain, text="VIEW TIMETABLE", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command = self.show_framett)
		self.timetable.pack(pady=10, padx=10, anchor='center', expand=True)
		self.student = tk.Button(self.facmain, text="VIEW STUDENT RECORDS", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.viewstudent)
		self.student.pack(pady=10, padx=10, anchor='center', expand=True)
		self.logout_button = tk.Button(self.facmain, text="LOG OUT", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.show_main)
		self.logout_button.pack(side=tk.LEFT, pady=10, padx=10, anchor='center', expand=True)
		self.exit_button = tk.Button(self.facmain, text="EXIT", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.exit)
		self.exit_button.pack(side=tk.RIGHT, pady=10, padx=10, anchor='center', expand=True)
		self.facmain.pack_forget()
#frameforfac-view&add&modifyattendancerecords
		self.facattrec=tk.Frame(self.master)
		self.facattrec.config(bg="#2b2a2a")
		self.title1 = tk.Label(self.facattrec, text="CHOOSE A DATE", font=("Footlight MT Light", 30, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=LEFT)
		self.title1.pack(padx=30, pady=30, anchor="center")
		style=tk.ttk.Style()
		style.configure("my.DateEntry", arrowcolor="white", bordercolor="white",darkcolor="white", lightcolor="white", selectbackground="black", selectforeground="white", foreground="black")
		self.cale = DateEntry(self.facattrec, width=15, height=9, background="#000000", borderwidth=9, style="my.DateEntry", date_pattern="dd/MM/yyyy")
		self.cale.pack(padx=20, pady=20, anchor="center")
		self.title2 = tk.Label(self.facattrec, text="ENTER LAST TWO DIGITS OF \nREGISTRATION NOS OF THE STUDENTS \n(Separated with Commas)", font=("Footlight MT Light", 30, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify="center")
		self.title2.pack(padx=30, pady=30, anchor="center")
		self.numbers_entry = tk.Entry(self.facattrec, font=("Arial", 15), fg="black", width=30)
		self.numbers_entry.pack(padx=20, pady=20)
		self.goback=tk.Button(self.facattrec, text="BACK", font=("Garamond",15), width=15, height=1, bg="#FFFDD0", fg="#000000", command=self.show_facmain_frame)
		self.goback.pack(side = tk.LEFT, pady=20, padx=20, anchor='center')
		self.markp = tk.Button(self.facattrec, text="MARK PRESENT", font=("Garamond",15), width=15, height=1, bg="#FFFDD0", fg="#000000", command=self.markpresent)
		self.markp.pack(side = tk.LEFT, pady=20, padx=20, anchor='center')
		self.marka = tk.Button(self.facattrec, text="MARK ABSENT", font=("Garamond",15), width=15, height=1, bg="#FFFDD0", fg="#000000", command=self.markabsent)
		self.marka.pack(side = tk.LEFT, pady=20, padx=20, anchor='center')
		self.viewrec = tk.Button(self.facattrec, text="VIEW RECORDS", font=("Garamond",15), width=15, height=1, bg="#FFFDD0", fg="#000000", command=self.viewfacsub)
		self.viewrec.pack(side = tk.LEFT, pady=20, padx=20, anchor='center')
		self.facattrec.pack_forget()
#frameforaddattendance-details-date,session,subject
		self.frame_details=tk.Frame(self.master)
		self.frame_details.config(bg="#2b2a2a")
		self.title1 = tk.Label(self.frame_details, text="CHOOSE A DATE", font=("Footlight MT Light", 25, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=LEFT)
		self.title1.pack(padx=15, pady=15)
		style=tk.ttk.Style()
		style.configure("my.DateEntry", arrowcolor="white", bordercolor="white",darkcolor="white", lightcolor="white", selectbackground="black", selectforeground="white", foreground="black")
		self.cal = DateEntry(self.frame_details, width=15, height=9, background="#000000", borderwidth=9, style="my.DateEntry", date_pattern="dd/MM/yyyy")
		self.cal.pack(padx=5, pady=5)
		self.title2 = tk.Label(self.frame_details, text="CHOOSE A SESSION", font=("Footlight MT Light", 25, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=LEFT)
		self.title2.pack(padx=15, pady=15)
		self.var1=tk.StringVar()
		self.session = ttk.Combobox(self.frame_details, state="readonly", values=["SESSION ONE : 08:10 AM TO 09:00 AM", "SESSION TWO : 09:00 AM TO 09:50 AM", "SESSION THREE : 10:10 AM TO 11:00 AM", "SESSION FOUR : 11:00 AM TO 11:50 AM", "SESSION FIVE : 12:50 PM TO 01:40 PM", "SESSION SIX : 01:40 PM TO 02:30 PM", "SESSION SEVEN : 02:40 PM TO 03:30 PM"], width=35, textvariable=self.var1)
		self.session.pack(padx=5, pady=5)
		self.title = tk.Label(self.frame_details, text="CHOOSE A COURSE", font=("Footlight MT Light", 25, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=LEFT)
		self.title.pack(padx=15, pady=15)
		self.var2=tk.StringVar()
		self.subject=ttk.Combobox(self.frame_details, state="readonly", values=["EN1002 : ENGLISH FOR ENGINEERS", "MA1002 : PROBABILITY & STATISTICS", "CS1002 : PROGRAMMING IN PYTHON", "CS1006T : DATA STRUCTURES", "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE", "CS1008 : CLASSICAL CRYPTOGRAPHY"], width=50, textvariable=self.var2)
		self.subject.pack(padx=5, pady=5)
		self.title3 = tk.Label(self.frame_details, text="YOU NEED A BARCODE TO MARK ATTENDANCE", font=("Footlight MT Light", 25, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=LEFT)
		self.title3.pack(padx=15, pady=15)
		self.goback=tk.Button(self.frame_details, text="BACK", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.show_stdmain_frame)
		self.goback.pack(side = tk.LEFT, pady=15, padx=15, anchor='center', expand=True)
		self.add=tk.Button(self.frame_details, text="OPEN CAMERA & ADD", font=("Garamond",15), width=25, height=1, bg="#FFFDD0", fg="#000000", command=self.checkdateandtime)
		self.add.pack(side=tk.RIGHT, pady=15, padx=15, anchor='center', expand=True)
		self.frame_details.pack_forget()
#frameforttforstudents
		self.frame_tt=tk.Frame(self.master)
		self.frame_tt.config(bg="#2b2a2a")
		self.title = tk.Label(self.frame_tt, text="EVEN SEMESTER", font=("Footlight MT Light", 45, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify="center")
		self.title.pack(pady=10)
		self.s1tt=tk.Button(self.frame_tt, text="VIEW TIMETABLE", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.opensecsem)
		self.s1tt.pack(pady=10, padx=10, anchor='center', expand=True)
		self.course = tk.Button(self.frame_tt, text="VIEW COURSES AND FACULTY", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.opentwocoursesandfac)
		self.course.pack(pady=10, padx=10, anchor='center', expand=True)		
		self.goback=tk.Button(self.frame_tt, text="BACK", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.show_stdmain_frame)
		self.goback.pack(pady=10, padx=10, anchor='center', expand=True)
		self.frame_tt.pack_forget()
#frameforttforfaculty
		self.framett=tk.Frame(self.master)
		self.framett.config(bg="#2b2a2a")
		self.title = tk.Label(self.framett, text="EVEN SEMESTER", font=("Footlight MT Light", 45, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify="center")
		self.title.pack(pady=10)
		self.s1tt=tk.Button(self.framett, text="VIEW TIMETABLE", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.opensecsem)
		self.s1tt.pack(pady=10, padx=10, anchor='center', expand=True)
		self.course = tk.Button(self.framett, text="VIEW COURSES AND FACULTY", font=("Garamond",15), width=30, height=1, bg="#786969", fg="#000000", command=self.opentwocoursesandfac)
		self.course.pack(pady=10, padx=10, anchor='center', expand=True)		
		self.goback=tk.Button(self.framett, text="BACK", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.show_facmain_frame)
		self.goback.pack(pady=10, padx=10, anchor='center', expand=True)
		self.framett.pack_forget()
#frameformodifyauth
		self.frame_modifyauth=tk.Frame(self.master)
		self.frame_modifyauth.config(bg="#2b2a2a")
		self.title = tk.Label(self.frame_modifyauth, text="ENTER THE APPROPRIATE DETAILS", font=("Footlight MT Light", 40, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=CENTER)
		self.title.pack(padx=10, pady=10)
		self.title1 = tk.Label(self.frame_modifyauth, text="CHOOSE A COURSE", font=("Footlight MT Light", 25, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=CENTER)
		self.title1.pack(padx=20, pady=20)
		self.var = tk.StringVar()
		self.subject=ttk.Combobox(self.frame_modifyauth, state="readonly", values=["EN1002 : ENGLISH FOR ENGINEERS", "MA1002 : PROBABILITY & STATISTICS", "CS1002 : PROGRAMMING IN PYTHON", "CS1006T : DATA STRUCTURES", "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE", "CS1008 : CLASSICAL CRYPTOGRAPHY"], width=50, textvariable=self.var)
		self.subject.pack(padx=5, pady=5)
		self.title2 = tk.Label(self.frame_modifyauth, text="CHOOSE A DATE", font=("Footlight MT Light", 25, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=CENTER)
		self.title2.pack(padx=20, pady=20)
		style=tk.ttk.Style()
		style.configure("my.DateEntry", arrowcolor="white", bordercolor="white",darkcolor="white", lightcolor="white", selectbackground="black", selectforeground="white", foreground="black")
		self.cal2 = DateEntry(self.frame_modifyauth, width=30, height=9, background="#000000", borderwidth=9, style="my.DateEntry", date_pattern="dd/MM/yyyy")
		self.cal2.pack(padx=5, pady=5)
		self.goback=tk.Button(self.frame_modifyauth, text="BACK", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.show_stdmain_frame)
		self.goback.pack(side=tk.LEFT, pady=10, padx=10, anchor='center', expand=True)
		self.view=tk.Button(self.frame_modifyauth, text="VIEW", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.modify_auth)
		self.view.pack(side = tk.RIGHT, pady=20, padx=20, anchor='center', expand=True)
		self.frame_modifyauth.pack_forget()
#frameforsubforviewrecord
		self.frame_sub=tk.Frame(self.master)
		self.frame_sub.config(bg="#2b2a2a")
		self.title = tk.Label(self.frame_sub, text="CHOOSE A COURSE", font=("Footlight MT Light", 25, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=LEFT)
		self.title.pack(padx=30, pady=30)
		self.sub1 = tk.Button(self.frame_sub, text="EN1002 : ENGLISH FOR ENGINEERS", font=("Garamond",15), width=50, height=1, bg="#FFFDD0", fg="#000000", command=self.viewenglish)
		self.sub1.pack(pady=10, padx=10, anchor='center', expand=True)
		self.sub2 = tk.Button(self.frame_sub, text="MA1002 : PROBABILITY AND STATISTICS", font=("Garamond",15), width=50, height=1, bg="#FFFDD0", fg="#000000", command=self.viewmath)
		self.sub2.pack(pady=10, padx=10, anchor='center', expand=True)
		self.sub3 = tk.Button(self.frame_sub, text="CS1002 : PROGRAMMING IN PYTHON", font=("Garamond",15), width=50, height=1, bg="#FFFDD0", fg="#000000", command=self.viewpython)
		self.sub3.pack(pady=10, padx=10, anchor='center', expand=True)
		self.sub4 = tk.Button(self.frame_sub, text="CS1006T : DATA STRUCTURES", font=("Garamond",15), width=50, height=1, bg="#FFFDD0", fg="#000000", command=self.viewdsa)
		self.sub4.pack(pady=10, padx=10, anchor='center', expand=True)
		self.sub5 = tk.Button(self.frame_sub, text="CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE", font=("Garamond",15), width=50, height=1, bg="#FFFDD0", fg="#000000", command=self.viewcoa)
		self.sub5.pack(pady=10, padx=10, anchor='center', expand=True)
		self.sub6 = tk.Button(self.frame_sub, text="CS1008 : CLASSICAL CRYPTOGRAPHY", font=("Garamond",15), width=50, height=1, bg="#FFFDD0", fg="#000000", command=self.viewcc)
		self.sub6.pack(pady=10, padx=10, anchor='center', expand=True)
		self.goback=tk.Button(self.frame_sub, text="BACK", font=("Garamond",15), width=20, height=1, bg="#FFFDD0", fg="#000000", command=self.show_stdmain_frame)
		self.goback.pack(pady=10, padx=10, anchor='center', expand=True)
		self.frame_sub.pack_forget()
#frameformodifyauthenticateptoa
		self.frame_modauthentication1 = tk.Frame(self.master)
		self.frame_modauthentication1.config(bg="#2b2a2a")
		self.title = tk.Label(self.frame_modauthentication1, text="YOU CAN MODIFY THE RECORDS ONLY \nWHEN YOU HAVE THE RIGHT AUTHENTICATION",font=("Footlight MT Light", 30, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=CENTER)
		self.title.grid(row=0, column=0, padx=30, pady=30, columnspan=3)
		self.goback = tk.Button(self.frame_modauthentication1, text="BACK", font=("Garamond", 15), width=20, height=1,bg="#FFFDD0", fg="#000000", command=self.show_stdmain_frame)
		self.goback.grid(row=1, column=0, pady=10, padx=10)
		self.authenticate = tk.Button(self.frame_modauthentication1, text="AUTHENTICATE", font=("Garamond", 15), width=20, height=1,bg="#FFFDD0", fg="#000000", command=self.modifyauthenticate1)
		self.authenticate.grid(row=1, column=1, pady=10, padx=10)
		self.exit = tk.Button(self.frame_modauthentication1, text="EXIT", font=("Garamond", 15), width=20, height=1,bg="#FFFDD0", fg="#000000", command=self.exit)
		self.exit.grid(row=1, column=2, pady=10, padx=10)
		self.frame_modauthentication1.pack_forget()
#frameformodifyauthenticateatop
		self.frame_modauthentication2 = tk.Frame(self.master)
		self.frame_modauthentication2.config(bg="#2b2a2a")
		self.title = tk.Label(self.frame_modauthentication2, text="YOU CAN MODIFY THE RECORDS ONLY \nWHEN YOU HAVE THE RIGHT AUTHENTICATION",font=("Footlight MT Light", 30, "bold"), bg="#2b2a2a", fg="#C4C0C0", justify=CENTER)
		self.title.grid(row=0, column=0, padx=30, pady=30, columnspan=3)
		self.goback = tk.Button(self.frame_modauthentication2, text="BACK", font=("Garamond", 15), width=20, height=1,bg="#FFFDD0", fg="#000000", command=self.show_stdmain_frame)
		self.goback.grid(row=1, column=0, pady=10, padx=10)
		self.authenticate = tk.Button(self.frame_modauthentication2, text="AUTHENTICATE", font=("Garamond", 15), width=20, height=1,bg="#FFFDD0", fg="#000000", command=self.modifyauthenticate2)
		self.authenticate.grid(row=1, column=1, pady=10, padx=10)
		self.exit = tk.Button(self.frame_modauthentication2, text="EXIT", font=("Garamond", 15), width=20, height=1,bg="#FFFDD0", fg="#000000", command=self.exit)
		self.exit.grid(row=1, column=2, pady=10, padx=10)
		self.frame_modauthentication2.pack_forget()
#studentauthenticate
	def studentlogin(self):
		df = pd.read_excel("C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx", sheet_name="Students")
		rollname = [int(str(r).strip()) for r in list(df['ROLL NO'])]
		barcodes = scan_barcodes(5)
		global num
		if barcodes:
			if all(x.isnumeric() for x in barcodes):
				if any(r in [int(b) for b in barcodes] for r in rollname):
					self.show_stdmain_frame()
				else:
					messagebox.showwarning("WARNING", "{rollnum} doesn't belong to Cyber Security Class".format(rollnum=barcodes[0]))
			else:
				messagebox.showwarning("WARNING", "{rollnum} doesn't belong to Shiv Nadar University, Chennai".format(rollnum=barcodes[0]))
				self.show_main()
		else:
			response = messagebox.askretrycancel("ERROR", "No Barcodes were Scanned \nDo you want to display the barcode again?")
			if response:
				self.studentlogin()
			else:
				self.show_main()
		if all(x.isnumeric() for x in barcodes):
			num = int(barcodes[0])
#facultyauthenticate
	def facultylogin(self):
		sub = None
		facandcourse = {"CS1002" : "CS1002", "EN1002" : "EN1002", "MA1002" : "MA1002", "CS1004" : "CS1004", "CS1006T" : "CS1006T", "CS1008" : "CS1008"}
		facnums = scan_barcodes(5)
		global facnum,coursename
		if facnums:
				if any(r in [fac for fac in facnums] for r in facandcourse.keys()):
					coursename = next((facandcourse[r] for r in facandcourse.keys() if r in facnums), None)
					facnum = facnums[0]
					self.show_facmain_frame()
				else:
					messagebox.showerror("ERROR", "{bar}doesn't belong to faculty member of Cyber Security Batch".format(bar=facnums[0]))
		else:
			response = messagebox.askretrycancel("ERROR", "No Barcodes were Scanned \nDo you want to display the barcode again?")
			if response:
				self.facultylogin()
			else:
				self.show_main()
#functionformodifying
	def modify_auth(self):
		selected_date=self.cal2.get_date()
		today = selected_date.strftime("%d-%m-%Y")
		selected_sub=self.var.get()
		if selected_sub == "EN1002 : ENGLISH FOR ENGINEERS":
			wb = xl.load_workbook("C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx")
			sheet = wb["EN1002"]
			date_col_index = None
			num_row_index = None
			for col in range(1, sheet.max_column+1):
				if sheet.cell(row=1, column=col).value == today:
					date_col_index = col
			for row in range(2, sheet.max_row+1):
				if sheet.cell(row=row, column=2).value == num:
					num_row_index = row
					break
			if date_col_index and num_row_index:
				if sheet.cell(row=num_row_index, column=date_col_index).value == "P" or sheet.cell(row=num_row_index, column=date_col_index).value == "p" or sheet.cell(row=num_row_index, column=date_col_index).value == "Present" or sheet.cell(row=num_row_index, column=date_col_index).value == "present" or sheet.cell(row=num_row_index, column=date_col_index).value == "1":
					response = messagebox.askquestion("INFO", "{rollnum} have been marked PRESENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication1()
					else:
						self.show_stdmain_frame()
				else:
					response = messagebox.askquestion("INFO", "{rollnum} have been marked ABSENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication2()
					else:
						self.show_stdmain_frame()
			else:
				messagebox.showerror("ERROR","Date was not found")
		elif selected_sub == "MA1002 : PROBABILITY & STATISTICS":
			wb = xl.load_workbook("C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx")
			sheet = wb["MA1002"]
			date_col_index = None
			num_row_index = None
			for col in range(1, sheet.max_column+1):
				if sheet.cell(row=1, column=col).value == today:
					date_col_index = col
			for row in range(2, sheet.max_row+1):
				if sheet.cell(row=row, column=2).value == num:
					num_row_index = row
					break
			if date_col_index and num_row_index:
				if sheet.cell(row=num_row_index, column=date_col_index).value == "P" or sheet.cell(row=num_row_index, column=date_col_index).value == "p" or sheet.cell(row=num_row_index, column=date_col_index).value == "Present" or sheet.cell(row=num_row_index, column=date_col_index).value == "present" or sheet.cell(row=num_row_index, column=date_col_index).value == "1":
					response = messagebox.askquestion("INFO", "{rollnum} have been marked PRESENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication1()
					else:
						self.show_stdmain_frame()
				else:
					response = messagebox.askquestion("INFO", "{rollnum} have been marked ABSENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication2()
					else:
						self.show_stdmain_frame()
			else:
				messagebox.showerror("ERROR","Date was not found")
		elif selected_sub == "CS1002 : PROGRAMMING IN PYTHON":
			wb = xl.load_workbook("C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx")
			sheet = wb["CS1002"]
			date_col_index = None
			num_row_index = None
			for col in range(1, sheet.max_column+1):
				if sheet.cell(row=1, column=col).value == today:
					date_col_index = col
			for row in range(2, sheet.max_row+1):
				if sheet.cell(row=row, column=2).value == num:
					num_row_index = row
					break
			if date_col_index and num_row_index:
				if sheet.cell(row=num_row_index, column=date_col_index).value == "P" or sheet.cell(row=num_row_index, column=date_col_index).value == "p" or sheet.cell(row=num_row_index, column=date_col_index).value == "Present" or sheet.cell(row=num_row_index, column=date_col_index).value == "present" or sheet.cell(row=num_row_index, column=date_col_index).value == "1":
					response = messagebox.askquestion("INFO", "{rollnum} have been marked PRESENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication1()
					else:
						self.show_stdmain_frame()
				else:
					response = messagebox.askquestion("INFO", "{rollnum} have been marked ABSENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication2()
					else:
						self.show_stdmain_frame()
			else:
				messagebox.showerror("ERROR","Date was not found")
		elif selected_sub == "CS1006T : DATA STRUCTURES":
			wb = xl.load_workbook("C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx")
			sheet = wb["CS1006T"]
			date_col_index = None
			num_row_index = None
			for col in range(1, sheet.max_column+1):
				if sheet.cell(row=1, column=col).value == today:
					date_col_index = col
			for row in range(2, sheet.max_row+1):
				if sheet.cell(row=row, column=2).value == num:
					num_row_index = row
					break
			if date_col_index and num_row_index:
				if sheet.cell(row=num_row_index, column=date_col_index).value == "P" or sheet.cell(row=num_row_index, column=date_col_index).value == "p" or sheet.cell(row=num_row_index, column=date_col_index).value == "Present" or sheet.cell(row=num_row_index, column=date_col_index).value == "present" or sheet.cell(row=num_row_index, column=date_col_index).value == "1":
					response = messagebox.askquestion("INFO", "{rollnum} have been marked PRESENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication1()
					else:
						self.show_stdmain_frame()
				else:
					response = messagebox.askquestion("INFO", "{rollnum} have been marked ABSENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication2()
					else:
						self.show_stdmain_frame()
			else:
				messagebox.showerror("ERROR","Date was not found")
		elif selected_sub == "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE":
			wb = xl.load_workbook("C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx")
			sheet = wb["CS1004"]
			date_col_index = None
			num_row_index = None
			for col in range(1, sheet.max_column+1):
				if sheet.cell(row=1, column=col).value == today:
					date_col_index = col
			for row in range(2, sheet.max_row+1):
				if sheet.cell(row=row, column=2).value == num:
					num_row_index = row
					break
			if date_col_index and num_row_index:
				if sheet.cell(row=num_row_index, column=date_col_index).value == "P" or sheet.cell(row=num_row_index, column=date_col_index).value == "p" or sheet.cell(row=num_row_index, column=date_col_index).value == "Present" or sheet.cell(row=num_row_index, column=date_col_index).value == "present" or sheet.cell(row=num_row_index, column=date_col_index).value == "1":
					response = messagebox.askquestion("INFO", "{rollnum} have been marked PRESENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication1()
					else:
						self.show_stdmain_frame()
				else:
					response = messagebox.askquestion("INFO", "{rollnum} have been marked ABSENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication2()
					else:
						self.show_stdmain_frame()
			else:
				messagebox.showerror("ERROR","Date was not found")
		elif selected_sub == "CS1008 : CLASSICAL CRYPTOGRAPHY":
			wb = xl.load_workbook("C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx")
			sheet = wb["CS1008"]
			date_col_index = None
			num_row_index = None
			for col in range(1, sheet.max_column+1):
				if sheet.cell(row=1, column=col).value == today:
					date_col_index = col
			for row in range(2, sheet.max_row+1):
				if sheet.cell(row=row, column=2).value == num:
					num_row_index = row
					break
			if date_col_index and num_row_index:
				if sheet.cell(row=num_row_index, column=date_col_index).value == "P" or sheet.cell(row=num_row_index, column=date_col_index).value == "p" or sheet.cell(row=num_row_index, column=date_col_index).value == "Present" or sheet.cell(row=num_row_index, column=date_col_index).value == "present" or sheet.cell(row=num_row_index, column=date_col_index).value == "1":
					response = messagebox.askquestion("INFO", "{rollnum} have been marked PRESENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication1()
					else:
						self.show_stdmain_frame()
				else:
					response = messagebox.askquestion("INFO", "{rollnum} have been marked ABSENT on {date} \nDo you want to modify it?".format(rollnum=num,date=today))
					if response == "yes":
						self.show_frame_modauthentication2()
					else:
						self.show_stdmain_frame()
			else:
				messagebox.showerror("ERROR","Date was not found")
#authenticationfrompresentoabsent
	def modifyauthenticate1(self):
		barcodes = scan_barcodes(5)
		if "22110169" in barcodes:
			self.modifyingptoa()
		elif barcodes==[]:
			answer = messagebox.askretrycancel("ERROR", "No Barcodes were Scanned \nShow the Authentication Card Again")
			if answer:
				self.modifyauthenticate1()
		else:
			self.show_stdmain_frame()
			messagebox.showerror("ERROR", "YOU DO NOT HAVE \nTHE RIGHT AUTHENTICATION")
#authenticationfromabsenttopresent
	def modifyauthenticate2(self):
		barcodes = scan_barcodes(5)
		if "22110169" in barcodes:
			self.modifyingatop()
		elif barcodes==[]:
			answer = messagebox.askretrycancel("ERROR", "No Barcodes were Scanned \nShow the Authentication Card Again")
			if answer:
				self.modifyauthenticate2()
		else:
			self.show_stdmain_frame()
			messagebox.showerror("ERROR", "YOU DO NOT HAVE \nTHE RIGHT AUTHENTICATION")
#frameforpresenttoabsent
	def modifyingptoa(self):
		path = "C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		selected_date=self.cal2.get_date()
		today = selected_date.strftime("%d-%m-%Y")
		selected_sub = self.var.get()
		scanned_num = num
		if selected_sub == "EN1002 : ENGLISH FOR ENGINEERS":
			sheet = "EN1002"
			presenttoabsent(path,sheet,today,scanned_num)
		elif selected_sub == "MA1002 : PROBABILITY & STATISTICS":
			sheet = "MA1002"
			presenttoabsent(path,sheet,today,scanned_num)
		elif selected_sub == "CS1002 : PROGRAMMING IN PYTHON":
			sheet = "CS1002"
			presenttoabsent(path,sheet,today,scanned_num)
		elif selected_sub == "CS1006T : DATA STRUCTURES":
			sheet = "CS1006T"
			presenttoabsent(path,sheet,today,scanned_num)
		elif selected_sub == "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE":
			sheet = "CS1004"
			presenttoabsent(path,sheet,today,scanned_num)
		elif selected_sub == "CS1008 : CLASSICAL CRYPTOGRAPHY":
			sheet = "CS1008"
			presenttoabsent(path,sheet,today,scanned_num)
			
#frameforabsenttopresent
	def modifyingatop(self):
		path = "C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		selected_date=self.cal2.get_date()
		today = selected_date.strftime("%d-%m-%Y")
		selected_sub = self.var.get()
		scanned_num = num
		if selected_sub == "EN1002 : ENGLISH FOR ENGINEERS":
			sheet = "EN1002"
			absenttopresent(path,sheet,today,scanned_num)
		elif selected_sub == "MA1002 : PROBABILITY & STATISTICS":
			sheet = "MA1002"
			absenttopresent(path,sheet,today,scanned_num)
		elif selected_sub == "CS1002 : PROGRAMMING IN PYTHON":
			sheet = "CS1002"
			absenttopresent(path,sheet,today,scanned_num)
		elif selected_sub == "CS1006T : DATA STRUCTURES":
			sheet = "CS1006T"
			absenttopresent(path,sheet,today,scanned_num)
		elif selected_sub == "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE":
			sheet = "CS1004"
			absenttopresent(path,sheet,today,scanned_num)
		elif selected_sub == "CS1008 : CLASSICAL CRYPTOGRAPHY":
			sheet = "CS1008"
			absenttopresent(path,sheet,today,scanned_num)
			
#functiondateandtimechecking
	def checkdateandtime(self):
		df = pd.read_excel("C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx", sheet_name="Students")
		path = 'C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx'
		rollname = [int(str(r).strip()) for r in list(df['ROLL NO'])]
		barcodes = scan_barcodes(5)
		selected_date=self.cal.get_date()
		selected_time=self.var1.get()
		selected_sub=self.var2.get()
		current_day = datetime.now()
		current_date = current_day.date()
		current_time = current_day.time()
		login_code = num
		if barcodes:
			if all(x.isdigit() for x in barcodes):
				if any(r in [int(b) for b in barcodes] for r in rollname):
					scanned_code = int(barcodes[0])
					if scanned_code == login_code:
						if selected_date == current_date:
							if selected_time == "SESSION ONE : 08:10 AM TO 09:00 AM" and "08:10" <= current_time.strftime("%H:%M") <= "23:00":
								if selected_sub == "EN1002 : ENGLISH FOR ENGINEERS":
									sheet = 'EN1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "MA1002 : PROBABILITY & STATISTICS":
									sheet = 'MA1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1002 : PROGRAMMING IN PYTHON":
									sheet = 'CS1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1006T : DATA STRUCTURES":
									sheet = 'CS1006T'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE":
									sheet = 'CS1004'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1008 : CLASSICAL CRYPTOGRAPHY":
									sheet = 'CS1008'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
							elif selected_time == "SESSION TWO : 09:00 AM TO 09:50 AM" and "09:00" <= current_time.strftime("%H:%M") <= "09:50":
								if selected_sub == "EN1002 : ENGLISH FOR ENGINEERS":
									sheet = 'EN1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "MA1002 : PROBABILITY & STATISTICS":
									sheet = 'MA1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1002 : PROGRAMMING IN PYTHON":
									sheet = 'CS1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1006T : DATA STRUCTURES":
									sheet = 'CS1006T'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE":
									sheet = 'CS1004'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1008 : CLASSICAL CRYPTOGRAPHY":
									sheet = 'CS1008'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
							elif selected_time == "SESSION THREE : 10:10 AM TO 11:00 AM" and "10:10" <= current_time.strftime("%H:%M") <= "11:00":
								if selected_sub == "EN1002 : ENGLISH FOR ENGINEERS":
									sheet = 'EN1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "MA1002 : PROBABILITY & STATISTICS":
									sheet = 'MA1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1002 : PROGRAMMING IN PYTHON":
									sheet = 'CS1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1006T : DATA STRUCTURES":
									sheet = 'CS1006T'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE":
									sheet = 'CS1004'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1008 : CLASSICAL CRYPTOGRAPHY":
									sheet = 'CS1008'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
							elif selected_time == "SESSION FOUR : 11:00 AM TO 11:50 AM" and "11:00" <= current_time.strftime("%H:%M") <= "11:50":
								if selected_sub == "EN1002 : ENGLISH FOR ENGINEERS":
									sheet = 'EN1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "MA1002 : PROBABILITY & STATISTICS":
									sheet = 'MA1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1002 : PROGRAMMING IN PYTHON":
									sheet = 'CS1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1006T : DATA STRUCTURES":
									sheet = 'CS1006T'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE":
									sheet = 'CS1004'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1008 : CLASSICAL CRYPTOGRAPHY":
									sheet = 'CS1008'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
							elif selected_time == "SESSION FIVE : 12:50 PM TO 01:40 PM" and "12:50" <= current_time.strftime("%H:%M") <= "13:40":
								if selected_sub == "EN1002 : ENGLISH FOR ENGINEERS":
									sheet = 'EN1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "MA1002 : PROBABILITY & STATISTICS":
									sheet = 'MA1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1002 : PROGRAMMING IN PYTHON":
									sheet = 'CS1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1006T : DATA STRUCTURES":
									sheet = 'CS1006T'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE":
									sheet = 'CS1004'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1008 : CLASSICAL CRYPTOGRAPHY":
									sheet = 'CS1008'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
							elif selected_time == "SESSION SIX : 01:40 PM TO 02:30 PM" and "13:40" <= current_time.strftime("%H:%M") <= "14:30":
								if selected_sub == "EN1002 : ENGLISH FOR ENGINEERS":
									sheet = 'EN1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "MA1002 : PROBABILITY & STATISTICS":
									sheet = 'MA1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1002 : PROGRAMMING IN PYTHON":
									sheet = 'CS1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1006T : DATA STRUCTURES":
									sheet = 'CS1006T'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE":
									sheet = 'CS1004'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1008 : CLASSICAL CRYPTOGRAPHY":
									sheet = 'CS1008'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
							elif selected_time == "SESSION SEVEN : 02:40 PM TO 03:30 PM" and "14:40" <= current_time.strftime("%H:%M") <= "15:30":
								if selected_sub == "EN1002 : ENGLISH FOR ENGINEERS":
									sheet = 'EN1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "MA1002 : PROBABILITY & STATISTICS":
									sheet = 'MA1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1002 : PROGRAMMING IN PYTHON":
									sheet = 'CS1002'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1006T : DATA STRUCTURES":
									sheet = 'CS1006T'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1004 : COMPUTER ORGANIZATION AND ARCHITECTURE":
									sheet = 'CS1004'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
								elif selected_sub == "CS1008 : CLASSICAL CRYPTOGRAPHY":
									sheet = 'CS1008'
									write_date_to_sub(path,sheet,selected_date)
									add_p(login_code,path,sheet)
							else:
								self.show_frame_details
								messagebox.showwarning("WARNING", "YOU CANNOT ADD ATTENDANCE \nGIVE CURRENT TIME")
						else:
							messagebox.showwarning("WARNING", "YOU CANNOT ADD ATTENDANCE \nGIVE TODAY'S DATE")
					else:
						self.show_frame_details()
						messagebox.showwarning("WARNING, {rollnum} is not your roll number \nAdd Attendance only for your roll number!!")
				else:
					self.show_frame_details()
					messagebox.showwarning("WARNING", "{rollnum} doesn't belong to Cyber Security Class".format(rollnum=barcodes[0]))
			else:
				self.show_frame_details()
				messagebox.showwarning("WARNING", "{rollnum} doesn't belong to Shiv Nadar University, Chennai".format(rollnum=barcodes[0]))
		else:
			response = messagebox.askretrycancel("ERROR", "No Barcodes were Scanned \nDo you want to display the barcode again?")
			if response:
				self.checkdateandtime()
			else:
				self.show_frame_details()
			
	def exit(self):
		root.destroy()
		sys.exit()

	def opensecsem(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = "SEMTWOTT"
		protected_view_excel(path,sheet)

	def opentwocoursesandfac(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = "SEMTWO"
		protected_view_excel(path,sheet)
	
	def show_main(self):
		self.camera_frame1.pack_forget()
		self.camera_frame2.pack_forget()
		self.stdmain.pack_forget()
		self.facmain.pack_forget()
		self.main.pack()
		
	def show_camera_frame1(self):
		self.main.pack_forget()
		self.stdmain.pack_forget()
		self.camera_frame1.pack()

	def show_camera_frame2(self):
		self.main.pack_forget()
		self.facmain.pack_forget()
		self.camera_frame2.pack()

	def show_stdmain_frame(self):
		self.main.pack_forget()
		self.frame_sub.pack_forget()
		self.camera_frame1.pack_forget()
		self.frame_details.pack_forget()
		self.frame_modifyauth.pack_forget()
		self.frame_tt.pack_forget()
		self.frame_modauthentication2.pack_forget()
		self.frame_modauthentication1.pack_forget()
		self.stdmain.pack()

	def show_facmain_frame(self):
		self.main.pack_forget()
		self.camera_frame2.pack_forget()
		self.framett.pack_forget()
		self.facattrec.pack_forget()
		self.facmain.pack()

	def show_facattrec_frame(self):
		self.facmain.pack_forget()
		self.facattrec.pack()

	def show_frame_details(self):
		self.stdmain.pack_forget()
		self.frame_details.pack()

	def show_frame_tt(self):
		self.stdmain.pack_forget()
		self.frame_tt.pack()

	def show_framett(self):
		self.facmain.pack_forget()
		self.framett.pack()

	def show_frame_studentauth(self):
		self.main.pack_forget()
		self.frame_studentauth.pack()

	def show_frame_modifyauth(self):
		self.stdmain.pack_forget()
		self.frame_modauthentication2.pack_forget()
		self.frame_modauthentication1.pack_forget()
		self.frame_modifyauth.pack()

	def show_frame_modauthentication1(self):
		self.frame_modifyauth.pack_forget()
		self.stdmain.pack_forget()
		self.frame_modauthentication1.pack()

	def show_frame_modauthentication2(self):
		self.frame_modifyauth.pack_forget()
		self.stdmain.pack_forget()
		self.frame_modauthentication2.pack()

	def show_frame_sub(self):
		self.stdmain.pack_forget()
		self.frame_sub.pack()

	def convert_to_list(self):
		numbers_string = self.numbers_entry.get()
		numbers_list = numbers_string.split(",")
		numbers_list = [int(num.strip()) for num in numbers_list]
		return numbers_list
	
	def markpresent(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = coursename
		selected_date = self.cale.get_date()  # assuming self.cale.get_date() returns a string
		write_date_to_sub(path,sheet,selected_date)
		val = self.convert_to_list()
		markpresent(path,sheet,selected_date,val)

	def markabsent(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = coursename
		selected_date = self.cale.get_date()  # assuming self.cale.get_date() returns a string
		write_date_to_sub(path,sheet,selected_date)
		val = self.convert_to_list()
		markabsent(path,sheet,selected_date,val)

	def viewfacsub(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = coursename
		protected_view_excel(path,sheet)

	def viewstudent(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = "Students"
		protected_view_excel(path,sheet)

	def viewenglish(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = "EN1002"
		protected_view_excel(path,sheet)

	def viewmath(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = "MA1002"
		protected_view_excel(path,sheet)

	def viewpython(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = "CS1002"
		protected_view_excel(path,sheet)

	def viewdsa(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = "CS1006T"
		protected_view_excel(path,sheet)

	def viewcoa(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = "CS1004"
		protected_view_excel(path,sheet)

	def viewcc(self):
		path = r"C:\\Users\\jaya2\\MVSC\\cia2\\CyberSecurity.xlsx"
		sheet = "CS1008"
		protected_view_excel(path,sheet)

root = tk.Tk()
root.withdraw()
showloadingscreen()
root.deiconify()
app = App(root)
root.title("CyberX Attendance")
root.geometry("1000x550")
root.configure(bg="#2b2a2a")
root.resizable(False, False)
root.mainloop()