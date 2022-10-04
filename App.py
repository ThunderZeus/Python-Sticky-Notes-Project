#importing libraries and modules
import sqlite3 as sql
from tkinter import *
from tkinter import messagebox

#Creating the GUI Window:
window=Tk()
window.geometry("700x600")
window.title("ProjectGurukul Pin Your Notes")
Label(window,text="Pin Your Notes with ProjectGurukul").pack()

Note_Title_Label=Label(window,text="Note Title:").pack()
Note_Title_Entry=Entry(window)
Note_Title_Entry.pack()
 
Txt_Label=Label(window,text="Enter Your Text Here:").pack()
Txt=Text(window)
Txt.pack()
 
Button(window, text="Create new Notes",command=create_notes,bg='pink').pack()
Button(window, text="View Notes",command=view_notes,bg='yellow').pack()
Button(window, text="Edit Notes",command=edit_notes,bg='yellow').pack()
Button(window, text="Delete Notes",command=delete_notes,bg='yellow').pack()

#Connecting to the DataBase:
# Create database connection and connect to table
try:
        con = sql.connect('ProjectGurukul.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE notes_table
                         ( notes_title text, notes text)''')
except:
        print("Connected to table of database")

#Create Notes Functionality:
def create_notes():
        #Get input values
        notes_title = Note_Title_Entry.get()
        notes = Txt.get("1.0", "end-1c")
        #Raise a prompt for missing values
        if  (len(notes_title)<=0) & (len(notes)<=1):
                messagebox.showerror(message = "Enter Details" )
        else:
        #Insert into the table
                cur.execute("INSERT INTO notes_table VALUES ('%s','%s')" %( notes_title, notes))
                messagebox.showinfo(message="Note added")
        #Commit to preserve the changes
                con.commit()
#Edit Button Functionality:
#Update the notes
def edit_notes():
        #Obtain user input
        notes_title = Note_Title_Entry.get()
        notes = Txt.get("1.0", "end-1c")
        #Check if input is given by the user
        if  (len(notes_title)<=0) & (len(notes)<=1):
                messagebox.showerror(message = "Enter Details:" )
        #update the note
        else:
                sql_statement = "UPDATE notes_table SET notes = '%s'  and notes_title ='%s'" %(notes, notes_title)
               
        cur.execute(sql_statement)
        messagebox.showinfo(message="Note Edited and Saved")
#View Button Functionality:
#Display all the notes
def view_notes():
        #Obtain all the user input
        notes_title = Note_Title_Entry.get()
        #If no input is given, retrieve all notes
        if(len(notes_title)<=0):
                sql_statement = "SELECT * FROM notes_table"
               
        #Retrieve notes matching a title
        elif (len(notes_title)>0):
                sql_statement = "SELECT * FROM notes_table where notes_title ='%s'" %notes_title
 
               
        #Execute the query
        cur.execute(sql_statement)
        #Obtain all the contents of the query
        row = cur.fetchall()
        #Check if none was retrieved
        if len(row)<=0:
                messagebox.showerror(message="Note not Found")
        else:
                #Print the notes
                for i in row:
                        messagebox.showinfo(message=+"\nTitle: "+i[0]+"\nNotes: "+i[1])
 #Delete Button Functionality:
#Delete the notes
def delete_notes():
        #Obtain input values
        notes_title = Note_Title_Entry.get()
        #Ask if user wants to delete all notes
        choice = messagebox.askquestion(message="Do you want to delete all notes?")
        #If yes is selected, delete all
        if choice == 'yes':
                sql_statement = "DELETE FROM notes_table"  
        else:
        #Delete notes matching a particular date and title
                if (len(notes_title)<=0):  
                        #Raise error for no inputs
                        messagebox.showerror(message = "Enter Details:" )
                        return
                else:
                        sql_statement = "DELETE FROM notes_table where date ='%s' and notes_title ='%s'" %( notes_title)
        #Execute the query
        cur.execute(sql_statement)
        messagebox.showinfo(message="Note(s) Deleted")
        con.commit()
 
