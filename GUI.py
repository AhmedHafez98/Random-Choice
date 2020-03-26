from tkinter import Tk,StringVar,IntVar,CENTER,RIDGE
import tkinter.ttk as ttk
from tkinter import messagebox

class Main():

    def __init__(self,Title):

        self.Title=Title
        self.root=Tk()
        self.root.title(Title)
        self.root.geometry('200x100')
        self.root.resizable(False,False)
        ttk.Label(self.root,text='Welcome to Random Tag').grid(row=0,column=0,columnspan=2,sticky='snew',padx=10,pady=10)
        ttk.Button(self.root,text='Edit',command=self.edit).grid(row=1,column=0,sticky='snew',padx=10,pady=10)
        ttk.Button(self.root,text='Get',command=self.get).grid(row=1,column=1,sticky='snew',padx=10,pady=10)
        from DB import sq
        sq().create_table()
        self.root.mainloop()
    def edit(self):
        self.root.destroy()
        EDIT('Edit Tags')
        self.__init__(self.Title)
    def get(self):
        from DB import sq
        id = sq().get()
        if len(id)==0:
            messagebox.showerror('GET Error','Please Enter Tags')
            self.edit()
            return
        self.root.destroy()
        GET('GET Tag')
        self.__init__(self.Title)
class EDIT:
    def __init__(self, Title):
        self.currow=2
        from DB import sq
        self.lst = sq().show()
        self.root = Tk()
        self.root.title(Title)
        self.dat=[]
        self.inpadd=(StringVar(),IntVar())
        self.inpadd[1].set(1)
        E=ttk.Entry(self.root,textvariable=self.inpadd[0],justify=CENTER)
        E.grid(row=0, column=0, sticky='snew',padx=10,pady=10)
        E.focus()
        ttk.Spinbox(self.root, textvariable=self.inpadd[1], from_=1, to=100,width=5).grid(row=0, column=1, sticky='snew',padx=10,pady=10)
        ttk.Button(self.root,text='Add',command=self.Add).grid(row=0, column=2,columnspan=2, sticky='snew',padx=10,pady=10)
        ttk.Button(self.root,text='Delete',command=self.Del).grid(row=1, column=1, sticky='snew',padx=10,pady=10)
        ttk.Button(self.root,text='Update',command=self.Upd).grid(row=1, column=2, sticky='snew',padx=10,pady=10)
        ttk.Label(self.root,text='Tag Name',relief=RIDGE).grid(row=1, column=0, sticky='snew',padx=10,pady=10)
        for tg in self.lst:
            self.addtag(tg[0],tg[1])
        self.root.mainloop()
        # self.root.bind('<Return>',self.Add())
    def addtag(self,name,task):
        l=ttk.Label(self.root,text=name)
        spn=[0,0]
        spn[0]=IntVar()
        spn[0].set(task)
        spn[1]=ttk.Spinbox(self.root, textvariable=spn[0], from_=1, to=100,width=5)
        chk=[0,0]
        chk[0]=IntVar()
        chk[1]=ttk.Checkbutton(self.root,variable=chk[0],onvalue=1,offvalue=0)
        self.dat.append((l,chk,spn))
        ln=len(self.dat)-1
        self.dat[ln][0].grid(row=self.currow, column=0, sticky='snw',padx=10,pady=10)
        self.dat[ln][1][1].grid(row=self.currow, column=1, sticky='snew',padx=10,pady=10)#chk
        self.dat[ln][2][1].grid(row=self.currow, column=2, sticky='snew',padx=10,pady=10)           #spn
        self.currow+=1
    def Add(self):
        from DB import sq
        name=self.inpadd[0].get()
        task=self.inpadd[1].get()
        if name=='':
            messagebox.showerror('Add Error','Please Enter Tag Name')
        else :
            x=sq().add(name,task)
            if x != None:
                messagebox.showerror('Add Error', str(x))
                return
            self.addtag(name,task)
            self.inpadd[0].set('')
            self.inpadd[1].set(1)
    def Del(self):
        from DB import sq
        delid=[]
        for id,tg in enumerate(self.dat):
            name = tg[0]['text']
            if tg[1][0].get():
              sq().Del(name)
              delid.append(id)
        delid.sort(reverse=True)
        for id in delid:
            self.dat[id][0].destroy()
            self.dat[id][1][1].destroy()
            self.dat[id][2][1].destroy()
            del self.dat[id]
    def Upd(self):
        from DB import sq
        for tg in self.dat:
            name=tg[0]['text']
            task=tg[2][0].get()
            sq().Update(name,task)
class GET:
    def __init__(self, Title):
        from DB import sq
        id=sq().get()
        self.root = Tk()
        self.root.title(Title)
        self.root.resizable(False,False)
        s=' Tag is {} and Has {} tasks'.format(id[0],id[1])
        ttk.Label(self.root, text=s).grid(row=0, column=0, columnspan=4, sticky='snew',padx=10,pady=10)
        ttk.Button(self.root, text='Done', command=lambda :self.done(id)).grid(row=1, column=3, sticky='snew',padx=10,pady=10)
        self.root.mainloop()
    def done(self,id):
        from DB import sq
        if id[1]==1:
            sq().Del(id[0])
        else:
            sq().Update(id[0],id[1]-1)
        self.root.destroy()