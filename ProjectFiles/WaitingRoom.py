from tkinter import *
import tkinter.messagebox
import json
from StringData import *
from jahakWork import *
class WaitingRoom(Frame):
    def  __init__(self,master,resp):
        super().__init__(master)
        self.__tk = master
        self.__cpdFrame=None
        self.__scene = None
        if (not( "user_name" in resp)):
            resp["user_name"] = []
        if ( not ("computer_count" in resp)):
            resp["computer_count"] = 0
        if(not ('isRightDir' in resp)):
            resp['isRightDir']=True
        self.__totalPlayerCount = 0
        self.__firstAccess = True
        self.__resp = {"user_name":[],"isRightDir":True}
        
        for previousName in resp['user_name']:
            self.__resp['user_name'].append(previousName)
        self.create_wdigets(self.__resp)
    def setNextScene(self,sc):
        self.__scene = sc
    def showDialogHadMinPlayer(self):
        tkinter.messagebox.showinfo(StringData.getDlgTitle_minPlayer(),StringData.getDlgContent_minPlayer())
    @property
    def result(self):
        return self.__resp
    def scene(self):
        return self.setNextScene
    def packList(self):
        size = self.listbox_playerlist.size()
        if('user_name' in self.__resp):
            self.__resp['user_name'].clear()
        else:
            self.__resp['user_name']=[]
        for i in range(size):
            self.__resp["user_name"].append(self.listbox_playerlist.get(i))
        return self.__resp        
    def getChoosePlayDiection_Frame(self,names,dirRespCarrier,createMode = False,master=None):
        if(createMode):
            self.__cpdFrame = ChoosePlayDirection(self,names,dirRespCarrier)
            self.__cpdFrame.setNextScene(self.nextScene)
        
        return self.__cpdFrame
        
    
    def setNextScene(self,sc):
        self.__scene=sc
    def nextScene(self):
        (self.__scene)(self.__tk,self.result)
    
    
    
    def doPlay(self):
        size = self.listbox_playerlist.size()
        if(size>1):
            self.__resp = self.packList()
            for chd in self.winfo_children():
                chd.destroy()
                del chd
            
            cpd = self.getChoosePlayDiection_Frame(self.__resp['user_name'],self.__resp,True,self) #ChoosePlayDirection(self,self.__resp['user_name'])
            
            
            cpd.pack(expand=True,fill=BOTH)
        else:
            self.showDialogHadMinPlayer()
        #self.destroy()
    def create_wdigets(self,resp=None):
        self.__lb1 = Label(self,text=StringData.getLableTitlePlayerCountHeader())
        self.__lb1.grid(row=0,column=0)
        self.label_totalPlayerCount= Label(self,justify=LEFT,text=str(self.__totalPlayerCount)+"명")
        self.label_totalPlayerCount.grid(row=0,column=1)
        self.__btn1 = Button(self,text=StringData.getBtnTxtPlayerDel(),command=self.delPlayer)
        self.__btn1.grid(row=0,column=3)
        self.listbox_playerlist = Listbox(self,selectmode="SINGLE",height=8,width=35)
        self.listbox_playerlist.grid(row=1,column=0,columnspan=4)
        self.entry_inputnewplayerName = Entry(self,width=20,justify=LEFT)
        self.entry_inputnewplayerName.grid(row=2,column=0,columnspan=2)
        self.__btn2 = Button(self,text=StringData.getBtnTxtPlayerAdd(),command=self.addPlayer)
        self.__btn2.grid(row=2,column=3)
        self.__btn3 = Button(self,text=StringData.getBtnTxtDoPlay(),command=self.doPlay)
        self.__btn3.grid(row=3,column=4)
        #self.__ckb_enable_computer = Checkbutton(master,text="컴퓨터 사용",command=self.doSyncCkbEnableComputer).
        if(resp!=None and type(resp)==list and self.__firstAccess == True):
            self.__firstAccess = False
            for prevName in resp:
                if(prevName != ''  ):
                    self.listbox_playerlist.insert(self.listbox_playerlist.size(),prevName)
                
            self.label_totalPlayerCount['text'] = str(self.listbox_playerlist.size())+StringData.getPeopleCountUnit()

        self.entry_inputnewplayerName.bind("<Return>",self.addPlayer)
        self.pack(padx=20,pady=20)

    def delPlayer(self):
        idx = self.listbox_playerlist.curselection()
        if(idx != ()):
            self.listbox_playerlist.delete(idx)
            self.label_totalPlayerCount['text'] = str(self.listbox_playerlist.size())+StringData.getPeopleCountUnit()
            
    def addPlayer(self,event=None):
        pname = self.entry_inputnewplayerName.get()
        if(pname == '' or pname == []):
            tkinter.messagebox.showinfo(StringData.getErrorText(),StringData.getUserNameEmptyErrorMsgBoxContent())
        else:
            size = self.listbox_playerlist.size()
            hasSamePlayer = False
            for i in range(size):
                if(pname == self.listbox_playerlist.get(i)):
                    hasSamePlayer = True
                    break
            if(hasSamePlayer):
                tkinter.messagebox.showinfo(StringData.getDlgTitle_existRegisteredPlayer(),StringData.getDlgContent_existRegisteredPlayer())
            elif(size>7):
                tkinter.messagebox.showinfo(StringData.getDlgTitle_maxPlayer(),StringData.getDlgContent_maxPlayer())
            else:
                self.listbox_playerlist.insert(self.listbox_playerlist.size(),pname)
                self.label_totalPlayerCount['text'] = str(self.listbox_playerlist.size())+StringData.getPeopleCountUnit()
            
        self.entry_inputnewplayerName.delete(0,END)
