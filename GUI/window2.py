# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wx
import wx.aui
#import wx.html
#import wx.dataview
import time

from AI.WinDev import MWC

import GUI.MainMenu2 as MM
import GUI.MainTool as MT
import GUI.AuiPanel.PAui as PA
import importlib
import GUI.BG2 as BG

#import Utility.eCalClak1 as C1
#import Utility.DigitClack as DgK
#import Utility.user as user
from Config.Init import *

import GUI.proman as pro

_ = wx.GetTranslation


class MainWin(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title=u'main',size=(1920,1200),name=u'main')

        # Get Program Config ===================


        self.config = wx.GetApp().GetConfig()

        wx.SystemOptions.SetOption("msw.remap", "0")

        label = self.config.Read(u'Winname')
        self.SetLabel(label)
        #self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        #STBT = 'B'
        #AuiCenter = 'A'
        fntis = self.config.Read(u'Font').split(',')
        #print(fntis)
        if fntis[4] == 'True':
            undr = True
        else:
            undr = False

        #info = wx.NativeFontInfo()
        #info.FromUserString(self.config.Read(u'Font'))
        #ifont = wx.Font(info)
        #print(ifont.FaceName)
        ifont = wx.Font(int(fntis[0]), int(fntis[1]), int(fntis[2]), int(fntis[3]), undr, faceName=fntis[5])
        self.SetFont(ifont)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        # If like Back Gorund or Aui Center =============================
        if eval(self.config.Read('BGActive')):
            self.BGrnd(self.config.Read('Background'))


        # Menu of Program==============
        if self.config.Read("Menu") == '1':
            self.menu = MM.AppMenu()
            if len(self.menu.GetMenus()) != 0:
                #self.SetMenuBar(menu)
                self.UpdateMenu(self.menu, self.menu.GetMenus())

            if self.config.Read('Toolbar') == '1':
                self.Toolbar()
                TBBG = self.config.Read("TBGColor").split(',')[1]
                self.tb.SetBackgroundColour(wx.SystemSettings.GetColour(int(TBBG)))
            elif self.config.Read('Toolbar') == '2':
                self.ToolPnl()

            self.MakeStatus()


        STBG = self.config.Read("SBGColor").split(',')[1]
        self.GetStatusBar().SetBackgroundColour(wx.SystemSettings.GetColour(int(STBG)))

        # All Panel Aui=======================
        self.APnls2()

        #self.BGrnd(BakGrnd)
        self.Bind(wx.EVT_RIGHT_DOWN, self.domouse)
        self.Bind(wx.EVT_CONTEXT_MENU, self.setmenu)

        self.m_mgr.Update()
        self.Centre(wx.BOTH)

    def __del__(self):
        self.timer.Stop()
        self.m_mgr.UnInit()

    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime("%I:%M:%S", t)
        self.SetStatusText(st, self.stnbr)

    def MakeStatus(self):
        lststat = eval(self.config.Read('Status'))
        i = 1
        Wthlst = [-1]

        statusBar = self.CreateStatusBar(len(lststat) + 1,
                                         wx.STB_ELLIPSIZE_END | wx.STB_ELLIPSIZE_MIDDLE | wx.STB_SHOW_TIPS | wx.STB_SIZEGRIP,
                                         wx.ID_ANY)
        # statusBar.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))
        for st in lststat:
            if st == 'time':
                # Timer in status ============================================
                self.timer = wx.PyTimer(self.Notify)
                self.timer.Start(1000)
                Wthlst.append(90)
            elif st == 'date':
                t = time.localtime(time.time())
                self.SetStatusText(time.strftime("%d-%b-%Y", t), i)
                Wthlst.append(90)
            else:
                self.SetStatusText(st, i)
                Wthlst.append(-1)
            i += 1
        self.SetStatusBar(statusBar)
        #print(Wthlst)
        self.stnbr = len(Wthlst) - 1
        self.SetStatusWidths(Wthlst)
        self.SetStatusBarPane(0)
        if 'time' in lststat:
            self.Notify()


    def domouse(self, event):
        self.setmenu(event)

    def setmenu(self, event):
        self.MnuDic = {1: [_(u'Menu Change'), 9999], 2: [_(u'Toolbar Change'), 9998], 3: [_(u'Panes Change'), 9997], 4: [u'', 0],
                       5: [_(u'Databases...'), 9996], 6: [_(u'Programs...'), 9995], 7: [_(u'Add Tools...'), 9994], 8: [u'', 0],
                       9: [_(u'ML Design...'), 9993], 10: [u'', 0], 11: [_(u'Settings...'), 9992]}
        self.m1 = wx.Menu()

        self.itms = []
        i = 0
        for itm in self.MnuDic:
            self.Bind(wx.EVT_MENU, self.OnPopupOne, id=itm)
            if self.MnuDic[itm][0] == u'':
                self.m1.AppendSeparator()
            else:
                # self.itms.append( wx.MenuItem(self.m1, wx.ID_ANY, MnuDic[itm][0], wx.EmptyString) )
                self.m1.Append(itm, self.MnuDic[itm][0])
                # self.m1.Append(itm, self.itms[i])
                #self.Bind(wx.EVT_MENU, self.OnPopupOne, id=MnuDic[itm][1])
                i = i + 1

        self.PopupMenu(self.m1)
        self.m1.Destroy()

    def OnPopupOne(self, event):
        # print(event,event.GetId())
        pmid = event.GetId()
        #a = pro.DoProgram(self.MnuDic[pmid][1], 'A')
        a = pro.DoProgram2(self.MnuDic[pmid][1], '')
        #s = a.size() if 'size' in dir(a) else ()
        win1 = wx.Frame(self, -1)
        #win1.SetSize(s)
        a.main(win1)

    def OnMenu(self, event):
        self.mid = event.GetId()
        # print( self.mid )
        #a = pro.DoProgram(self.mid, 'M')
        a = pro.DoProgram2(self.mid, '')
        # print dir(a)
        #s = a.size() if 'size' in dir(a) else ()
        win1 = wx.Frame(self, -1)
        #win1.SetSize(s)
        a.main(win1)

    def OnTool(self, event):
        self.tid = event.GetId()
        # print( self.tid )
        #a = pro.DoProgram(self.tid, 'T')
        a = pro.DoProgram2(self.tid, '')
        # print dir(a)
        #s = a.size() if 'size' in dir(a) else ()
        win1 = wx.Frame(self, -1)
        #win1.SetSize(s)
        a.main(win1)

    def Toolbar(self):
        self.tb = self.CreateToolBar(wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT|wx.TB_TEXT)
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

                    self.tb.AddTool(t[0], t[1], wx.Bitmap(ICONS_TOOL+t[2],wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, t[1], t[3], None)
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
            MTB = MT.MyAuiToolbar(self)
            MyTL = MTB.data
            #print(MyTL)
            self.tool.append( MTB.CreatTool(MLT[T]) )
            self.tool[i].SetToolBitmapSize(wx.Size(24, 24))
            self.tool[i].Realize()
            self.m_mgr.AddPane(self.tool[i], wx.aui.AuiPaneInfo().Name("tb"+str(i)).Caption("Toolbar").
                           ToolbarPane().Top().LeftDockable(True).RightDockable(False))
            self.Bind(wx.EVT_TOOL_RANGE, self.OnTool, id=self.tool[i].mytb[0].GetId(), id2=self.tool[i].mytb[-1].GetId())
            i += 1


    def APnls2(self):
        self.Pnls = []
        ML = PA.MyLstPnl2()

        for pnl in ML.lstpnl:
            if pnl[1]+'.py' in ML.GetAuiPnl():
                ii = importlib.import_module('GUI.AuiPanel.' + pnl[1])
                mp = ii.MyPanel1(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
                self.Pnls.append(mp)
                PInfo = ML.GetAuiInfo(pnl[1])
                self.m_mgr.AddPane(mp, PInfo)

    def BGrnd(self,BGF):
        self.bmpwin = BG.BGPanel(self,BGF)
        self.m_mgr.AddPane( self.bmpwin, wx.aui.AuiPaneInfo() .CaptionVisible( False ) .Center() .CloseButton( False ).Dock().Resizable().FloatingSize( wx.Size( 800,600 )) )

    def NewMenu(self):
        self.barMenu = wx.MenuBar()
        self.SetMenuBar(self.barMenu)
        return self.barMenu

    def UpdateMenu(self,imenu,menu):
        self.SetMenuBar(imenu)

        frstitm = menu[0][0].GetMenuItems()
        lastitm = menu[-1][0].GetMenuItems()
        if len(frstitm) != 0:
            h = frstitm[0].GetId()
            #h1 = lastitm[-1].GetId()
            #print(h,h1)
            #self.Bind(wx.EVT_MENU_RANGE, self.OnMenu, id=h1, id2=h.GetId())
            self.Bind(wx.EVT_MENU_RANGE, self.OnMenu, id=101, id2=9999)

    def NewToolBar(self):
        self.toolbar = MT.MyToolbar()
        self.SetToolBar()
