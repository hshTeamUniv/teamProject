from tkinter import *
import time
import random 
class ChoosePlayDirection(Frame):
    def __init__(self,master,playerNames,dirRespCarrier=None):
        super().__init__(master)
        self.__scene = None
        self.pack(padx=10, pady=10)
        self.people = playerNames[:]
        self.button1_clicks = 0
        self.button2_clicks = 0
        self.peopleCount = len(self.people)
 
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        self.grid(row=0,column=0)
        self.pack(expand=True,fill=BOTH)
        self.create_widgets(dirRespCarrier)
        
    
    def setNextScene(self,sc):
        self.__scene = sc
    def create_widgets(self,resp):
        initName = "none"
        if(len(self.people)!=0):
            initName = self.people[0]
            
        self.display = Label(self, text="'"+initName+"'순서방향을 정해주십시오")
        self.display.grid(row=0, column=1)
        Label(self, text=' ').grid(row=1,column=1)
        self.button1 = Button(self)
        self.button1["text"] = "순방향"
        self.button1["command"] = lambda: self.update_count(resp,1-1)
        self.button1.grid(row=2, column=0)
        self.button2 = Button(self)
        self.button2['text'] = '역방향'
        self.button2['command'] = lambda: self.update_count(resp,2-1)
        self.button2.grid(row=2, column=2)
    def nextPlayer(self,resp):
        if(self.people==[] or len(self.people)==1):
            self.end_sequence(resp)
        else:
            self.people = self.people[1:]
            txt = self.display['text']
            after = txt[txt.index("'",1):]
            self.display['text'] = "'"+self.people[0]+after

    
    def update_count(self,resp,which):
        if(not which):
            self.button1_clicks += 1
        else:
            self.button2_clicks += 1
        self.nextPlayer(resp)
    def end_sequence(self,resp):
        
        end_button = self.button1_clicks + self.button2_clicks
        isRightDir = True
        key_isRightDir = "isRightDir"
        if end_button == self.peopleCount : 
            if self.button1_clicks > self.button2_clicks :
                Label( text='순방향으로 정하셨습니다').grid(row=3, column=1)
            elif self.button1_clicks < self.button2_clicks : 
                Label( text='역방향으로 정하셨습니다').grid(row=3, column=1)
                isRightDir=False
            else : 
                la = [1,2]
                random.shuffle(la)
                if la[0] == 1 : 
                    Label( text='순방향으로 정하셨습니다').grid(row=3, column=1)
                    
                else : 
                    Label( text='역방향으로 정하셨습니다').grid(row=3, column=1)
                    isRightDir=False
        resp[key_isRightDir] = isRightDir
        (self.__scene)()
        

