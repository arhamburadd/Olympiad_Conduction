from tkinter import *
import mysql.connector as ms
from tkinter import messagebox
f=open('Initiate.txt','a')
f.close()
connection = ms.connect(host="localhost",user='root',password="Arham@26",database='arham')
cursor = connection.cursor()
print("Connection is established.")
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS ar (id float primary key,name varchar(20),passsword varchar(20),State varchar(40))")
    connection.commit()

    cursor.execute("""create table IF NOT EXISTS subjects(id float,Physics varchar(20),Chemistry varchar(20),Maths varchar(20),
    English varchar(20),Biology varchar(20),Computer_science varchar(20),foreign key(id) references ar(id));""")
    connection.commit()
    cursor.execute("""create table IF NOT EXISTS Results(id float,Physics_marks float,Chem_Marks float,Bio_marks float,Maths_marks float,Eng_Marks float,
    CSC_Marks float,Total_Marks float,Grade varchar(2),Percent Float,Status varchar(10),foreign key (id) references ar(id));""")
    connection.commit()


create_table()
def checkhost():
    d1=entry12.get()
    y1=entry13.get()

    if y1=='Arham' and d1 == '169':
        win1.destroy()
        host()
    elif d1 != 169 or y1 != 'Arham':
        return messagebox.showerror(title='Error!',message='Enter correct Details.')
    


def AIR():
    cursor.execute("create table if not exists air(id float,percent float,rank1 int);")
    connection.commit()
    cursor.execute("SELECT percent,id from results ORDER BY percent DESC;")
    fet=cursor.fetchall()
    connection.commit()
    print(fet)
    le=0
    for i in fet:
        le+=1
    print(le)
    for i,j in zip(fet,range(1,le+1)):
        print(i[0],j)
        perc=float(i[0])
        ID=i[1]
        air=int(j)
        cursor.execute(f"insert into air values({ID},{perc},{air})")
        connection.commit()


def stateC():
    global un1,un
    cursor.execute("select state from ar;")
    stat=cursor.fetchall()
    un=[]
    connection.commit()
    for i in stat:
        if i[0].lower() not in un:
            un.append(i[0].lower())

    un1=[]
    for i in range(len(un)):
        axx=''
        for j in range(len(un[i])):
            if un[i][j].isspace():
                axx+='_'
            else:
                axx+=un[i][j]
        un1.append(axx)

    for i in un1:
        cursor.execute(f"create table if not exists {i}(id int,percent float,rank1 int)")
        connection.commit()


def insertstate():
    for i,j in zip(un,un1):
        cursor.execute(f"select id,percent,state from results natural join ar where state='{i}' order by percent desc ;")
        fet=cursor.fetchall()
        connection.commit()
        length=len(fet)

        

        for k,x in zip(range(1,length+1),fet):
            cursor.execute(f"insert into {j} values({x[0]},{x[1]},{k});")
            connection.commit()


def initiate():

    AIR()
    stateC()
    insertstate()


def Host_check():
    global entry12,entry13,win1
    win1=Tk()
    win1.geometry("350x250")
    win1.title("Results!")
    win1.config(background="light blue")

    a=StringVar()
    label=Label(win1,text='Host ID:',background='light blue').grid(row=0,column=0)
    entry12=Entry(win1,width=25,textvariable=a)
    entry12.grid(row=0,column=1)

    b=StringVar()
    label=Label(win1,text='Password:',padx=5,pady=5,bg='light blue').grid(row=1,column=0)
    entry13=Entry(win1,width=25,textvariable=b)
    entry13.grid(row=1,column=1)

    butt=Button(win1,text='Enter.',bg='light blue',activebackground='light blue', activeforeground='black',command=checkhost).grid()



def Results_show():
    im1=Tk()
    im1.geometry("350x450")
    im1.title("Results!")
    im1.config(background="light blue")

    cursor.execute(f"select * from results where id='{d}'") 
    b=cursor.fetchall()
    connection.commit()
    for i in b:
        phys=i[1]
        chem=i[2]
        math=i[4]
        eng=i[5]
        bio=i[3]
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
    cursor.execute(f"select grade,percent,status from results where id={d}")
    a=cursor.fetchall()
    connection.commit()
    g1=a[0][0]
    p1=a[0][1]
    s1=a[0][2]
    label=Label(im1,text='Your Grade:',bg='light blue').grid(column=0)
    label=Label(im1,text=f'{g1}',bg='light blue').grid(column=1)
    
    label=Label(im1,text='Your Percentage:',bg='light blue').grid(column=0)
    label=Label(im1,text=f'{p1}',bg='light blue').grid(column=1)

    label=Label(im1,text='Status:',bg='light blue').grid(column=0)
    label=Label(im1,text=f'{s1}',bg='light blue').grid(column=1)


    cursor.execute(f"select state from ar where id= {d}")
    fetchexe=cursor.fetchall()
    connection.commit()
    label=Label(im1,text='Your State:',bg='light blue').grid(column=0)
    label=Label(im1,text=f'{fetchexe[0][0]}',bg='light blue').grid(column=1)



    cursor.execute("select state from ar;")
    stat=cursor.fetchall()
    un=[]
    connection.commit()
    for i in stat:
        if i[0].lower() not in un:
            un.append(i[0].lower())
    un1=[]
    for i in range(len(un)):
        axx=''
        for j in range(len(un[i])):
            if un[i][j].isspace():
                axx+='_'
            else:
                axx+=un[i][j]
        un1.append(axx)

    state=''
    for i in range(len(un)):
        if un[i] == fetchexe[0][0].lower():
            state=un1[i]
    print(state)
    cursor.execute(f"select rank1 from {state} where id={d}")
    stater=cursor.fetchall()
    print(stater[0][0])
    connection.commit()
    label=Label(im1,text='Your State Rank:',bg='light blue').grid(column=0)
    label=Label(im1,text=f'{stater[0][0]}',bg='light blue').grid(column=1)

    
    
    cursor.execute(f"select rank1 from air where id={d}")
    airr=cursor.fetchall()
    connection.commit()

    label=Label(im1,text='All India Rank:',bg='light blue').grid(column=0)
    label=Label(im1,text=f'{airr[0][0]}',bg='light blue').grid(column=1)




def Results_check():
    global d,y
    d=entry.get()
    y=entry1.get()
    cursor.execute(f"select id,passsword from ar where id={d}")
    
    a=cursor.fetchall()
    connection.commit()
    for i in a:
        id=i[0]
        passw=i[1]
    if y==passw:
        imm.destroy()
        Results_show()
    if y != passw:
        return messagebox.showerror(title='Error!',message='Enter correct Details.')
    

def again():
        if messagebox.askyesno(title='Continue',message='Do you want to Continue?'):
            main2()
def results():
    
    global entry,entry1,imm
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
    
    but=Button(imm,text='Enter.',command=Results_check,bg='white',fg='black').grid(row=2,column=1)

    imm.mainloop()




def Entry_Check(var,index,mode):
    ab=entry_idd.get()
    try:
        
        cursor.execute(f"select * from subjects where id='{ab}'")
        b=cursor.fetchall()
        connection.commit()
        for i in b:
            phys=i[1]
            chem=i[2]
            math=i[3]
            eng=i[4]
            bio=i[5]
            csc=i[6]
        if phys == 'no':
            entry_p.config(state=DISABLED)
        else:
            entry_p.config(state=NORMAL)
        if chem == 'no': 
            entry_c.config(state=DISABLED)
        else:
            entry_c.config(state=NORMAL)
        if bio == 'no':
            entry_b.config(state=DISABLED)
        else:
            entry_b.config(state=NORMAL)
        if csc == 'no':
            entry_cs.config(state=DISABLED)
        else:
            entry_cs.config(state=NORMAL)
        if math == 'no':
            entry_m.config(state=DISABLED)
        else:
            entry_m.config(state=NORMAL)
        if eng == 'no':
            entry_e.config(state=DISABLED) 
        else:
            entry_e.config(state=NORMAL)
    except:
        return messagebox.showerror('Incorrect ID','Enter Correct ID')

count=0

def Insert_results():
    global count,total
    count+=1
    total=0
    #try:  
    ab=entry_idd.get()
    query=f'insert into results values({ab},'
    if entry_p.get().isnumeric():
        p=float(entry_p.get())
        total+=p
        query+=f'{p},'
    else:
        query+='NULL,'
        p=0

    if entry_c.get().isnumeric():
        c=float(entry_c.get())
        total+=c
        query+=f'{c},'
    else:
        query+='NULL,'
        c=0

    if entry_b.get().isnumeric():
        b=float(entry_b.get())
        total+=b
        query+=f'{b},'
    else:
        query+='NULL,'
        b=0

    if entry_m.get().isnumeric():
        m=float(entry_m.get())
        total+=m
        query+=f'{m},'
    else:
        query+='NULL,'
        m=0

    if entry_e.get().isnumeric():
        e=float(entry_e.get())
        total+=e
        query+=f'{e},'
    else:
        query+='NULL,'
        e=0

    if entry_cs.get().isnumeric():
        cs=float(entry_cs.get())
        total+=cs
        query+=f'{cs},'
    else:
        query+='NULL,'
        cs=0
    
    Grade()
    if cs <= 100  and e <= 100 and m <= 100 and b <= 100 and c <= 100 and p <= 100:
        query+=f"{total},'{grade}',{percent},'{status}')"
        
        print(query)
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
        
    else:
        return messagebox.showerror('Incorrect Details','Please Again')
 


def Confirm():
    im.destroy()
    again()
def host():
    global entry_b,entry_c,entry_m,entry_p,entry_idd,entry_e,entry_cs,count,bvar,pvar,evar,csvar,cvar,mvar,Entry_var,im
    im=Tk()
    im.geometry("400x400")
    im.title("Host.")
    im.config(background="light blue")

    label0=Label(im,text="Please Enter the ID:",pady=-2,font=('Bold',9))
    label0.place(x=5,y=3)
    Entry_var=StringVar(im)
    Entry_var.trace_add('write', callback=Entry_Check)

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
    
    but=Button(im,text="Enter The results",command=Insert_results,font=('ariel',10,'bold'),fg='black',bg='white',
              activebackground='black',activeforeground='black')
    but.place(x=130,y=170)
    
    im.protocol("WM_DELETE_WINDOW",Confirm)
    im.mainloop()


count=0
id1=0

def insert_into_db():
    global count,id1
    count=0
    id1=float(entry_id.get())
    a=int(entry_id.get()) 
    b=entry_name.get()
    c=entry_password.get()
    f=entry_state.get()
    cursor.execute("INSERT INTO ar values({},'{}','{}','{}')".format(a,b,c,f))
    connection.commit()
    entry_id.config(state=DISABLED)
    entry_password.config(state=DISABLED)
    entry_name.config(state=DISABLED)   
    entry_state.config(state=DISABLED)
    count+=1




def Insert_Subjects():
    global cursor
    global p
    global c
    global b
    global csc
    global es
    global m
    idd=float(entry_id.get())
    p=c=b=m=csc=es='no'
    if x.get()=='yes':
        p='yes'
    if chem1.get() == 'yes':
        c='yes'
    if bio1.get() == 'yes':
        b='yes'
    if cs1.get() == 'yes':
        csc='yes    '
    if eng1.get() == 'yes':
        es='yes'
    if math1.get() == 'yes':
        m='yes'

    cursor.execute(f"insert into subjects values({idd},'{p}','{c}','{m}','{es}','{b}','{csc}')")
    connection.commit()



def Registration_Enter():
    if entry_id.get() == "" or entry_name.get() == "" or entry_password.get() == "":
 
            return messagebox.showinfo("Input Required", "Please enter the correct details.")
    else:
        
        cursor.execute("select id from ar;")
        a_=1
        out=cursor.fetchall()
        e=entry_id.get()
        connection.commit()
        for i in range (len(out)):
            if float(e) == out[i][0]:
                a_=0
                return messagebox.showinfo("Error", "Please provide a unique ID.")
        if a_ != 0:
            insert_into_db()
            Insert_Subjects()
            window.destroy()
            return messagebox.showinfo("Success!", "Success!")
            


def Registration_():
    global window,entry_state
    global button_insert
    global entry_name
    global entry_id
    global entry_password
    global x 
    global chem1
    global math1
    global eng1
    global bio1
    global cs1
    window = Tk()
    window.geometry("350x400")
    window.title("LIVE Show Password Entry")
    window.config(background="light blue")

    label=Label(window,text="ID:",font=('ariel',10,'bold'),fg='black',bg='light blue')
    label.place(x=5,y=8)
    entry_id = Entry(window, width=40)
    entry_id.place(x=30,y=35)


    label=Label(window,text="Name:",font=('ariel',10,'bold'),fg='black',bg='light blue')
    label.place(x=5,y=58)
    entry_name = Entry(window, width=40) 
    entry_name.place(x=30,y=85)


    label=Label(window,text="Password:",font=('ariel',10,'bold'),fg='black',bg='light blue')
    label.place(x=5,y=108)
    entry_password =  Entry(window, width=40,show='*')
    entry_password.place(x=30,y=135)

    label=Label(window,text="State:",font=('ariel',10,'bold'),fg='black',bg='light blue')
    label.place(x=5,y=158)
    entry_state =Entry(window,width=40)
    entry_state.place(x=30,y=185)   

    button_insert =  Button(window, text="Enter.", command=Registration_Enter,bg='white')
    button_insert.place(x=130,y=350)
    
    a=Label(window,text='Subjects:',font=('ariel',10,'bold'),fg='black',bg='light blue')
    a.place(x=5,y=210)


    x=StringVar(window,'no')
    chem1=StringVar(window,'no')
    math1=StringVar(window,'no')
    a=Checkbutton(window,text='Physics',variable=x,onvalue='yes',offvalue='no',font=('ariel',10,'bold'),fg='black',bg='light blue',
              activebackground='light blue',activeforeground='black',)
    a.place(x=30,y=237)

    chem=Checkbutton(window,text='Chemistry',variable=chem1,onvalue='yes',offvalue='no',font=('ariel',10,'bold'),
                     fg='black',bg='light blue',
                     activebackground='light blue',
                     activeforeground='black',)
    chem.place(x=110,y=237)

    math=Checkbutton(window,text='Maths',variable=math1,onvalue='yes',offvalue='no',font=('ariel',10,'bold'),
                     fg='black',bg='light blue',
                     activebackground='light blue',
                     activeforeground='black',)
    math.place(x=206,y=237)
    
    eng1=StringVar(window,'no')
    eng=Checkbutton(window,text='English',variable=eng1,onvalue='yes',offvalue='no',font=('ariel',10,'bold'),
                     fg='black',bg='light blue',
                     activebackground='light blue',
                     activeforeground='black',)
    eng.place(x=30,y=270)

    bio1=StringVar(window,'no')
    bio=Checkbutton(window,text='Biology',variable=bio1,onvalue='yes',offvalue='no',font=('ariel',10,'bold'),
                     fg='black',bg='light blue',
                     activebackground='light blue',
                     activeforeground='black',)
    bio.place(x=110,y=270)
    
    cs1=StringVar(window,'no')
    cs=Checkbutton(window,text='Computer Science',variable=cs1,onvalue='yes',offvalue='no',font=('ariel',10,'bold'),
                     fg='black',bg='light blue',
                     activebackground='light blue',
                     activeforeground='black',)
    cs.place(x=191,y=270)    
    window.mainloop()


def Grade():
    global grade,percent,status
    aG=int(entry_idd.get())
    grade=''
    connection.commit()
    kb=total
    cursor.execute(f"select * from subjects where id='{aG}'")    
    b=cursor.fetchall()
    connection.commit()
    totM=0
    for i in b:
        phys=i[1]
        chem=i[2]
        math=i[4]
        eng=i[5]
        bio=i[3]
        csc=i[6]
        print(phys,chem,math,eng,bio,csc)
    if phys == 'yes':
        totM+=100
        print('P')
    if csc == 'yes':
        totM+=100
        print('cs')
    if chem == 'yes': 
        totM+=100
        print('C')
    if bio == 'yes':
        totM+=100
        print('B')
        print(csc)
    if math == 'yes':
        totM+=100
        print('M')
    if eng == 'yes':
        totM+=100
        print('E')

    print(totM)
    percent=(kb/totM)*100
    status=''

    if percent >= 0 and percent <= 50:
        grade='F'
    elif percent >= 51 and percent <= 60:
        grade='D'
    elif percent >= 61 and percent <= 80:
        grade='C'
    elif percent >= 81 and percent <= 90:
        grade='B'
    elif percent >= 91 and percent <= 95:
        grade='A'
    elif percent >= 96 and percent <= 100:
        grade='A+'
    if  percent >= 50:
        status='pass'
    else:
        status='fail'
    print(grade,percent,status)





def e():

    pa=px.get()
    ca=cx.get()
    ea=ex.get()
    ma=mx.get()
    ba=bx.get()
    csa=csx.get()
    dates=[]

    win.destroy()
    return messagebox.showinfo("Done", "Registration Done!")
    cursor.execute(f"insert into subjects values({idd},'{p}','{c}','{m}','{e}','{b}','{csc}')")

    

def allocation():
    global px
    global cx
    global ex
    global mx
    global csx,win
    global bx
    global pradio1
    global pradio2
    global pradio3
    global cradio1
    global cradio2
    global cradio3
    global eradio1
    global eradio2
    global eradio3
    global mradio1
    global mradio2
    global mradio3
    global bradio1
    global bradio2
    global bradio3
    global csradio1
    global csradio2
    global csradio3,id1

    win=Tk()
    win.geometry('600x400')
    win.config(background='light blue')


    
    cursor.execute("select date1,date2,date3 from dates where subjects='physics'")
    fet=cursor.fetchall()
    phys=[]
    for i in fet:
        phys+=[i[0],i[1],i[2]]
    px=IntVar()
    l=Label(win,text="Physics:",font=('ariel',10,'bold'),fg='black',bg='light blue').grid(row=0,column=1)
    pradio1=Radiobutton(win,text=phys[0],variable=px,value=0,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    pradio1.grid(row=0,column=2,ipadx=5)
    pradio2=Radiobutton(win,text=phys[1],variable=px,value=1,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    pradio2.grid(row=0,column=1+2,ipadx=5)
    pradio3=Radiobutton(win,text=phys[2],variable=px,value=2,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    pradio3.grid(row=0,column=2+2,ipadx=5)    
    a=px.get()

    Entry_var=StringVar(win)
    Entry_var.trace_add('write', callback=e)

    #entry_id=Entry(win,width=25,textvariable=Entry_var)
    #entry_id.place(x=120,y=3)

    
    cursor.execute("select date1,date2,date3 from dates where subjects='chemistry'")
    fet=cursor.fetchall()
    che=[]
    for i in fet:
        che+=[i[0],i[1],i[2]]
    cx=IntVar()
    l=Label(win,text="Chemistry",font=('ariel',10,'bold'),fg='black',bg='light blue').grid(row=1,column=1)
    cradio1=Radiobutton(win,text=che[0],variable=cx,value=0,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    cradio1.grid(row=1,column=0+2,ipadx=5)
    cradio2=Radiobutton(win,text=che[1],variable=cx,value=1,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    cradio2.grid(row=1,column=1+2,ipadx=5)
    cradio3=Radiobutton(win,text=che[2],variable=cx,value=2,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    cradio3.grid(row=1,column=2+2,ipadx=5)


    cursor.execute("select date1,date2,date3 from dates where subjects='English'")
    fet=cursor.fetchall()
    eng=[]
    for i in fet:
        eng+=[i[0],i[1],i[2]]
    ex=IntVar()
    l=Label(win,text="English",font=('ariel',10,'bold'),fg='black',bg='light blue').grid(row=2,column=1)
    eradio1=Radiobutton(win,text=eng[0],variable=ex,value=0,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    eradio1.grid(row=2,column=0+2,ipadx=5)
    eradio2=Radiobutton(win,text=eng[1],variable=ex,value=1,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    eradio2.grid(row=2,column=1+2,ipadx=5)
    eradio3=Radiobutton(win,text=eng[2],variable=ex,value=2,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    eradio3.grid(row=2,column=2+2,ipadx=5)



    cursor.execute("select date1,date2,date3 from dates where subjects='Maths'")
    fet=cursor.fetchall()
    mat=[]
    for i in fet:
        mat+=[i[0],i[1],i[2]]
    mx=IntVar()
    l=Label(win,text="Maths:",font=('ariel',10,'bold'),fg='black',bg='light blue').grid(row=3,column=1,ipadx=5)
    mradio1=Radiobutton(win,text=mat[0],variable=mx,value=0,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    mradio1.grid(row=3,column=0+2,ipadx=5)
    mradio2=Radiobutton(win,text=mat[1],variable=mx,value=1,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    mradio2.grid(row=3,column=1+2,ipadx=5)
    mradio3=Radiobutton(win,text=mat[2],variable=mx,value=2,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    mradio3.grid(row=3,column=2+2,ipadx=5)


    cursor.execute("select date1,date2,date3 from dates where subjects='Computers'")
    fet=cursor.fetchall()
    csc=[]
    for i in fet:
        csc+=[i[0],i[1],i[2]]
    csx=IntVar()
    l=Label(win,text="Computer:",font=('ariel',10,'bold'),fg='black',bg='light blue').grid(row=4,column=1,ipadx=5)
    csradio1=Radiobutton(win,text=csc[0],variable=csx,value=0,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    csradio1.grid(row=4,column=0+2,ipadx=5)
    csradio2=Radiobutton(win,text=csc[1],variable=csx,value=1,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    csradio2.grid(row=4,column=1+2,ipadx=5)
    csradio3=Radiobutton(win,text=csc[2],variable=csx,value=2,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    csradio3.grid(row=4,column=2+2,ipadx=5)


    cursor.execute("select date1,date2,date3 from dates where subjects='biology'")
    fet=cursor.fetchall()
    bio=[]
    for i in fet:
        bio+=[i[0],i[1],i[2]]
    bx=IntVar()
    l=Label(win,text="Biology:",font=('ariel',10,'bold'),fg='black',bg='light blue').grid(row=5,column=1,ipadx=5)
    bradio1=Radiobutton(win,text=bio[0],variable=bx,value=0,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    bradio1.grid(row=5,column=0+2,ipadx=5)
    bradio2=Radiobutton(win,text=bio[1],variable=bx,value=1,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    bradio2.grid(row=5,column=1+2,ipadx=5)
    bradio3=Radiobutton(win,text=bio[2],variable=bx,value=2,font=("Ariel",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black')
    bradio3.grid(row=5,column=2+2,ipadx=5)
    
    l=[[pradio1,pradio2,pradio3],[cradio1,cradio2,cradio3],[mradio1,mradio2,mradio3],[eradio1,eradio2,eradio3],[bradio1,bradio2,bradio3],[csradio1,csradio2,csradio3]]

    cursor.execute(f"select * from subjects where id={id1}")
    k=cursor.fetchall()
    connection.commit()
    for i in range(1,len(k[0])):
        if k[0][i] =='no':
            for j in l[i-1]:
                j['state']=DISABLED

    
    button_insert =  Button(win, text="Done?", command=e)
    button_insert.grid(row=14,column=3)
    win.mainloop()



def Check_what():
    global num
    get=qx.get()
    main1.destroy()
    if get == 0:
        Registration_()
        allocation()
        again()
    if get == 1:
        Host_check()
        
    if get == 2:
        results()
        again()
    if get == 3:
        num=1
        f=open('Initiate.txt','a+')
        f.seek(0)
        read1=f.read()
        if read1.lower() != 'initiated':
            f.write('initiated')
            initiate()
            again()
            return messagebox.showinfo(title='Success',message='Initiated!')
        else:
            again()
            return messagebox.showerror(title='Error!',message='Already Initiated')


        

def main2():
    global qx,main1
    main1=Tk()
    main1.geometry('200x250')
    main1.config(background='light blue')
    qx=IntVar()
    label=Label(main1,text='Olympiad Exam:',font=('Bold'),bg='Light blue').place(x=0,y=0)

    reg=Radiobutton(main1,text='Registration.',variable=qx,value=0,font=("bold",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black',indicatoron=0)
    reg.place(x=30,y=50,anchor=W)
    host=Radiobutton(main1,text='Host.',variable=qx,value=1,font=("bold",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black',indicatoron=0)
    host.place(x=30,y=90,anchor=W)
    result=Radiobutton(main1,text='Results.',variable=qx,value=2,font=("bold",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black',indicatoron=0)
    result.place(x=30,y=130,anchor=W)
    

    ini=Radiobutton(main1,text='Initiate Results.',variable=qx,value=3,font=("bold",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black',indicatoron=0)
    ini.place(x=30,y=170,anchor=W)

    button=Button(main1,text='Enter.',command=Check_what,font=("bold",10),fg='black',bg='light blue'
                           ,activebackground='light blue',activeforeground='black',).place(x=50,y=190)

    
    main1.mainloop()
main2()
