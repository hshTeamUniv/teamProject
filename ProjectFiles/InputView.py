from tkinter import *
from StringData import *
from WaitingRoom import *
class InputView:
    
    @staticmethod
    def getWaitingRoomFrameWithWait(master,resp):
        result = WaitingRoom(master,resp)
        
        return result
    