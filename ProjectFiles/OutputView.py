from tkinter import *
import threading
from Deck import *
#from Util import *
from Player import *
#from Util import *
import tkinter.messagebox
import hoonWork
from test.test_dynamicclassattribute import PropertyDel
from CardButton import *
from ValueContainedCheckButton import *
class OutputView(Frame):

    @staticmethod
    def configKeyList():
        return ["nextTurnCmd","popCardsCmd","deckShuffleCmd","deckSortCmd","initPlayerCardFrames","initPlayerPublicCardFrames","initPlayerNames","initWidgetRefreshView"]
    def __init__(self,master):
        super().__init__(master)
        self.__cFrame = None
        self.__cPublicFrame=None
        self.__currentP = None
        self.__afterP = None
        configKeyList = OutputView.configKeyList()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.porderlv=None
        self.__topframe=None
        self.pranklv=None
        self.__configs={key:None for key in configKeyList}
        self.frame5container=None
        self.frame2container=None
        self.pack(fill=BOTH,padx=10,pady=10,expand=True)
    def setManipulatedPlayers(self,p1,p2):
        self.__currentP = p1
        self.__afterP = p2
        
    def getPublicCardFrame(self,player=None):
        if(self.__cPublicFrame != None):
            lst = self.__cPublicFrame.winfo_children()
            for i in lst:
                i.destroy()
        if(self.__cPublicFrame==None):
            
            self.__cPublicFrame = Frame(self.frame2)
            try:
                self.__cPublicFrame.pack(fill=X,expand=TRUE)
            except:
                pass
            self.__cPublicFrame.grid(row=0,column=0,stick="news")
        if(player!=None and type(player)==Player):
            self.__afterP=player
        if(self.__afterP!=None):
            phand = self.__afterP.getHand()
            for i in range(len(phand)):
            
                btn =CardButton(self.__cPublicFrame,text=phand[i].getButtonTextFormat(),wraplength=30,height=8,justify=CENTER).setMainText(phand[i].getButtonTextFormat()).setSubText("Card"+str(i+1)).switchToSubText()
                btn.setCardObj(phand[i])
                btn.config( command=lambda card=phand[i],btn=btn:self.__afterP.delCardFromFrame( btn,card,self.__cPublicFrame))
                btn.grid(row=0,column=i,rowspan=2,stick=N+S+E+W)
        self.frame2container.configure(scrollregion = self.frame2container.bbox("all"))        
        return self.__cPublicFrame
    def ckbCommand(self,cb):
        cb.switchValue()
        print("ckbcommand")
    def chgCkb(self,cb):
        cb.toggle()
        self.ckbCommand(cb)
        
    def getSelectedCardList(self):
        self.selectedCardCount=-1
        children = self.__cFrame.winfo_children()
        result = []
        for child in children:
            chd = child.winfo_children()
                
            if(chd[0].getValue() and chd[1].getCardObj().isDropable()):
                result.append(chd[1].getCardObj())
        
        if(len(result)!=2):
            print(children)
            print("error")
            print(result)
            self.selectedCardCount=len(result)
            tkinter.messagebox.showinfo(StringData.getDlgTitle_cardPopError(),StringData.getDlgContent_cardPopError())
            result=[]
        else:
            if(result[0].getRawLevel() != result[1].getRawLevel() ):
                result=[]
        return result
    
    def getCardFrame(self,player=None):
        if(player!=None and type(player)==Player):
            self.__currentP=player
        if(self.__cFrame!=None):# and len(self.__hand)!= len(self.__cFrame.winfo_children())):
            lst = self.__cFrame.winfo_children()
            for i in lst:
                i.destroy()
            if(self.__currentP!=None):
                phand = self.__currentP.getHand()
                for i in range(len(phand)):
                    Grid.columnconfigure(self.__cFrame,i,weight=1)
                    p=PanedWindow(self.__cFrame,orient=VERTICAL)
                    cb = ValueContainedCheckButton(p,width=0)
                    cb.config(command=lambda cb=cb: self.ckbCommand(cb))
                
                    cb.pack(fill=X)
                    txt= phand[i].getButtonTextFormat()
                    btn =CardButton(p,wraplength=30,height=8,text=txt).setMainText(phand[i].getButtonTextFormat()).setSubText("Card"+str(i+1)).switchToMainText()
                    btn.setCardObj(phand[i])
                #img=btn.getImage()
                    btn.config(command=lambda cb1=cb: self.chgCkb(cb1),height=8) #command=lambda card=self.__hand[i],btn=btn:self.delCardFromFrame( btn,card,mgcls=mgcls,isPublicFrame=False))
                    btn.pack(fill=Y)
                #btn.image = img
                    p.add(cb)
                    p.add(btn)
                    p.grid(row=0,column=i,rowspan=2,stick=N+S+E+W) #.pack(side=LEFT)
            
        elif(self.__cFrame==None):
            self.__cFrame = Frame(self.frame5)
            try:
                self.__cFrame.pack(fill=BOTH,expand=TRUE)
            except:
                pass
            if(self.__currentP!=None):
                phand = self.__currentP.getHand()
                
                for i in range(len(phand)):
                    Grid.columnconfigure(self.__cFrame,i,weight=1)
                    p=PanedWindow(self.__cFrame,orient=VERTICAL)
                
                    txt= phand[i].getButtonTextFormat()
                    cb = ValueContainedCheckButton(p,width=0)
                    cb.config(command=lambda cb=cb: self.ckbCommand(cb))
                    cb.pack(fill=X)
                    btn =CardButton(p,wraplength=30,height=8).setMainText(phand[i].getButtonTextFormat()).setSubText("Card"+str(i+1)).switchToMainText()
                    btn.setCardObj(phand[i])
                    #img = btn.getImage()
                    btn.config(command=lambda cb=cb: self.chgCkb(cb),height=8) #lambda card=self.__hand[i],btn=btn:self.delCardFromFrame( btn,card,mgcls=mgcls,isPublicFrame=False))
                    #btn.image = img
                    btn.pack(fill=Y)
                
                    p.add(cb)
                    p.add(btn)
                    p.grid(row=0,column=i,rowspan=2,stick=N+S+E+W) #.pack(side=LEFT)
                
            self.__cFrame.grid(row=0,column=0,stick="news")
        
        self.frame5container.configure(scrollregion = self.frame5container.bbox("all"))
            
        return self.__cFrame
    @property
    def internalConfigs(self):
        return self.__configs
    def setInternalConfigs(self,karg):
        for key in karg:
            self.__configs[key] = karg[key]
    @property
    def topFrame(self):
        return self.__topframe
    @property
    def orderListView(self):
        return self.porderlv
    @property
    def rankListView(self):
        return self.pranklv
    @property
    def preparingFrame(self):
        return self.__preparingFrame
    def create_widgets(self):
        
        self.__topframe = PanedWindow(self,orient=VERTICAL)
        self.__topframe.pack(fill=BOTH,anchor=CENTER,expand=True)
        self.__topframe.grid(row=0,column=0,sticky="news")

        frame4 = PanedWindow(self.__topframe)
        topcardframe = Frame(self.__topframe)
        bottomcardframe = Frame(self.__topframe)
        self.frame5container = Canvas(bottomcardframe,scrollregion=(0,0,1500,0))
        self.frame5 = Frame(self.frame5container)
        self.frame5.pack(fill=BOTH,expand=TRUE,padx=10)
        xscoller= Scrollbar(bottomcardframe,orient=HORIZONTAL,command=self.frame5container.xview)
        xscoller.pack(side=BOTTOM,fill=X,padx=10)
        self.frame5container.create_window((0,0), window=self.frame5, anchor=NW)
        self.frame5container.pack(fill=BOTH,expand=TRUE)
        self.frame5container.configure(xscrollcommand=xscoller.set)
        self.frame5container.create_oval(0,0,400,300,fill='red')
        self.frame2container = Canvas(topcardframe,scrollregion=(0,0,1500,0))
        self.frame2 = Frame(self.frame2container)
        self.frame2.pack(fill=BOTH,expand=TRUE)
        xscollertop= Scrollbar(topcardframe,orient=HORIZONTAL,command=self.frame2container.xview)
        xscollertop.pack(side=BOTTOM,fill=X,padx=10)

        self.frame2container.create_window((0,0), window=self.frame2, anchor=NW)
        self.frame2container.pack(side=TOP,fill=X,padx=10)
        self.frame2container.configure(xscrollcommand=xscollertop.set)
        
        self.__topframe.add(topcardframe,stretch="always")
        self.__topframe.add(frame4,stretch="always")
        self.__topframe.add(bottomcardframe,stretch="always")
        playerorderFrame = PanedWindow(frame4,orient=VERTICAL)
        playerRankFrame = PanedWindow(frame4,orient=VERTICAL)
        middleFrameContainter = LabelFrame(frame4, text="유저 조작 버튼 ")
        middleFrame = PanedWindow(middleFrameContainter)
        middleFrame.pack(fill=BOTH,expand=True)
        self.porderlv = Listbox(playerorderFrame,selectmode=NONE,height=8,width=20)
        self.pranklv = Listbox(playerRankFrame,selectmode=NONE,height=8,width=22)
        playerorderFrame.add(Label(playerorderFrame,text="플레이어 순서"))
        playerRankFrame.add(Label(playerRankFrame,text="플레이어 현재 랭킹"))
        playerorderFrame.add(self.porderlv)
        playerRankFrame.add(self.pranklv)
        frame4.add(playerorderFrame,stretch="always")
        frame4.add(middleFrameContainter,stretch="always")
        frame4.add(playerRankFrame,stretch="always")

        self.__preparingFrame = Frame(self.frame2)
        #self.__preparingFrame.pack(fill=X,expand=TRUE)
        self.__preparingFrame.pack(fill=X,expand=TRUE)
        self.__preparingFrame.grid(row=0,column=0,stick="news")
        Label(self.__preparingFrame,text="모든 플레이어들의 패에서 중복 숫자를 가진 카드들이 없을 때까지 기다리는중...").grid(row=0,column=0,columnspan=3)

        #self.__preparingFrame.pack()
        playerControllView = PanedWindow(middleFrame,orient=VERTICAL)
        playerControllView.add(Button(middleFrame,text="턴넘기기 ",command=self.__configs[OutputView.configKeyList()[0]]),stretch="always")
        playerControllView.add(Button(middleFrame,text="선택한 카드 버리기 ",command=self.__configs[OutputView.configKeyList()[1]]),stretch="always")
        playerControllView.add(Button(middleFrame,text="패 섞기 ",command=self.__configs[OutputView.configKeyList()[2]]),stretch="always")
        playerControllView.add(Button(middleFrame,text="패 정렬",command=self.__configs[OutputView.configKeyList()[3]]),stretch="always")
        middleFrame.add(playerControllView,stretch="always")
        initNames = self.__configs[OutputView.configKeyList()[6]]
        for i in range(len(initNames)):
            self.porderlv.insert(self.porderlv.size(),initNames[i])
           
        self.__configs[OutputView.configKeyList()[7]]() 
        self.frame5container.configure(scrollregion = self.frame5container.bbox("all"))
        self.frame2container.configure(scrollregion = self.frame2container.bbox("all"))
        self.doThread(self.frame5container,self.frame2container)
    def threadWork(self,f5c,f2c):
        import time
        time.sleep(0.2)
        f5c.configure(scrollregion = f5c.bbox("all"))
        f2c.configure(scrollregion = f2c.bbox("all"))
    def doThread(self,f5c,f2c):
        t = threading.Thread(target=self.threadWork ,args=(f5c,f2c,))
        t.start()
    @staticmethod
    def showGUI(tk):
        window =tk
        screen_width = int(window.winfo_screenwidth()*0.97)
        screen_height = int(window.winfo_screenheight()*0.95)
        window.geometry(str(screen_width)+"x"+str(screen_height))
        
        ov = OutputView(window)
        return ov
        #window.mainloop()