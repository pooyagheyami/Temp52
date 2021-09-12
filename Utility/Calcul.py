#In the name of GOD
#please put your code under here
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanel4
###########################################################################
OPERATIONS = ('/', '*', '-', '+')
DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.')

class MyPanel1 ( wx.Panel ):
        
        def __init__( self, parent ):
                wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 176,236 ), style = wx.TAB_TRAVERSAL )
                
                Vsz1 = wx.BoxSizer( wx.VERTICAL )
                
                S1 = wx.BoxSizer( wx.VERTICAL )
                
                self.Result = wx.TextCtrl( self,id=-1, value='0',
                                           pos=wx.DefaultPosition,
                                           size=wx.DefaultSize,
                                           style=wx.TE_READONLY|wx.TE_RIGHT)
                
                S1.Add( self.Result, 1, wx.ALL|wx.EXPAND, 5 )
                
                
                Vsz1.Add( S1, 1, wx.EXPAND, 5 )
                
                Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
                
                V1 = wx.BoxSizer( wx.VERTICAL )
                
                S1 = wx.BoxSizer( wx.HORIZONTAL )
                
                self.Bclr = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
                S1.Add( self.Bclr, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
                
                self.btnt = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
                S1.Add( self.btnt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                self.btnz = wx.Button( self, wx.ID_ANY, u"*", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
                S1.Add( self.btnz, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
                
                
                V1.Add( S1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                self.Pnum = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER )
                V2 = wx.BoxSizer( wx.VERTICAL )
                
                FGS = wx.FlexGridSizer( 3, 3, 0, 0 )
                FGS.SetFlexibleDirection( wx.BOTH )
                FGS.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

                lbl = '789456123'
                self.btns = []
                i = 0
                for c in lbl:
                        self.btns.append(wx.Button( self.Pnum, wx.ID_ANY, c, wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT ))
                        FGS.Add( self.btns[i], 0, wx.ALL, 5 )
                        self.btns[i].Bind( wx.EVT_BUTTON, self.OnChar )
                        i = i + 1
                    
                                
                V2.Add( FGS, 1, wx.EXPAND, 5 )
                
                H2 = wx.BoxSizer( wx.HORIZONTAL )
                
                self.btn0 = wx.Button( self.Pnum, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
                H2.Add( self.btn0, 1, wx.ALL, 5 )
                
                self.btni = wx.Button( self.Pnum, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
                H2.Add( self.btni, 0, wx.ALL, 5 )
                
                
                V2.Add( H2, 1, wx.EXPAND, 5 )
                
                
                self.Pnum.SetSizer( V2 )
                self.Pnum.Layout()
                V2.Fit( self.Pnum )
                V1.Add( self.Pnum, 1, wx.EXPAND |wx.ALL, 5 )
                
                
                Hsz1.Add( V1, 1, wx.EXPAND, 5 )
                
                V3 = wx.BoxSizer( wx.VERTICAL )
                
                self.btnm = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
                V3.Add( self.btnm, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                self.btnp = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
                V3.Add( self.btnp, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                self.btnq = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
                V3.Add( self.btnq, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
                
                
                Hsz1.Add( V3, 1,  wx.EXPAND, 5 )
                
                
                Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )
                
                
                self.SetSizer( Vsz1 )
                self.Layout()

                self.Centre( wx.BOTH )
                # Connect Events
                self.Bclr.Bind( wx.EVT_BUTTON, self.OnChar )
                self.btnt.Bind( wx.EVT_BUTTON, self.OnChar )
                self.btnz.Bind( wx.EVT_BUTTON, self.OnChar )

                self.btn0.Bind( wx.EVT_BUTTON, self.OnChar )
                self.btni.Bind( wx.EVT_BUTTON, self.OnChar )

                self.btnm.Bind( wx.EVT_BUTTON, self.OnChar )
                self.btnp.Bind( wx.EVT_BUTTON, self.OnChar )
                self.btnq.Bind( wx.EVT_BUTTON, self.OnChar )

                self.update = None
                self.operation = None
                self.last = None
                self.resolved = None
        
        def __del__( self ):
                pass

        def OnChar( self, event ):
                """This Calculator method is called on every button click"""
                # define event variables: button, it's label, text field value
                button = event.GetEventObject()
                label = button.GetLabel()
                value = self.getValue()
                

                # below we handle our event differently based on button clicked

                # Clear button
                if label == 'C':
                        # simply reset display and forgot any custom calculator variables
                        self.Clear()

                # digit button pressed
                elif label in DIGITS:
                        # it's important to clear display before:
                        # * new operation
                        # * after zero digit
                        # * and after solve() funtion, '=' button
                        
                        if value == '0' or value in OPERATIONS or self.resolved:
                                #self.update('')
                                self.OnCalcu('')
                                self.resolved = False

                        self.Result.AppendText(label)

                # equal sign: try to calculate results
                elif label == '=':
                        # try to solve our equation
                        self.solve()

                # clicked operation button
                elif label in OPERATIONS:
                        # before any new operation try to solve previous operation
                        self.solve()

                        # remember previously entered number
                        # if user is just changing operation - no need to remember any value
                        if value not in OPERATIONS:
                                self.last = self.getValue()

                        # update last operation used and set display to operation label
                        self.operation = label
                        self.OnCalcu(label)

    
        def Clear(self):
                """Calculator Clear button"""
                self.Result.SetValue('0')
                self.operation = None
                self.last = None
                

        def update(self, value):
                """Shortcut for display update value"""
                self.Result.SetValue(str(value))

        def getValue(self):
                """Shortcut for display get value"""
                return self.Result.GetValue()

        def solve(self):
                """Equal operation: let's calculate result"""
                # only calculate anything if we got both: operation and last value
                if (self.last != None) and (self.operation != None):
                        # here we use strings and eval to calculate result
                        result =  str(eval(
                                # e.g.  "67 - 24"
                                u'float('+self.last+')'+ self.operation + 'float('+self.getValue()+')'
                        ))
                        # finally reset calculator values and update display with result
                        self.operation = None
                        self.last = None
                        self.OnCalcu(result)
                        self.resolved = True
                       

                        
        

        def OnKey( self, event ):
                pass
                
        def OnCalcu( self, value ):
                
                self.Result.SetValue(str(value))
                return None

class Calculator ( wx.Frame ):
        def __init__(self, parent):
                wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
                self.parent= parent

                self.Pnl = MyPanel1(self)

        def closeit(self):
                self.Close(True)

def size():
	return (-1,-1)

def main(panel=None ):
	parent =  panel.GetParent()

	frame = Calculator(parent )
	frame.SetTitle(u'Form')
	frame.SetSize(size())
	frame.Show()

if __name__ == '__main__':
	main()
