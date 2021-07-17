# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python

import wx
import Database.wxsq as DB
#import Database.wxsq as SQ
from GUI.proman import Mymenu,DoProgram

class MyPanel(wx.Panel):
    def __init__(self,parent,id,pos,siz,style):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 142,396 ), style = wx.TAB_TRAVERSAL )

        self.parent = parent
        
        inmenu = Mymenu()

        lbl = inmenu.Revitm()
                    
        self.btn = []
        VSiz = wx.BoxSizer( wx.VERTICAL )
        i = 0
        for b in lbl:
            if b[0] != None:
                self.btn.append( wx.Button( self, b[1], str(b[0]), wx.DefaultPosition, wx.DefaultSize, 0 ))
                VSiz.Add( self.btn[i], 0, wx.ALL, 5 )
                #self.btn[i].Bind( wx.EVT_BUTTON, self.onbtn  )
                i +=1
            else:
                self.line = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
                VSiz.Add( self.line, 0, wx.EXPAND |wx.ALL, 5 )

        
        
    
        self.SetSizer( VSiz )
        self.Layout()
