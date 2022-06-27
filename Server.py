from tkinter import *
from socket import *
class MyApp:
    def __init__(self,myParent):
        global L
        L=[]
        self.p=myParent
        self.f1=Frame(myParent,bg="purple")
        self.f1.pack(fill='x')
        self.w=Label(self.f1,text='Server Display:           :::',bg="purple",font="Consolas 14", fg='white')
        self.w.pack(side='left')
        self.f2=Frame(myParent,bg="#aeacaf")
        self.f2.pack()
        self.f3=Frame(myParent, bg='purple')
        self.f3.pack(fill=X, anchor='s',side='bottom')
        self.entry=Entry(self.f3,font="Consolas 11", bg='white')
        self.entry.pack(side='left',pady=10,padx=15)
        self.textmsg=StringVar()
        self.textmsg.set('connected to server')
        self.k=Label(self.f2, textvariable=self.textmsg ,bg='#d651ff',font="Consolas 14", fg='white')
        self.k.pack()
        self.but=Button(self.f3,text='SEND', font='Consolas 15',bg='grey', fg='purple',padx=5, pady=3, command=self.connect)
        self.but.pack(side='right')
        self.sendpush() 
        
    def sendpush(self):
        global serverPort
        serverPort=54742
        global serverSocket
        serverSocket=socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', serverPort))
        serverSocket.listen(1)
        global connectionSocket
        global addr
        connectionSocket, addr=serverSocket.accept()
        self.getmsg()
        
    def connect(self):
        globals()
        reprlsentence=self.entry.get()
        L.append('You: '+reprlsentence)
        connectionSocket.send(reprlsentence.encode('utf-8'))
        connectionSocket.close()
        self.sendpush()      

    def getmsg(self):
        globals()
        sentence=connectionSocket.recv(4096)
        sentence=sentence.decode('utf-8')
        L.append('Client: '+sentence)
        self.entry.delete(0,'end')
        self.textmsg.set('\n'.join(map(str,L)))

root=Tk()
root.geometry("300x455")
root.resizable(width=False, height=False)
root.configure(background='#aeacaf')
root.title('Regted')
myapp=MyApp(root)
root.mainloop()
