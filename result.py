from tkinter import *
import mysql.connector as ms
from tkinter import messagebox
connection = ms.connect(host="localhost",user='root',password="Arham@26",database='arham')
cursor = connection.cursor()
def res():
    im1=Tk()
    im1.geometry("350x250")
    im1.title("Results!")
    im1.config(background="light blue")

    cursor.execute(f"select * from results where id='{d}'")    
    b=cursor.fetchall()
    for i in b:
        phys=i[1]    
        chem=i[2]
        math=i[3]
        eng=i[4]
        bio=i[5]
        csc=i[6]
    try:
        if phys > 0 or phys < 100:
            label=Label(im1,text='Physics Mark:',bg='light blue').grid(column=0)
            label=Label(im1,text=f'{phys}',bg='light blue').grid(column=1)
    except:
        count=1
    try:
        if chem > 0 or chem < 100:
            label=Label(im1,text='Chemistry Mark:',bg='light blue').grid(column=0)
            label=Label(im1,text=f'{chem}',bg='light blue').grid(column=1)
    except:
        count=1
    try:
        if bio > 0 or bio < 100:
            label=Label(im1,text='Biology Mark:',bg='light blue').grid(column=0)
            label=Label(im1,text=f'{bio}',bg='light blue').grid(column=1)
    except:
        count=1
    try:
        if math > 0 or math < 100:
            label=Label(im1,text='Maths Mark:',bg='light blue').grid(column=0)
            label=Label(im1,text=f'{math}',bg='light blue').grid(column=1)
    except:
        count=1
    try:
        if eng > 0 or eng < 100:
            label=Label(im1,text='English Mark:',bg='light blue').grid(column=0)
            label=Label(im1,text=f'{eng}',bg='light blue').grid(column=1)
    except:
        count=1
    try: 
        if csc > 0 or csc < 100:
            label=Label(im1,text='Computer Science Mark:',bg='light blue').grid(column=0)
            label=Label(im1,text=f'{csc}',bg='light blue').grid(column=1)
    except:
        count=1

def z():
    global d,y
    d=entry.get()
    y=entry1.get()
    #try:
    cursor.execute(f"select id,passsword from ar where id={d}")
    a=cursor.fetchall()
    for i in a:
        id=i[0]
        passw=i[1]
    if y==passw:
        imm.destroy()
        res()
    #except:
        #return messagebox.showerror(title='Error!',message='Enter correct Details.')
    
def results():
    
    global a,b,entry,entry1,imm
    imm=Tk()
    imm.geometry("300x200")
    imm.title("Details.")
    imm.config(background="light blue")

    a=StringVar()
    label=Label(imm,text='ID:',background='light blue').grid(row=0,column=0)
    entry=Entry(imm,width=25,textvariable=a)
    entry.grid(row=0,column=1)

    b=StringVar()
    label=Label(imm,text='Password:',padx=5,pady=5,bg='light blue').grid(row=1,column=0)
    entry1=Entry(imm,width=25,textvariable=b)
    entry1.grid(row=1,column=1)
    
    but=Button(imm,text='Enter.',command=z,bg='white',fg='black').grid(row=2,column=1)

    imm.mainloop()
results()