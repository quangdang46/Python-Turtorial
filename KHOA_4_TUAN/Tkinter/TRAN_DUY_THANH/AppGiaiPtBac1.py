from tkinter import*
root=Tk()
def GiaiPt():
    x=int(a.get())
    y=int(b.get())
    if x==0 and y==0:
        kq1.set("Vo so nghiem")
    elif x==0 and y!=0:
        kq1.set("Vo nghiem")
    else:
        kq1.set(str(-y/x))
def Tiep():
    a.set("")
    b.set("")
    kq1.set("")
a=StringVar()
b=StringVar()
kq1=StringVar()
root.title("PTB1")
root.geometry('300x200')
root.resizable(1,1)
lbl=Label(root,text='PHUONG TRINH BAC 1',fg='red',font=('Arian 15'))
lbl.grid(row=0,columnspan=3)
hesoa=Label(root,text='He so a:')
hesoa.grid(row=1,column=0)
hesob=Label(root,text='He so b:')
hesob.grid(row=2,column=0)
ent1=Entry(root,width=30,textvariable=a)
ent2=Entry(root,width=30,textvariable=b)
ent1.grid(row=1,column=1)
ent2.grid(row=2,column=1)
MyButton=Frame(root)
Button(MyButton,text="Giai",command=GiaiPt).pack(side="left")
Button(MyButton,text="Tiep",command=Tiep).pack(side="left")
Button(MyButton,text="Thoat",command=MyButton.quit).pack(side="left")
MyButton.grid(row=3,columnspan=2)
ketqua=Label(root,text='Ket qua: ')
ketqua.grid(row=4,column=0)
kq=Entry(root,width=30,textvariable=kq1)
kq.grid(row=4,column=1)
root.mainloop()