# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wx
import wx.aui
import wx.html

import GUI.MainMenu2 as MM
import GUI.MainTool as MT

import GUI.AuiPanel.PAui as PA

import importlib

import GUI.BG2 as BG

#import Config.basedata as bs
#import Utility.massage as ms
import Utility.eCalClak1 as C1
import Utility.DigitClack as DgK
#import Utility.user as user
from Config.Init import * 
import wx.dataview

import GUI.proman as pro
  
class MainWin(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title=u'main',size=(800,600))

        #Check config for first start prgram ===============
        
        #Check config for show or hide aui panels=========

        STBT = 'N'
        bps = 1
        tps = 1
        BGF = "V10.jpg"

        #Menu of Program============== 
        menu = MM.MainMenu()

        statusBar = self.CreateStatusBar()
        imenu = menu.createMenuBar()

        if len(imenu.GetMenus()) > 1:
            self.SetMenuBar(imenu)
            h = menu.GetItemId()
            h1 = menu.mid
            self.Bind(wx.EVT_MENU_RANGE, self.OnMenu, id=h1, id2=h.GetId())

        #Enable or Disable Menu==========================
        #imenu.EnableTop(3, False)

        #Show aui panels==============
        #self.Toolbar()


        #Aui Panels of Program==================
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow( self )
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        # Create Tool Bars=======================
        if STBT == 'N':
            self.Toolbar()
        else:
            self.ToolPnl()

        #Panel report=======================
        #self.Stpnl(sps)
        #All Panel Aui=======================
        self.APnls()

        #set background in frame ==================
        self.BGrnd(bps,BGF)


        self.m_mgr.Update()
        self.Centre( wx.BOTH )

        #Show other win in main windows==============

        DigitK = DgK.MyFrame1(self)
        DigitK.SetSize((270,95))
        DigitK.SetPosition((970,100))
        DigitK.Show()
        '''
        if C == 1:
            wino = wx.Frame(self,-1,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
            
            txt = bs.Startpro()
            Startp = ms.MyPanel1(wino,txt)

            wino.SetSize((600,400))
            wino.SetPosition((100,100))
            wino.Show()
        
        '''
        self.Clock(tps)
        self.Update()

    def OnMenu(self, event):
        self.mid = event.GetId()
        #print( self.mid )
        a = pro.DoProgram(self.mid,'M')
        #print dir(a)
        s = a.size() if 'size' in dir(a) else ()
        
        win1 = wx.Frame(self, -1)
        win1.SetSize(s)
        a.main(win1)

    def OnTool(self, event):
        self.tid = event.GetId()
        #print( self.tid )
        a = pro.DoProgram(self.tid,'T')
        # print dir(a)
        s = a.size() if 'size' in dir(a) else ()

        win1 = wx.Frame(self, -1)
        win1.SetSize(s)
        a.main(win1)

    def Toolbar(self):
        self.tb = self.CreateToolBar(wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT)
        Tbd = MT.ToolData()
        Tbl = Tbd.ToolBarList()
        #print(Tbl)
        tsize = (24, 24)
        self.tb.SetToolBitmapSize(tsize)
        for tl in Tbl:
            for t in Tbl[tl]:
                if t[1] == '' or t[1] == None:
                    self.tb.AddSeparator()
                else:
                    #print(t)

                    self.tb.AddTool(t[0], t[1], wx.Bitmap(ICON32_PATH+t[2],wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, t[1], t[3], None)
                    self.Bind(wx.EVT_TOOL, self.OnTool, id=t[0])
            self.tb.AddSeparator()


        self.tb.Realize()


    def ToolPnl(self):
        self.tool = []
        MTBL = MT.ToolData()
        MLT = MTBL.ToolBarList()
        i = 0
        for T in MLT:
            #print(MLT[T])
            MTB = MT.MyToolbar(self)
            MyTL = MTB.data
            #print(MyTL)
            self.tool.append( MTB.CreatTool(MLT[T]) )
            self.tool[i].SetToolBitmapSize(wx.Size(24, 24))
            self.tool[i].Realize()
            self.m_mgr.AddPane(self.tool[i], wx.aui.AuiPaneInfo().Name("tb"+str(i)).Caption("Toolbar").
                           ToolbarPane().Top().LeftDockable(True).RightDockable(False))
            self.Bind(wx.EVT_TOOL_RANGE, self.OnTool, id=self.tool[i].mytb[0].GetId(), id2=self.tool[i].mytb[-1].GetId())
            i += 1

    def APnls(self):
        self.Pnls = []
        ML = PA.MyLstPnl()
        FL = ML.GetAuiPro()
        for P in ML.GetAuiPnl():
            #print(P)
            if P != '__init__.py':
                ii = importlib.import_module('GUI.AuiPanel.'+P[:-3])
                mp = ii.MyPanel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
                self.Pnls.append(mp)

                if P in FL:
                    PInfo = ML.GetAuiInfo(FL[P])

                    if ' Size' in FL[P]:
                        #print(FL[P][5])
                        PInfo.FloatingSize(int(FL[P][5].strip().split(' ')[0]),int(FL[P][5].strip().split(' ')[1]))
                    if ' Layer' in FL[P]:
                        #print(FL[P][7])
                        PInfo.Layer(int(FL[P][7].strip()))
                    self.m_mgr.AddPane(mp,PInfo)

    def Clock(self,TPS):
        #self.owin = wx.Frame(self,-1,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.owin = C1.MyFrame1(self)
        #clockpanel = C1.ClockPanel(self.owin)
        self.owin.SetSize((250,250))
        self.owin.SetPosition((150,100))
        if TPS == 1:
            self.owin.Show()
        elif TPS == 0:
            self.owin.Hide()

    def BGrnd(self,BPS,BGF):
        #self.bmpwin = BG.MyHtmlPanel(self,wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL , BGF)    
        #self.htmlwin = BG.MyHtmlPanel(self,wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
        self.bmpwin = BG.BGPanel(self,BGF)
        self.m_mgr.AddPane( self.bmpwin, wx.aui.AuiPaneInfo() .Right() .Center() .CloseButton( False ).Dock().Resizable().FloatingSize( wx.Size( 800,600 )) )
        #print self.bmpwin.GetSize()
        if BPS == 1 :
            self.m_mgr.GetPane(self.bmpwin).Show()
        elif BPS == 0:
            self.m_mgr.GetPane(self.bmpwin).Hide()
