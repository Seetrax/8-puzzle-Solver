from tkinter import *
from tkinter import ttk
import time
import Search as nop

root =Tk()

root.title("N-puzzle")
he=50
we=50

def clicked ():
    new=Toplevel(root)
    new.title("Heuristic Selection")

    Label(new,text="Choose a Heuristic :" ).grid(row=0,column=0)    
    But1=Button(new,text="Sum of manhattan distances",width=50,pady=20,command=Smh)
    But1.grid(row=1,column=0)
    But2=Button(new,text="No of misplaced tiles",width=50,pady=20,command=Mt)
    But2.grid(row=2,column=0)
    But3=Button(new,text="Zero manhattan distance",width=50,pady=20,command=Zmh)
    But3.grid(row=3,column=0)
def Smh():
    '''m=[[int(e1.get()),int(e2.get()),int(e3.get())],[int(e4.get()),int(e5.get()),int(e6.get())],[int(e7.get()),int(e8.get()),int(e9.get())]]
    print(m)
    canvas_height=300
    canvas_width=300
    
    tt=nop.Asearch_smn(m,nop.fin)
    h=len(tt[0])
    w=len(tt[0][0])
    
    j=0
    for i in tt[0]:
        print(f"Step {j}")
        nop.printpuz(i)
        print()
        j+=1
    new=Toplevel(root)
    new.title("Nodes Explored")

    mycan=Canvas(new,width=600,height=300)
    mycan.grid(row=0,column=0)
    mycan.create_text(300,100,text=str(tt[1]) + " nodes were expanded",font=("arial", 14),justify=CENTER)
    mycan.create_text(300,150,text="Steps to solve the problem is printed in the terminal",font=("arial", 14),justify=CENTER)'''
    m=[[int(e1.get()),int(e2.get()),int(e3.get())],[int(e4.get()),int(e5.get()),int(e6.get())],[int(e7.get()),int(e8.get()),int(e9.get())]]
    print(m)

    tt=nop.Asearch_smn(m,nop.fin)
    h=len(tt[0])
    w=len(tt[0][0])
    new=Toplevel(root)
    new.title("Solution")
    mf=Frame(new)
    mycan=Canvas(new)
    mycan.pack(side=LEFT,fill=BOTH,expand=1)
    scroll=ttk.Scrollbar(new,orient=VERTICAL,command=mycan.yview)
    scroll.pack(side=RIGHT,fill=Y)
    mycan.configure(yscrollcommand=scroll.set)
    mycan.bind('<Configure>',lambda e : mycan.configure(scrollregion=mycan.bbox("all")))
    sf=Frame(mycan)
    mycan.create_window((0,0),window=sf,anchor="nw")
    '''for i in range(100):
        print(i)
        Button(sf,text="po",command=clicked).grid(row=i,column=0)'''
    space=2
    step=0
    Label(sf,text=str(tt[1]) + "  nodes were expanded to solve this problem").grid(row=0,column=0)
    Label(sf,text="Steps to solve the problem :").grid(row=1,column=0)
    for k in tt[0]:
        Label(sf,text="         ").grid(row=space,column=0)
        Label(sf,text="         ").grid(row=space+1,column=0)

        Label(sf,text=f'Step ' +str(step)+" :").grid(row=space+2,column=0)
        
        space+=2
        for i in range(len(k)):
            for j in range(len(k[i])):
                if k[i][j]==0:
                    Label(sf,text=" ").grid(row=i+space,column=j+1)
                else:
                    Label(sf,text=str(k[i][j])).grid(row=i+space,column=j+1)
        space+=4
        step+=1
def Zmh():
    m=[[int(e1.get()),int(e2.get()),int(e3.get())],[int(e4.get()),int(e5.get()),int(e6.get())],[int(e7.get()),int(e8.get()),int(e9.get())]]
    print(m)
    tt=nop.Asearch_zmn(m,nop.fin)
    h=len(tt[0])
    w=len(tt[0][0])
    new=Toplevel(root)
    new.title("Solution")
    mf=Frame(new)
    mycan=Canvas(new)
    mycan.pack(side=LEFT,fill=BOTH,expand=1)
    scroll=ttk.Scrollbar(new,orient=VERTICAL,command=mycan.yview)
    scroll.pack(side=RIGHT,fill=Y)
    mycan.configure(yscrollcommand=scroll.set)
    mycan.bind('<Configure>',lambda e : mycan.configure(scrollregion=mycan.bbox("all")))
    sf=Frame(mycan)
    mycan.create_window((0,0),window=sf,anchor="nw")
    '''for i in range(100):
        print(i)
        Button(sf,text="po",command=clicked).grid(row=i,column=0)'''
    space=2
    step=0
    Label(sf,text=str(tt[1]) + "  nodes were expanded to solve this problem").grid(row=0,column=0)
    Label(sf,text="Steps to solve the problem :").grid(row=1,column=0)
    for k in tt[0]:
        Label(sf,text="         ").grid(row=space,column=0)
        Label(sf,text="         ").grid(row=space+1,column=0)

        Label(sf,text=f'Step ' +str(step)+" :").grid(row=space+2,column=0)
        
        space+=2
        for i in range(len(k)):
            for j in range(len(k[i])):
                if k[i][j]==0:
                    Label(sf,text=" ").grid(row=i+space,column=j+1)
                else:
                    Label(sf,text=str(k[i][j])).grid(row=i+space,column=j+1)
        space+=4
        step+=1
def Mt():
    m=[[int(e1.get()),int(e2.get()),int(e3.get())],[int(e4.get()),int(e5.get()),int(e6.get())],[int(e7.get()),int(e8.get()),int(e9.get())]]
      
    print(m)
    tt=nop.Asearch_mt(m,nop.fin)
    h=len(tt[0])
    w=len(tt[0][0])
    new=Toplevel(root)
    new.title("Solution")
    mf=Frame(new)
    mycan=Canvas(new)
    mycan.pack(side=LEFT,fill=BOTH,expand=1)
    scroll=ttk.Scrollbar(new,orient=VERTICAL,command=mycan.yview)
    scroll.pack(side=RIGHT,fill=Y)
    mycan.configure(yscrollcommand=scroll.set)
    mycan.bind('<Configure>',lambda e : mycan.configure(scrollregion=mycan.bbox("all")))
    sf=Frame(mycan)
    mycan.create_window((0,0),window=sf,anchor="nw")
    '''for i in range(100):
        print(i)
        Button(sf,text="po",command=clicked).grid(row=i,column=0)'''
    space=2
    step=0
    Label(sf,text=str(tt[1]) + "  nodes were expanded to solve this problem").grid(row=0,column=0)
    Label(sf,text="Steps to solve the problem :").grid(row=1,column=0)
    for k in tt[0]:
        Label(sf,text="         ").grid(row=space,column=0)
        Label(sf,text="         ").grid(row=space+1,column=0)

        Label(sf,text=f'Step ' +str(step)+" :").grid(row=space+2,column=0)
        
        space+=2
        for i in range(len(k)):
            for j in range(len(k[i])):
                if k[i][j]==0:
                    Label(sf,text=" ").grid(row=i+space,column=j+1)
                else:
                    Label(sf,text=str(k[i][j])).grid(row=i+space,column=j+1)
        space+=4
        step+=1
           
    
##myLabel.pack()
frame=Frame(root,padx=50,pady=50)
frame.grid(row=2,column=0)
Label(root,text="   Enter the initial Config of the 8-puzzle problem :" ,font=("arial",14)).grid(row=0,column=0)
Label(root,text="  Please enter zero as entry for the empty box " ,font=("arial",10)).grid(row=1,column=0)

e1=Entry(frame,font=("arial", 36),width=2,borderwidth=5)
e1.grid(row=0,column=0)

e2=Entry(frame,font=("arial", 36),width=2,borderwidth=5)
e2.grid(row=0,column=1)

e3=Entry(frame,font=("arial", 36),width=2,borderwidth=5)
e3.grid(row=0,column=2)

e4=Entry(frame,font=("arial", 36),width=2,borderwidth=5)
e4.grid(row=1,column=0)

e5=Entry(frame,font=("arial", 36),width=2,borderwidth=5)
e5.grid(row=1,column=1)

e6=Entry(frame,font=("arial", 36),width=2,borderwidth=5)
e6.grid(row=1,column=2)

e7=Entry(frame,font=("arial", 36),width=2,borderwidth=5)
e7.grid(row=2,column=0)

e8=Entry(frame,font=("arial", 36),width=2,borderwidth=5)
e8.grid(row=2,column=1)

e9=Entry(frame,font=("arial", 36),width=2,borderwidth=5)
e9.grid(row=2,column=2)
But1=Button(root,text="Solve",padx=30,pady=20,command=clicked,fg='black',bg='green')
But1.grid(row=2,column=3)

'''But1=Button(root,text="Solve with sum of manhattan distances as heuristic",padx=30,pady=20,command=clicked,fg='yellow',bg='black')
But1.grid(row=0,column=3)
But2=Button(root,text="Solve with no of misplaced tiles as heuristic",padx=30,pady=20,command=clicked,fg='yellow',bg='black')
But2.grid(row=1,column=3)
But3=Button(root,text="Solve with manhattan distance of 0 alone as heuristic",padx=30,pady=20,command=clicked,fg='yellow',bg='black')
But3.grid(row=2,column=3)'''
root.mainloop()
