#Chen Lu. ID:51398516. ICS LAB 5.

#Note 1: Empty space: 0, black: 1, white: 2.
#Note 2: All elements in the board are string.
import tkinter

class gamestate:
    def __init__(self, rows:str, cols:str, turn: str, arrange:str, how:str):
        self.rows=rows
        self.cols=cols
        self.turn=turn
        self.arrange=arrange
        self.how=how
        self.board=[]
        self.arow=0
        self.acol=0
        self.adiag=0
        
    def ifwinner(self):        
        answerlist=[]
        answerlist.append(True) #True stands for no winner
        answerlist.append('0') #winner
        plainstr=''
        for onerow in range(int(self.rows)):
            for onecol in range(int(self.cols)):
                plainstr=plainstr+self.board[onerow][onecol]
        if '0' not in plainstr:
            answerlist[0]=False
            answerlist[1]=self.calwinner(plainstr)
            return answerlist
        for onerow in range(1,int(self.rows)+1,1):          
            for onecol in range(1,int(self.cols)+1,1):
                locapair=[onerow,onecol]
                if self.board[onerow-1][onecol-1]=='0':
                    if self.checkapicsvalid(locapair)==True:
                        return answerlist
        self.switchturn()
        for onerow in range(1,int(self.rows)+1,1):            
            for onecol in range(1,int(self.cols)+1,1):
                locapair=[onerow,onecol]
                if self.board[onerow-1][onecol-1]=='0':
                    if self.checkapicsvalid(locapair)==True:
                        return answerlist
        answerlist[0]=False
        answerlist[1]=self.calwinner(plainstr)
        return answerlist
                                  
    def calwinner(self,plainstr):
        white=0
        black=0
        for onechara in plainstr:
            if onechara=='1':
                black+=1
            elif onechara=='2':
                white+=1
        if self.how=='More pieces win':
            if white > black:
                return '2'
            elif white < black:
                return '1'
            else:
                return '0'
        else:
            if white > black:
                return '1'
            elif white < black:
                return '2'
            else:
                return '0'
       
    def checknum(self):
        self.black=0
        self.white=0
        for eachlist in self.board:
            for each_item in eachlist:
                if each_item=='1':
                    self.black+=1
                if each_item=='2':
                    self.white+=1
        return (self.black,self.white)
    
    def printnumber(self):
        number_tuple=(self.checknum())
        print('B:',number_tuple[0],' ','W:',number_tuple[1])
        
    def new_board(self):
        '''return a new and empty game board with initial pices on it'''        
        for self.row in range(int(self.rows)):
            self.board.append([])
            for self.col in range(int(self.cols)):
                self.board[-1].append('0')
        if self.arrange=='Black':
            self.board[int(int(self.rows)/2-1)][int(int(self.cols)/2-1)]='1'
            self.board[int(int(self.rows)/2)][int(int(self.cols)/2)]='1'
            self.board[int(int(self.rows)/2-1)][int(int(self.cols)/2)]='2'
            self.board[int(int(self.rows)/2)][int(int(self.cols)/2-1)]='2'     
        else:
            self.board[int(int(self.rows)/2-1)][int(int(self.cols)/2-1)]='2'
            self.board[int(int(self.rows)/2)][int(int(self.cols)/2)]='2'
            self.board[int(int(self.rows)/2-1)][int(int(self.cols)/2)]='1'
            self.board[int(int(self.rows)/2)][int(int(self.cols)/2-1)]='1'
        return self.board
    
    def switchturn(self):
        '''switch the turn'''
        if self.turn=='Black' or self.turn=='1':
            self.turn='2'
        elif self.turn=='White' or self.turn=='2':
            self.turn='1'
            
    def decideturn(self):
        '''decide the turn'''
        if self.turn=='Black' or self.turn=='1':
            self.turn='1'
        elif self.turn=='White' or self.turn=='2':
            self.turn='2'
                
    def checkapicsvalid(self,locationpair):
        '''if len(locationpair)==0:
            return True'''
        rownum=int(locationpair[0])-1
        colnum=int(locationpair[1])-1
        actrangerows=int(self.rows)-1
        actrangecols=int(self.cols)-1
        if self.board[rownum][colnum]=='1' or self.board[rownum][colnum]=='2':
            return False
        targetlist=self.generatechecklist(rownum,colnum,actrangerows,actrangecols)
        rowresult=self.checkrow(targetlist,rownum,colnum)
        colresult=self.checkcol(targetlist,rownum,colnum)
        diagresult=self.checkdiag(targetlist,rownum,colnum)
        if len(rowresult) == 0 and len(colresult)== 0 and len(diagresult[0])==0 and len(diagresult[1])==0 and len(diagresult[2])==0 and len(diagresult[3])==0:
            return False
        self.arow=rowresult
        self.acol=colresult
        self.adiag=diagresult     
        return True

    def updateboard(self,locapair):
        orgrow=int(locapair[0])-1
        orgcol=int(locapair[1])-1
        changelist=[]
        if len(self.arow)!=0:            
            for one in self.arow:            
                changelist.append(one)
        if len(self.acol)!=0:
            for one in self.acol:
                changelist.append(one)
        for one in self.adiag:
            if len(one)!=0:
                for oneitem in one:
                    changelist.append(oneitem) 
        if self.turn =='1':
            for one in changelist:
                onerow=one[0]
                onecol=one[1]
                self.board[onerow][onecol]='1'
            self.board[orgrow][orgcol]='1'               
        else:
            for one in changelist:
                onerow=one[0]
                onecol=one[1]
                self.board[onerow][onecol]='2'
            self.board[orgrow][orgcol]='2'
            
    def generatechecklist(self,rownum:int,colnum:int,actrangerows:int,actrangecols:int)->list:
        targetlist=[]
        for row in range(actrangerows+1):
            if row > rownum:
                targetlist.append([row,colnum,'colsame','+'])
            if row < rownum:
                targetlist.append([row,colnum,'colsame','-'])
        for col in range(actrangecols+1):
            if col > colnum:
                targetlist.append([rownum,col,'rowsame','+'])
            if col < colnum:
                targetlist.append([rownum,col,'rowsame','-'])
        rownumcopy=rownum
        colnumcopy=colnum
        while (rownumcopy+1)<= actrangerows and (colnumcopy+1)<= actrangecols:
            targetlist.append([rownumcopy+1, colnumcopy+1, 'diagsame','downright'])
            rownumcopy+=1
            colnumcopy+=1
        rownumcopy=rownum
        colnumcopy=colnum
        while (rownumcopy-1)>= 0 and (colnumcopy-1)>= 0:
            targetlist.append([rownumcopy-1, colnumcopy-1, 'diagsame','upleft'])
            rownumcopy-=1
            colnumcopy-=1
        rownumcopy=rownum
        colnumcopy=colnum
        while (rownumcopy+1)<= actrangerows and (colnumcopy-1)>= 0:
            targetlist.append([rownumcopy+1, colnumcopy-1, 'diagsame','downleft'])
            rownumcopy+=1
            colnumcopy-=1
        rownumcopy=rownum
        colnumcopy=colnum
        while (rownumcopy-1)>= 0 and (colnumcopy+1)<= actrangecols:
            targetlist.append([rownumcopy-1, colnumcopy+1, 'diagsame','upright'])
            rownumcopy-=1
            colnumcopy+=1
        return targetlist

    def checkrow(self,targetlist,rownum,colnum):
        answerlist=[]
        inlistindex=0
        rowlistincr=[]
        rowlistdecr=[]
        rawrowlistdecr=[]
        incrchecklist=[]
        decrchecklist=[]
        for oneitem in targetlist:
            if oneitem[2]=='rowsame' and oneitem[3]=='+':
                rowlistincr.append(oneitem)
            if oneitem[2]=='rowsame' and oneitem[3]=='-':
                rawrowlistdecr.append(oneitem)
        for onenum in range(len(rawrowlistdecr)-1,-1,-1):
            rowlistdecr.append(rawrowlistdecr[onenum])
        for position in rowlistincr:
            rowindex=position[0]
            colindex=position[1]
            incrchecklist.append(self.board[rowindex][colindex])
        checkstr=''
        for oneitem in incrchecklist:
            checkstr=checkstr+oneitem
        if str(self.turn) in checkstr:
            checkindex=0
            for oneitem in incrchecklist:
                if oneitem!=self.turn:
                    inlistindex+=1
                else:
                    break            
            for onenum in range(inlistindex+1):
                if incrchecklist[onenum]!= self.turn and incrchecklist[onenum]!='0':
                    checkindex+=1
                else:
                    break           
            if checkindex==inlistindex and checkindex!= 0:
                for onenum in range(checkindex+1):
                    thisitem=[rownum]
                    thisitem.append(rowlistincr[onenum][1])
                    answerlist.append(thisitem)
        inlistindex=0
        for position in rowlistdecr:
            rowindex=position[0]
            colindex=position[1]
            decrchecklist.append(self.board[rowindex][colindex])
        checkstr=''
        for oneitem in decrchecklist:
            checkstr=checkstr+oneitem
        if str(self.turn) in checkstr:
            checkindex=0
            for oneitem in decrchecklist:
                if oneitem!=self.turn:
                    inlistindex+=1
                else:
                    break
            for onenum in range(inlistindex+1):
                if decrchecklist[onenum]!= self.turn and decrchecklist[onenum]!='0':
                    checkindex+=1
                else:
                    break
            if checkindex==inlistindex and checkindex!= 0:
                for onenum in range(checkindex+1):
                    thisitem=[rownum]
                    thisitem.append(rowlistdecr[onenum][1])
                    answerlist.append(thisitem)
        return answerlist
        
    def checkcol(self,targetlist,rownum,colnum):
        answerlist=[]
        inlistindex=0
        collistincr=[]
        collistdecr=[]
        rawcollistdecr=[]
        incrchecklist=[]
        decrchecklist=[]
        for oneitem in targetlist:
            if oneitem[2]=='colsame' and oneitem[3]=='+':
                collistincr.append(oneitem)
            if oneitem[2]=='colsame' and oneitem[3]=='-':
                rawcollistdecr.append(oneitem)
        for onenum in range(len(rawcollistdecr)-1,-1,-1):
            collistdecr.append(rawcollistdecr[onenum])
        for position in collistincr:
            rowindex=position[0]
            colindex=position[1]
            incrchecklist.append(self.board[rowindex][colindex])
        checkstr=''
        for oneitem in incrchecklist:
            checkstr=checkstr+oneitem
        if str(self.turn) in checkstr:            
            checkindex=0
            for oneitem in incrchecklist:
                if oneitem!=self.turn:
                    inlistindex+=1
                else:
                    break
            for onenum in range(inlistindex+1):
                if incrchecklist[onenum]!= self.turn and incrchecklist[onenum]!='0':
                    checkindex+=1
                else:
                    break
            if checkindex==inlistindex and checkindex!= 0:
                for onenum in range(checkindex+1):
                    thisitem=[0]
                    thisitem.append(colnum)
                    thisitem[0]=collistincr[onenum][0]
                    answerlist.append(thisitem)                
        inlistindex=0
        for position in collistdecr:
            rowindex=position[0]
            colindex=position[1]
            decrchecklist.append(self.board[rowindex][colindex])
        checkstr=''
        for oneitem in decrchecklist:
            checkstr=checkstr+oneitem
        if str(self.turn) in checkstr:
            checkindex=0
            for oneitem in decrchecklist:
                if oneitem!=self.turn:
                    inlistindex+=1
                else:
                    break
            for onenum in range(inlistindex+1):
                if decrchecklist[onenum]!= self.turn and decrchecklist[onenum]!='0':
                      checkindex+=1
                else:
                    break
            if checkindex==inlistindex and checkindex!= 0:
                for onenum in range(checkindex+1):
                    thisitem=[0]
                    thisitem.append(colnum)
                    thisitem[0]=collistdecr[onenum][0]
                    answerlist.append(thisitem)
        return answerlist
    
    def checkdiag(self,targetlist,rownum,colnum):
        answerlist=[]
        uprawlist=[]
        downrawlist=[]
        upleftlist=[]
        uprightlist=[]
        downrightlist=[]
        downleftlist=[]
        upleftchecklist=[]
        uprightchecklist=[]
        downleftchecklist=[]
        upleftchecklist=[]
        for item in targetlist:
            if item[2]=='diagsame' and item[3][0]=='u':
                uprawlist.append(item)
            elif item[2]=='diagsame' and item[3][0]=='d':
                downrawlist.append(item)
        for item in uprawlist:
            if item[3][2]=='r':
                uprightlist.append(item)
            else:
                upleftlist.append(item)
        for item in downrawlist:
            if item[3][4]=='r':
                downrightlist.append(item)
            else:
                downleftlist.append(item)
        uprightchecklist=self.appendlist(uprightlist)
        upleftchecklist=self.appendlist(upleftlist)
        downleftchecklist=self.appendlist(downleftlist)
        downrightchecklist=self.appendlist(downrightlist)
        answerlist.append(self.appendvalidposition(uprightchecklist,rownum,colnum,'ur'))
        answerlist.append(self.appendvalidposition(upleftchecklist,rownum,colnum,'ul'))
        answerlist.append(self.appendvalidposition(downleftchecklist,rownum,colnum,'dl'))
        answerlist.append(self.appendvalidposition(downrightchecklist,rownum,colnum,'dr'))
        return answerlist

    def appendlist(self, alist):
        answerlist=[]
        for position in alist:
            rowindex=position[0]
            colindex=position[1]
            answerlist.append(self.board[rowindex][colindex])
        return answerlist         
                
    def appendvalidposition(self,alist,rownum,colnum,para):
        checkstr=''
        answerlist=[]
        inlistindex=0
        for oneitem in alist:
            checkstr=checkstr+oneitem
        if str(self.turn) in checkstr:
            checkindex=0
            for oneitem in alist:
                if oneitem!=self.turn:
                    inlistindex+=1
                else:
                    break
            for onenum in range(inlistindex+1):
                if alist[onenum]!= self.turn and alist[onenum]!='0':
                    checkindex+=1
                else:
                    break
            if checkindex==inlistindex and checkindex!= 0:
                for onenum in range(checkindex+1):
                    if para=='ur':
                        thisitem=[]
                        thisitem.append(rownum-onenum)
                        thisitem.append(colnum+onenum)
                        answerlist.append(thisitem)
                    if para=='ul':
                        thisitem=[]
                        thisitem.append(rownum-onenum)
                        thisitem.append(colnum-onenum)
                        answerlist.append(thisitem)
                    if para=='dl':
                        thisitem=[]
                        thisitem.append(rownum+onenum)
                        thisitem.append(colnum-onenum)
                        answerlist.append(thisitem)
                    if para=='dr':
                        thisitem=[]
                        thisitem.append(rownum+onenum)
                        thisitem.append(colnum+onenum)
                        answerlist.append(thisitem)                  
        return answerlist
                    
                
            
                
        
        
        
    

