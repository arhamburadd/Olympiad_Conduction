from tkinter import *
import mysql.connector as ms
from tkinter import messagebox

connection = ms.connect(host="localhost",user='root',password="Arham@26",database='arham')
cursor = connection.cursor()
def e(var,index,mode):
    ab=entry_idd.get()
    try:
        cursor.execute(f"select * from subjects where id='{ab}'")    
        b=cursor.fetchall()
        for i in b:
            phys=i[1]    
            chem=i[2]
            math=i[3]
            eng=i[4]
            bio=i[5]
            csc=i[6]
        if phys == 'no':
            entry_p.config(state=DISABLED)
        if chem == 'no': 
            entry_c.config(state=DISABLED)
        if bio == 'no':
            entry_b.config(state=DISABLED)
        if csc == 'no':
            entry_cs.config(state=DISABLED)
        if math == 'no':
            entry_m.config(state=DISABLED)
        if eng == 'no':
            entry_e.config(state=DISABLED) 
    except:
        return messagebox.showerror('Incorrect ID','Enter Correct ID')



count=0
def f():
    global count
    count+=1
    try:    
        ab=entry_idd.get()
        query=f'insert into results values({ab},'
        if entry_p.get().isnumeric():
            p=float(entry_p.get())
            query+=f'{p},'
        else:
            query+='NULL,'

        if entry_c.get().isnumeric():
            c=float(entry_c.get())
            query+=f'{c},'
        else:
            query+='NULL,'

        if entry_b.get().isnumeric():
            b=float(entry_b.get())
            query+=f'{b},'
        else:
            query+='NULL,'

        if entry_m.get().isnumeric():
            m=float(entry_m.get())
            query+=f'{m},'
        else:
            query+='NULL,'

        if entry_e.get().isnumeric():
            e=float(entry_e.get())
            query+=f'{e},'
        else:
            query+='NULL,'

        if entry_cs.get().isnumeric():
            cs=float(entry_cs.get())
            query+=f'{cs})'
        else:
            query+='NULL)'
        
        cursor.execute(query)
        connection.commit()
        bvar.set("")
        cvar.set("")
        csvar.set("")
        mvar.set("")
        pvar.set("")
        evar.set("")
        entry_b['state']=NORMAL
        entry_c['state']=NORMAL
        entry_e['state']=NORMAL
        entry_m['state']=NORMAL
        entry_cs['state']=NORMAL
        entry_p['state']=NORMAL
    except:
        return messagebox.showerror('Incorrect Details','Please Try Again')
    


def host():
    global entry_b,entry_c,entry_m,entry_p,entry_idd,entry_e,entry_cs,count,bvar,pvar,evar,csvar,cvar,mvar,Entry_var
    im=Tk()
    im.geometry("400x400")
    im.title("Host.")
    im.config(background="light blue")

    label0=Label(im,text="Please Enter the ID:",pady=-2,font=('Bold',9))
    label0.place(x=5,y=3)
    Entry_var=StringVar(im)
    Entry_var.trace_add('write', callback=e)

    entry_idd=Entry(im,width=25,textvariable=Entry_var)
    entry_idd.place(x=120,y=3)

    pvar=StringVar(im)
    cvar=StringVar(im)
    mvar=StringVar(im)
    csvar=StringVar(im)
    evar=StringVar(im)
    bvar=StringVar(im)
    

    label1=Label(im,text="Please Enter the Physics marks:",pady=-2,font=('Bold',9),bg='white')
    label1.place(x=5,y=25)
    entry_p=Entry(im,width=25,textvariable=pvar)
    entry_p.place(x=188,y=25)

    label=Label(im,text="Please Enter the Chemistry Marks:",pady=-2,font=('Bold',9),bg='white')
    label.place(x=5,y=47)
    entry_c=Entry(im,width=25,textvariable=cvar)
    entry_c.place(x=199,y=47)

    label=Label(im,text="Please Enter the Maths Marks:",pady=-2,font=('Bold',9),bg='white')
    label.place(x=5,y=69)
    entry_m=Entry(im,width=25,textvariable=mvar)
    entry_m.place(x=176,y=69)
    
    label=Label(im,text="Please Enter the Biology Marks:",pady=-2,font=('Bold',9),bg='white')
    label.place(x=5,y=91)
    entry_b=Entry(im,width=25,textvariable=bvar)
    entry_b.place(x=183,y=91)


    label=Label(im,text="Please Enter the CSC Marks:",pady=-2,font=('Bold',9),bg='white')
    label.place(x=5,y=113)
    entry_cs=Entry(im,width=25,textvariable=csvar)
    entry_cs.place(x=170,y=113)

    label=Label(im,text="Please Enter the English Marks:",pady=-2,font=('Bold',9),bg='white')
    label.place(x=5,y=135)
    entry_e=Entry(im,width=25,textvariable=evar)
    entry_e.place(x=185,y=135)
    
    but=Button(im,text="Enter The results",command=f,font=('ariel',10,'bold'),fg='black',bg='white',
              activebackground='black',activeforeground='black')
    but.place(x=130,y=170)
    
    
    im.mainloop()
host()
