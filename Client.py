from tkinter import *
from socket import *
class MyApp:
    def __init__(self,myParent):
        global L
        L=[]
        self.p=myParent
        self.f1=Frame(myParent,bg="purple")          
        self.f1.pack(fill='x')                      
        self.w=Label(self.f1,text='Client Display:           :::',bg="purple",font="Consolas 14", fg='white')
        self.w.pack(side='left')
        self.f2=Frame(myParent,bg='#aeacaf' )
        self.f2.pack(fill='both')
        self.f3=Frame(myParent, bg='purple')
        self.f3.pack(side='bottom',fill=BOTH)
        self.entry=Entry(self.f3,font="Consolas 11", bg='white')
        self.entry.pack(side='left',pady=10,padx=15)
        self.textmsg=StringVar()                    
        self.textmsg.set('connected to server')
        self.k=Label(self.f2, textvariable=self.textmsg ,bg="#d651ff",font="Consolas 14", fg='white')
        self.k.pack()
        self.but=Button(self.f3,text='SEND', font='Consolas 15', bg='grey', fg='purple',padx=5, pady=3, command=self.sendpush )
        self.but.pack(side='right')

    def get(self):
        global serverName
        serverName='192.168.2.2'
        global serverPort
        serverPort=60043
        global clientSocket
        clientSocket=socket(AF_INET,SOCK_STREAM)                
        clientSocket.connect((serverName,serverPort))           
        
    def sendpush(self):
        self.get()
        globals()
        global sentence
        sentence = self.entry.get()
        clientSocket.send(sentence.encode('utf-8'))
        L.append('You: '+sentence)
        self.entry.delete(0,'end')
        self.getmsg()

    def getmsg(self):
        globals()
        modifiedSentence=clientSocket.recv(4096)
        modifiedSentence=modifiedSentence.decode('utf-8')
        L.append('Server: '+modifiedSentence)
        self.textmsg.set('\n'.join(map(str, L)))
        clientSocket.close()
         
root=Tk()
root.geometry("300x455")
root.resizable(width=False, height=False)
root.configure(background='#aeacaf')
root.title('Regted')
myapp=MyApp(root)
root.mainloop()
