#Chen Lu. ID:51398516. ICS LAB 5.

from proj_5_logic import *
from tkinter.ttk import *
from math import *
import tkinter


class startwindow:
    def __init__(self):
        self.pair=[]
        self.boardlocapics=[]
        self.rowfraclist=[]
        self.colfraclist=[]
        self.rownum=1
        self.colnum=1
        self.rowspace=0
        self.colspace=0
        self.turn=''
        self.arrange=''
        self.how=''
        self.thisgamestate=gamestate(self.rownum,self.colnum,self.turn,self.arrange,self.how)
        self._startwindow=tkinter.Tk()
        self._startwindow.title('Option Window')
        self._canvas=tkinter.Canvas(master=self._startwindow,
                                    width=300, height=45,
                                    )
        
        self._canvas.grid(
            row = 0, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        
        self._startwindow.rowconfigure(0, weight = 1)
        self._startwindow.columnconfigure(0, weight = 1)
        
        self.rowlabel=Label(master=self._startwindow,text='How many rows:',
                            font = ('Helvetica', 15))
        self.rowlabel.grid(row=0, column=0, padx=10, pady=10,
                           sticky=tkinter.W+tkinter.N)
        self.collabel=Label(master=self._startwindow,text='How many colnums:',
                            font = ('Helvetica', 15))
        self.collabel.grid(row=1, column=0, padx=10, pady=10,
                           sticky=tkinter.W+tkinter.N)
        self.turnlabel=Label(master=self._startwindow,text='Who moves first:',
                            font = ('Helvetica', 15))
        self.turnlabel.grid(row=2, column=0, padx=10, pady=10,
                           sticky=tkinter.W+tkinter.N)
        self.arrangelabel=Label(master=self._startwindow,text='Upper left piece:',
                            font = ('Helvetica', 15))
        self.arrangelabel.grid(row=3, column=0, padx=10, pady=10,
                           sticky=tkinter.W+tkinter.N)
        self.winlabel=Label(master=self._startwindow,text='Win condition:',
                            font = ('Helvetica', 15))
        self.winlabel.grid(row=4, column=0, padx=10, pady=10,
                           sticky=tkinter.W+tkinter.N)


        self.rowbox=tkinter.ttk.Combobox(master=self._startwindow,
                                         width=15,font=('Helvetica', 15),
                                         value=[4,6,8,10,12,14,16],
                                         state='readonly')
        self.rowbox.grid(row=0, column=1, padx=10, pady=10,
                           sticky=tkinter.E+tkinter.N)
        self.colbox=tkinter.ttk.Combobox(master=self._startwindow,
                                         width=15,font=('Helvetica', 15),
                                         value=[4,6,8,10,12,14,16],
                                         state='readonly')
        self.colbox.grid(row=1, column=1, padx=10, pady=10,
                           sticky=tkinter.E+tkinter.N)
        self.turnbox=tkinter.ttk.Combobox(master=self._startwindow,
                                         width=15,font=('Helvetica', 15),
                                         value=['Black','White'],
                                         state='readonly')
        self.turnbox.grid(row=2, column=1, padx=10, pady=10,
                           sticky=tkinter.E+tkinter.N)
        self.arrangebox=tkinter.ttk.Combobox(master=self._startwindow,
                                         width=15,font=('Helvetica', 15),
                                         value=['Black','White'],
                                         state='readonly')
        self.arrangebox.grid(row=3, column=1, padx=10, pady=10,
                           sticky=tkinter.E+tkinter.N)
        self.winbox=tkinter.ttk.Combobox(master=self._startwindow,
                                         width=15,font=('Helvetica', 15),
                                         value=['More pieces win','Less pieces win'],
                                         state='readonly')
        self.winbox.grid(row=4, column=1, padx=10, pady=10,
                           sticky=tkinter.E+tkinter.N)
        self.startbutton=tkinter.Button(master=self._startwindow,
                                       text='START',font=('Helvetica', 15),command=self.startpressed
                                       )
        self.startbutton.grid(row=5, column=0, padx=0, pady=10,
                           sticky=tkinter.N+tkinter.E)

        self._boardwindow=tkinter.Tk()
        self._boardwindow.title('Othello')
        self._canvas=tkinter.Canvas(master=self._boardwindow,width=600,
                                    height=600,background='green')
        self._canvas.grid(row=0,column=0,padx=0,pady=0,
                          sticky=tkinter.N+tkinter.E+tkinter.W+tkinter.S)

        self._canvas_width=self._canvas.winfo_width()
        self._canvas_height=self._canvas.winfo_height()

        self._boardwindow.rowconfigure(0,weight=1)
        self._boardwindow.columnconfigure(0,weight=1)

        self._canvas.bind('<Configure>',self._resized)
        self._canvas.bind('<Button-1>',self._clickedonce)

    def start(self):
        self._boardwindow.mainloop()
        
    def startpressed(self):
        checker=0
        self.rownum=self.rowbox.get()
        self.colnum=self.colbox.get()
        self.turn=self.turnbox.get()
        self.arrange=self.arrangebox.get()
        self.how=self.winbox.get()
        if self.rownum=='' or self.colnum=='' or self.turn=='' or self.arrange=='' or self.how=='':
            self._boardwindow.destroy()
            self._startwindow.destroy()
            return
        self.thisgamestate=gamestate(self.rownum,self.colnum,self.turn,self.arrange,self.how)
        self._startwindow.destroy()      
        self.thisgamestate.new_board()
        self.thisgamestate.decideturn()
        self.drawboard()
        

    def _clickedonce(self,event:tkinter.Event):
        self._clicked(event)
        while True:
            if self.thisgamestate.checkapicsvalid(self.pair)==True:
                self.thisgamestate.updateboard(self.pair)
                self.thisgamestate.switchturn()
                self.drawboard()              
                if self.thisgamestate.ifwinner()[0]:
                    self.drawboard()
                else:
                    self.printinfowin()
            else:
                break

    def printinfo(self):
        text1='Black:'+str(self.thisgamestate.checknum()[0])+'     White:'+str(self.thisgamestate.checknum()[1])
        text2=''
        if self.thisgamestate.turn=='1':
            text2='Turn: Black'
        if self.thisgamestate.turn=='2':
            text2='Turn: White'
        self.Label1=Label(master=self._boardwindow,text=text1,
                          font=('Helvetica', 15))
        self.Label1.grid(row=4, column=0, padx=80, pady=10,
                           sticky=tkinter.S)
        self.Label1=Label(master=self._boardwindow,text=text2,
                          font=('Helvetica', 15))
        self.Label1.grid(row=5, column=0, padx=80, pady=10,
                           sticky=tkinter.S)

    def printinfowin(self):
        text1='Black:'+str(self.thisgamestate.checknum()[0])+'     White:'+str(self.thisgamestate.checknum()[1])
        text2=''
        if self.thisgamestate.ifwinner()[1]=='1':
            text2='Winner: Black'
        elif self.thisgamestate.ifwinner()[1]=='2':
            text2='Winner: White'
        else:
            text2='No winner'
        self.Label1=Label(master=self._boardwindow,text=text1,
                          font=('Helvetica', 15))
        self.Label1.grid(row=4, column=0, padx=80, pady=10,
                           sticky=tkinter.S)
        self.Label1=Label(master=self._boardwindow,text=text2,
                          font=('Helvetica', 15))
        self.Label1.grid(row=5, column=0, padx=80, pady=10,
                           sticky=tkinter.S)
             
    def _clicked(self,event:tkinter.Event):
        self._canvas_width=self._canvas.winfo_width()
        self._canvas_height=self._canvas.winfo_height()
        click_point=self.from_pixel(event.x,event.y,
                                     self._canvas_width,
                                     self._canvas_height)
        pointx=click_point[0]
        pointy=click_point[1]
        self.changetologic(pointx,pointy)
        
    def from_pixel(self,eventx,eventy,self_canvas_width,self_canvas_height):
        return (eventx/self_canvas_width,
                eventy/self_canvas_height)
        
    def changetologic(self,pointx,pointy):
        self.pair=[]
        yloca=int(int(pointx//self.colspace)+1)
        xloca=int(int(pointy//self.rowspace)+1)
        self.pair.append(xloca)
        self.pair.append(yloca)

    def drawboard(self):
        self._canvas.delete(tkinter.ALL)
        self._canvas_width=self._canvas.winfo_width()
        self._canvas_height=self._canvas.winfo_height()       
        self.rowspace=1/int(self.rownum)
        self.colspace=1/int(self.colnum)
        self.genfracrowlist()
        self.genfraccollist()
        self.drawlines()
        self.drawpics()
        self.printinfo()

    def drawpics(self):        
        inityspace=0
        for onerow in self.thisgamestate.board:
            initxspace=0
            for onecol in onerow:               
                if onecol=='1':
                    self.drawblack(initxspace,inityspace)
                elif onecol=='2':
                    self.drawwhite(initxspace,inityspace)
                initxspace+=self.colspace
            inityspace+=self.rowspace

    def drawblack(self,initxspace,inityspace):
        self._canvas_width=self._canvas.winfo_width()
        self._canvas_height=self._canvas.winfo_height()
        self._canvas.create_oval(initxspace*self._canvas_width,
                                   inityspace*self._canvas_height,
                                   (initxspace+self.colspace)*self._canvas_width,
                                   (inityspace+self.rowspace)*self._canvas_height,
                                   fill='black')

    def drawwhite(self,initxspace,inityspace):
        self._canvas_width=self._canvas.winfo_width()
        self._canvas_height=self._canvas.winfo_height()
        self._canvas.create_oval(initxspace*self._canvas_width,
                                   inityspace*self._canvas_height,
                                   (initxspace+self.colspace)*self._canvas_width,
                                   (inityspace+self.rowspace)*self._canvas_height,
                                   fill='white')
                 
    def genfracrowlist(self):
        initspace=0
        self.rowfraclist=[]
        while True:
            if initspace < 1:
                self.rowfraclist.append(initspace)
                initspace+=self.colspace
            else:
                break
        self.rowfraclist.append(1)

    def genfraccollist(self):
        initspace=0
        self.colfraclist=[]
        while True:
            if initspace < 1:
                self.colfraclist.append(initspace)
                initspace+=self.rowspace
            else:
                break
        self.colfraclist.append(1)

    def drawlines(self):        
        self.drawvertical()
        self.drawhori()

    def drawvertical(self):
        self._canvas_width=self._canvas.winfo_width()
        self._canvas_height=self._canvas.winfo_height()
        for one in self.rowfraclist:
            
            self._canvas.create_line(one*self._canvas_width,0,
                                one*self._canvas_width,
                                self._canvas_height,fill='black')
                
    def drawhori(self):
        self._canvas_width=self._canvas.winfo_width()
        self._canvas_height=self._canvas.winfo_height()
        for one in self.colfraclist:           
            self._canvas.create_line(0,self._canvas_height*one,
                                self._canvas_width,
                                self._canvas_height*one,fill='black')
    
    def _resized(self,event:tkinter.Event):        
        self.drawboard()
        
    

if __name__ == '__main__':
    app=startwindow().start()

