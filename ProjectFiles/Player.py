import json
import random
import time
from Deck import *
from Card import *
from tkinter import *
from StringData import *
import tkinter.messagebox
class Player:
    @staticmethod
    def someInternalConfigKeys():
        return ["ExistRemoveablePlayerCmd","refreshPlayerRankCmd","refreshDisplayedCardFrameCmd","transmitCard"]
    @property
    def frameConfigs(self):
        return self.__FrameCnfs
    def setFrameConfigs(self,kargs):
        for key in kargs:
            self.__FrameCnfs[key] = kargs[key]
    __FrameCnfs = {}
    __hand=None
    __name=""
    def shuffleDeck(self):
        self.__hand = self.__hand.shuffle()
    def setOutputViewObj(self,obj):
        self.__ovObj = obj
    def delSelectedCardsFromFrame(self):
        return self.delCardsFromFrame(self.__ovObj.getSelectedCardList())
    def delCardsFromFrame(self,cards):
        if(len(cards)>2 or cards == () or cards == []):
            return False
        isRemoved = self.popTwoCards(cards)
        if(isRemoved):
            self.__FrameCnfs[Player.someInternalConfigKeys()[0]]()
            self.__FrameCnfs[Player.someInternalConfigKeys()[1]]()
        return isRemoved
        
    def delCardFromFrame(self,btn,card,frame,**args):
        isDrpabe=card.isDropable()
        cd1=card.cloneCard()
        btn.destroy()
        self.__hand.remove(card)
        self.__FrameCnfs[Player.someInternalConfigKeys()[0]]()
            
        self.__FrameCnfs[Player.someInternalConfigKeys()[3]](cd1)
        self.__FrameCnfs[Player.someInternalConfigKeys()[2]]()
        self.__FrameCnfs[Player.someInternalConfigKeys()[1]]()
        try:
            for chd in frame.winfo_children():
                chd.configure(state='disable') 
        except:
            pass
        del btn,card

    
    
    @property
    def hasSameLevelCard(self):
        for i in range(len(Card.Levels())):
            count = 0
            for j in range(len(self.__hand)):
                if(self.__hand[j].level==i):
                    count+=1
            if(count>1):
                return True
        return False
            
    
    def sortDeck(self):
        self.__hand.sort(key=lambda card: card.level)
    __rootFrameCanvas = None
    
    @property
    def name(self):
        return self.__name
    def __init__(self,name):
        self.__ovObj=None
        self.__hand = Deck.getEmptyDeck();
        self.setName(name)
    def popTwoCards(self,cards):
        if(len(cards)>2):
            return False
        hasJoker = False
        for card in cards:
            hasJoker = hasJoker or (not card.isDropable())
            if(hasJoker):
                break
        if(not hasJoker):
            for card in cards:
                self.__hand.remove(card)
            return True
        return False
    def exportCard(self,exportingIdx):
        result = self.__hand[exportingIdx].cloneCard()
        del self.__hand[exportingIdx]
        return  result
    def importCard(self,card):
        self.__hand.append(card)

    def setName(self,Name):
        self.__name = Name
        return self
    def getName(self):
        return self.__name
    def setHand(self,hand):
        d = hand
        if(type(hand) == Deck):
            d= d.getCloneDeck()
        else:
            d = Deck.getEmptyDeck()
            d.extend(hand)
        self.__hand = d
    def setDeck(self,hand):
        return self.setHand(hand)
    
    def pushCard(self,card):
        self.importCard(card)
        return self.__hand
    def isComputer(self):
        return False
    def getHand(self):
        return self.__hand
    def getDeck(self):
        return self.__hand