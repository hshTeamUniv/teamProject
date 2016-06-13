from tkinter import *
class CardButton(Button):
    __mainText=""
    __subText=""
    def __init__(self, master=None, **kargs):
        super().__init__( master, kargs)
        self.__cardObj=None
        
    
    def setCardObj(self,co):
        self.__cardObj = co
    def getCardObj(self):
        return self.__cardObj
    def setMainText(self,txt):
        self.__mainText=txt
        return self
    def getImage(self):
        return self.__cardObj.getImage()
    def setSubText(self,txt):
        self.__subText=txt
        return self
    def switchToMainText(self):
        if(self['text']!=self.__mainText):
            self['text']=self.__mainText
        return self
    def switchToSubText(self):
        if(self['text']!=self.__subText):
            self['text']=self.__subText
        return self
    def swipeText(self):
        if(self['text']==self.__mainText):
            self['text']==self.__subText
        else:
            self['text']==self.__mainText
        return self
