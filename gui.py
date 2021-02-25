import tkinter as tk
from tkinter import filedialog,messagebox
import send as wsend
import sys,os
import receive as wreceive
MONOSPACES=("Consolas",11)
class main(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.frame_index=0
        
        tk.Tk.__init__(self,*args,**kwargs)
        self.geometry("700x500")
        #self.protocol("WM_DELETE_WINDOW",self.close)
        #logo = tk.PhotoImage(file=" Users/Clay/Clay/Python/KRG/Bible/src/biblelogo.png")
        
        #mylist=tk.Listbox(self,yscrollcommand=scrollbar.set)
        #mylist.pack(side=tk.RIGHT,fill=tk.BOTH)
        #scrollbar.config(command=mylist.yview)
        #self.iconphoto(False,logo)
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)  
        self.menuBar = tk.Menu(self)
        self.pageMenu = tk.Menu(self.menuBar,tearoff=0)
        self.pageMenu.add_command(label="Send",command=self.send)
        self.pageMenu.add_separator()
        #self.pageMenu.add_separator()
        self.pageMenu.add_command(label = "Receive",command=self.receive)
        
        self.menuBar.add_cascade(label="Page",menu=self.pageMenu)
        self.config(menu=self.menuBar)
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1)
        self.frames={}
        #self.report_callback_exception=self.errorhandle
        self.pages = (Send,Receive)
        #homeButton = ttk.Button(self,text="Home")
        #homeButton.place(anchor=tk.NE)
        for F in self.pages:
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
       
        self.show_frame(self.pages[0])
    def show_frame(self,frame):
        self.frames[frame].tkraise()
        self.title("WTransfer - "+self.frames[frame].titlestr)
    def send(self):
        self.show_frame(self.pages[0])
    def receive(self):
        self.show_frame(self.pages[1])

class Send(tk.Frame):
    titlestr="Send"
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.folder=tk.StringVar()
        self.folder.set("Blank")
        self.isfile=tk.IntVar()
        tk.Button(self,text="Path",command=self.choose).grid(row=0,column=0,padx=5,pady=5)
        tk.Checkbutton(self,text="Single File",variable=self.isfile).grid(row=0,column=1,padx=5,pady=5)
        tk.Button(self,text="Send",command=self.send).grid(row=1,column=1,padx=5,pady=5)
        self.table = tk.Listbox(self,width=70,height=10,font=MONOSPACES,exportselection=False)
        self.table.grid(row=2,column=1,columnspan=4,padx=5,pady=5)
    def send(self):
        self.table.delete(0,tk.END)
        if self.folder.get()=="Blank":
            messagebox.showwarning("Error","No File Selected...")
            return
        #temp = sys.stdout
        #sys.stdout=self
        
        if os.path.isdir(self.folder.get()):
            wsend.transfer(self.folder.get().replace('\\','/'),self.folder.get().replace('\\','/'),log=self.write)
        else:
            wsend.transfer(self.folder.get().replace('\\','/'),os.path.dirname(self.folder.get()).replace('\\','/'),log=self.write)
        #sys.stdout=temp
    def choose(self):
        if self.isfile.get()==1:
            file = filedialog.askopenfilename()
        else:
            file=filedialog.askdirectory()
        self.folder.set(file)
        #print(file)
    def write(self,text):
        self.table.insert(tk.END,text)
    def flush(self):
        pass
class Receive(tk.Frame):
    titlestr="Receive"
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.folder=tk.StringVar()
        self.folder.set("Blank")
        self.ip=tk.StringVar()
        #self.ip.set('Blank')
        tk.Button(self,text="Path",command=self.choose).grid(row=0,column=0,padx=5,pady=5)
        tk.Label(self,text="IP: ").grid(row=1,column=0,padx=5,pady=5)
        tk.Entry(self,textvariable=self.ip).grid(row=1,column=2,padx=5,pady=5)
        tk.Button(self,text="Receive",command=self.receive).grid(row=2,column=0,padx=5,pady=5)
        self.table = tk.Listbox(self,width=70,height=10,font=MONOSPACES,exportselection=False)
        self.table.grid(row=3,column=1,columnspan=4,padx=5,pady=5)
    def receive(self):
        self.table.delete(0,tk.END)
        if self.folder.get()=="Blank":
            messagebox.showwarning("Error","No File Selected...")
            return
        if not self.ip.get():
            messagebox.showwarning("Error","No File Selected...")
            return
        #temp = sys.stdout
        #sys.stdout=self
        
        wreceive.receive(self.folder.get().replace("\\",'/'),ip=self.ip.get(),log=self.write)
        #sys.stdout=temp
    def choose(self):

            file=filedialog.askdirectory()
            self.folder.set(file)
            #print(file)
    def write(self,text):
        self.table.insert(tk.END,text)
    def flush(self):
        pass
if __name__ == "__main__":
    m=main()
    m.mainloop()