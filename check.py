
import tkinter
from tkinter import *
root=Tk()
root.title("To-do-list")
root.geometry("400x600")
root.resizable(False,False)
task_list=[]
def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("C:\\Users\\venky\\OneDrive\\Documents\\todolistt\\taskl.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
def deletetask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("C:\\Users\\venky\\OneDrive\\Documents\\todolistt\\taskl.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete( ANCHOR)        
        
def opentask():
    
    try:
        global task_list
        with open("C:\\Users\\venky\\OneDrive\\Documents\\todolistt\\taskl.txt","r") as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END , task)
                
    except:
        
        file=open("C:\\Users\\venky\\OneDrive\\Documents\\todolistt\\taskl.txt","w")
        file.close()

                
image_icon=PhotoImage(file="C:\\Users\\venky\\OneDrive\\Documents\\task.png")
root.iconphoto(False,image_icon)

topimage=PhotoImage(file="C:\\Users\\venky\\OneDrive\\Documents\\topbar.png")
Label(root,image=topimage).pack()

dockimage=PhotoImage(file="C:\\Users\\venky\\OneDrive\\Documents\\dock.png")
Label(root,image=dockimage,bg="#32405b").place(x=30,y=25)

noteimage=PhotoImage(file="C:\\Users\\venky\\OneDrive\\Documents\\task.png")
Label(root,image=noteimage,bg="#32405b").place(x=30,y=25)

heading=Label(root,text="MY TASKS",font="arial 20 bold",fg="white",bg="dark blue")
heading.place(x=130,y=20)
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="add",font="arial 20 bold",width=6,bg="blue",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=("arial",12),width=40,height=16,bg="#32405b" , fg="white",cursor="hand2",selectbackground="#5a95ff")

listbox.pack(side=LEFT , fill=BOTH ,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT , fill =BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

opentask()

delete_icon=PhotoImage(file="C:\\Users\\venky\\OneDrive\\Documents\\delete.png")
Button(root,image=delete_icon,bd=0,command=deletetask).pack(side=BOTTOM,pady=2)

root.mainloop()

