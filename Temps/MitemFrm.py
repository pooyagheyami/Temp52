# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from AI.OpnFil import *
from AI.Analiz import *

from Config.Init import *

import Database.MenuSet2 as MS
import GUI.proman as pro
import importlib


###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1(wx.Panel):

    def __init__(self, parent, Data=[], Button=u'', id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(700, 360),
                 style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        self.Data = Data
        print(Data)
        self.Button = Button
        self.getMData = MS.GetData(u'Menu2.db', u'')
        self.setMDate = MS.SetData(u'', u'', u'')

        Vz1 = wx.BoxSizer(wx.VERTICAL)

        self.SP1 = wx.SplitterWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D)
        self.SP1.Bind(wx.EVT_IDLE, self.SP1OnIdle)

        self.P1 = wx.Panel(self.SP1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_RAISED | wx.TAB_TRAVERSAL)
        Vzp1 = wx.BoxSizer(wx.VERTICAL)

        Hzp1 = wx.WrapSizer(wx.HORIZONTAL, 0)

        if Data != []:
            self.barname = self.getMData.gBarN(Data[0])[0][0]
            self.C = self.barname[0]
        else:
            self.barname = u''
            self.C = 'P'

        self.title = wx.StaticText(self.P1, wx.ID_ANY, u"Menu Bar: " + self.barname, wx.DefaultPosition, wx.DefaultSize,
                                   0)
        self.title.Wrap(-1)

        Hzp1.Add(self.title, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt1a = wx.StaticText(self.P1, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.txt1a.Wrap(-1)

        Hzp1.Add(self.txt1a, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld0 = wx.TextCtrl(self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, -1), 0)
        Hzp1.Add(self.fld0, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt1b = wx.StaticText(self.P1, wx.ID_ANY, u"Access", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt1b.Wrap(-1)

        Hzp1.Add(self.txt1b, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld1 = wx.TextCtrl(self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        Hzp1.Add(self.fld1, 0, wx.ALL, 5)

        self.btnsrc = wx.Button(self.P1, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        Hzp1.Add(self.btnsrc, 0, wx.ALL, 5)

        Vzp1.Add(Hzp1, 0, wx.EXPAND, 5)

        Hzp2 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.txt2 = wx.StaticText(self.P1, wx.ID_ANY, u"Label", wx.DefaultPosition, wx.Size(70, -1), 0)
        self.txt2.Wrap(-1)

        Hzp2.Add(self.txt2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld2 = wx.TextCtrl(self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp2.Add(self.fld2, 1, wx.ALL, 5)

        Vzp1.Add(Hzp2, 0, wx.EXPAND, 5)

        Hzp3 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.txt3 = wx.StaticText(self.P1, wx.ID_ANY, u"Icon", wx.DefaultPosition, wx.Size(70, -1), 0)
        self.txt3.Wrap(-1)

        Hzp3.Add(self.txt3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld3 = wx.FilePickerCtrl(self.P1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.png;*.bmp;*.jpg",
                                      wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE | wx.FLP_SMALL)
        Hzp3.Add(self.fld3, 1, wx.ALL, 5)

        # self.fld3 = wx.TextCtrl( self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        # Hzp3.Add( self.fld3, 1, wx.ALL, 5 )

        # self.btnIcn = wx.Button( self.P1, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        # Hzp3.Add( self.btnIcn, 0, wx.ALL, 5 )

        Vzp1.Add(Hzp3, 0, wx.EXPAND, 5)

        Hzp31 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.icon = wx.StaticBitmap(self.P1, wx.ID_ANY, wx.Bitmap(ICONS_PATH + u"image.png", wx.BITMAP_TYPE_ANY),
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp31.Add(self.icon, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        Vzp1.Add(Hzp31, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        Hzp4 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.txt4 = wx.StaticText(self.P1, wx.ID_ANY, u"Shorcut", wx.DefaultPosition, wx.Size(70, -1), 0)
        self.txt4.Wrap(-1)

        Hzp4.Add(self.txt4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld4 = wx.TextCtrl(self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp4.Add(self.fld4, 1, wx.ALL, 5)

        Vzp1.Add(Hzp4, 0, wx.EXPAND, 5)

        Hzp5 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.txt5 = wx.StaticText(self.P1, wx.ID_ANY, u"Help String", wx.DefaultPosition, wx.Size(70, -1), 0)
        self.txt5.Wrap(-1)

        Hzp5.Add(self.txt5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld5 = wx.TextCtrl(self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp5.Add(self.fld5, 1, wx.ALL, 5)

        Vzp1.Add(Hzp5, 0, wx.EXPAND, 5)

        Hzp6 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.txt6 = wx.StaticText(self.P1, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.Size(70, -1), 0)
        self.txt6.Wrap(-1)

        Hzp6.Add(self.txt6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld6 = wx.TextCtrl(self.P1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp6.Add(self.fld6, 1, wx.ALL, 5)

        Vzp1.Add(Hzp6, 0, wx.EXPAND, 5)

        Hzp7 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.txt7 = wx.StaticText(self.P1, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.Size(50, -1), 0)
        self.txt7.Wrap(-1)

        Hzp7.Add(self.txt7, 0, wx.ALL, 5)

        self.rBtn1 = wx.RadioButton(self.P1, wx.ID_ANY, u"Normal", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp7.Add(self.rBtn1, 0, wx.ALL, 5)

        self.rBtn2 = wx.RadioButton(self.P1, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp7.Add(self.rBtn2, 0, wx.ALL, 5)

        self.rBtn3 = wx.RadioButton(self.P1, wx.ID_ANY, u"Radio", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp7.Add(self.rBtn3, 0, wx.ALL, 5)

        self.rBtn4 = wx.RadioButton(self.P1, wx.ID_ANY, u"SubMenu", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp7.Add(self.rBtn4, 0, wx.ALL, 5)

        Vzp1.Add(Hzp7, 0, wx.EXPAND, 5)

        Hzp71 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.cBox1 = wx.CheckBox(self.P1, wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp71.Add(self.cBox1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.cBox2 = wx.CheckBox(self.P1, wx.ID_ANY, u"Hidden", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp71.Add(self.cBox2, 0, wx.ALL, 5)

        Vzp1.Add(Hzp71, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.P1.SetSizer(Vzp1)
        self.P1.Layout()
        Vzp1.Fit(self.P1)
        self.P2 = wx.Panel(self.SP1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_RAISED | wx.TAB_TRAVERSAL)
        Vzp2 = wx.BoxSizer(wx.VERTICAL)

        Hzp8 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.txt8 = wx.StaticText(self.P2, wx.ID_ANY, u"Program to DO", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt8.Wrap(-1)

        Hzp8.Add(self.txt8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.file1 = wx.FilePickerCtrl(self.P2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.py",
                                       wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE | wx.FLP_SMALL)
        Hzp8.Add(self.file1, 1, wx.ALL, 5)

        Vzp2.Add(Hzp8, 0, wx.EXPAND, 5)

        Hzp9 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.Doprgitm = wx.TextCtrl(self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp9.Add(self.Doprgitm, 1, wx.ALL, 5)

        self.pykan = wx.StaticText(self.P2,wx.ID_ANY,u"=>",wx.DefaultPosition,wx.DefaultSize,0)
        Hzp9.Add(self.pykan, 0, wx.ALL,5)

        self.Dsfilitm = wx.TextCtrl(self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp9.Add(self.Dsfilitm, 1, wx.ALL, 5)

        Vzp2.Add(Hzp9, 0, wx.EXPAND, 5)

        Hzp10 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.btn1 = wx.Button(self.P2, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp10.Add(self.btn1, 0, wx.ALL, 5)

        self.btn2 = wx.Button(self.P2, wx.ID_ANY, u"Open File", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp10.Add(self.btn2, 0, wx.ALL, 5)

        self.btn3 = wx.Button(self.P2, wx.ID_ANY, u"New...", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp10.Add(self.btn3, 0, wx.ALL, 5)

        Vzp2.Add(Hzp10, 0, wx.EXPAND, 5)

        Hzp11 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.btn4 = wx.Button(self.P2, wx.ID_ANY, u"Analiz...", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp11.Add(self.btn4, 0, wx.ALL, 5)

        self.btn5 = wx.Button(self.P2, wx.ID_ANY, u"Parse...", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp11.Add(self.btn5, 0, wx.ALL, 5)

        self.btn6 = wx.Button(self.P2, wx.ID_ANY, u"Generate1", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp11.Add(self.btn6, 0, wx.ALL, 5)

        Vzp2.Add(Hzp11, 0, wx.EXPAND, 5)

        Hzpl = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.line1 = wx.StaticLine(self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        Hzpl.Add(self.line1, 1, wx.EXPAND | wx.ALL, 5)

        Vzp2.Add(Hzpl, 0, wx.EXPAND, 5)

        Hzp12 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.txt9 = wx.StaticText(self.P2, wx.ID_ANY, u"Select Database", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt9.Wrap(-1)

        Hzp12.Add(self.txt9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.dir1 = wx.DirPickerCtrl(self.P2, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                     wx.DefaultSize, wx.DIRP_DEFAULT_STYLE | wx.DIRP_SMALL)
        Hzp12.Add(self.dir1, 1, wx.ALL, 5)

        Vzp2.Add(Hzp12, 0, wx.EXPAND, 5)

        Hzp13 = wx.WrapSizer(wx.HORIZONTAL, 0)

        self.txt10 = wx.StaticText(self.P2, wx.ID_ANY, u"Tabels and Fields", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt10.Wrap(-1)

        Hzp13.Add(self.txt10, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        Lbox1Choices = []
        self.Lbox1 = wx.ListBox(self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Lbox1Choices, 0)
        Hzp13.Add(self.Lbox1, 1, wx.ALL, 5)

        Vzp2.Add(Hzp13, 0, wx.EXPAND, 5)

        Hzp14 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.btn7 = wx.Button(self.P2, wx.ID_ANY, u"Analiz...", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp14.Add(self.btn7, 0, wx.ALL, 5)

        self.btn8 = wx.Button(self.P2, wx.ID_ANY, u"Parse...", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp14.Add(self.btn8, 0, wx.ALL, 5)

        self.btn9 = wx.Button(self.P2, wx.ID_ANY, u"Generate2", wx.DefaultPosition, wx.DefaultSize, 0)
        Hzp14.Add(self.btn9, 0, wx.ALL, 5)

        Vzp2.Add(Hzp14, 1, wx.EXPAND, 5)

        self.P2.SetSizer(Vzp2)
        self.P2.Layout()
        Vzp2.Fit(self.P2)
        self.SP1.SplitVertically(self.P1, self.P2, 349)
        Vz1.Add(self.SP1, 1, wx.EXPAND, 5)

        Hz1 = wx.BoxSizer(wx.HORIZONTAL)

        self.btnA = wx.Button(self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0)
        Hz1.Add(self.btnA, 0, wx.ALL, 5)

        self.btnS = wx.Button(self, wx.ID_ANY, u"Save ", wx.DefaultPosition, wx.DefaultSize, 0)
        Hz1.Add(self.btnS, 0, wx.ALL, 5)

        self.btnR = wx.Button(self, wx.ID_ANY, u"Report", wx.DefaultPosition, wx.DefaultSize, 0)
        Hz1.Add(self.btnR, 0, wx.ALL, 5)

        Vz1.Add(Hz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        if self.Button == 'UpDate' or self.Button == 'Delete':
            self.putData(self.Data)

        self.SetSizer(Vz1)
        self.Layout()

        # Connect Events
        # self.btnIcn.Bind( wx.EVT_BUTTON, self.opnicn )
        self.btnsrc.Bind(wx.EVT_BUTTON, self.lstid)
        self.fld3.Bind(wx.EVT_FILEPICKER_CHANGED, self.shwicn)

        self.rBtn1.Bind(wx.EVT_RADIOBUTTON, self.typitm)
        self.rBtn2.Bind(wx.EVT_RADIOBUTTON, self.typitm)
        self.rBtn3.Bind(wx.EVT_RADIOBUTTON, self.typitm)
        self.rBtn4.Bind(wx.EVT_RADIOBUTTON, self.typitm)
        self.cBox1.Bind(wx.EVT_CHECKBOX, self.disitm)
        self.cBox2.Bind(wx.EVT_CHECKBOX, self.hiditm)
        self.file1.Bind(wx.EVT_FILEPICKER_CHANGED, self.chngfil)
        self.btn1.Bind(wx.EVT_BUTTON, self.prvw)
        self.btn2.Bind(wx.EVT_BUTTON, self.opnfil)
        self.btn3.Bind(wx.EVT_BUTTON, self.newfil)
        self.btn4.Bind(wx.EVT_BUTTON, self.anliz1)
        self.btn5.Bind(wx.EVT_BUTTON, self.pars1)
        self.btn6.Bind(wx.EVT_BUTTON, self.gnrt1)
        self.dir1.Bind(wx.EVT_DIRPICKER_CHANGED, self.dbfil)
        self.Lbox1.Bind(wx.EVT_LISTBOX, self.tblfld)
        self.btn7.Bind(wx.EVT_BUTTON, self.anliz2)
        self.btn8.Bind(wx.EVT_BUTTON, self.pars2)
        self.btn9.Bind(wx.EVT_BUTTON, self.gnrt2)
        self.btnA.Bind(wx.EVT_BUTTON, self.Aply)
        self.btnS.Bind(wx.EVT_BUTTON, self.Save)
        self.btnR.Bind(wx.EVT_BUTTON, self.Rprt)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    # def opnicn( self, event ):
    def putData(self, Data):
        # print(Data)
        self.fld0.SetValue(str(Data[1]))
        if self.Data[11] != None:
            self.fld1.SetValue(Data[11])
        if Data[2] == None:
            self.fld2.SetValue(u'Separator')
        else:
            self.fld2.SetValue(Data[2])
        if Data[8] != None:
            self.fld3.SetPath(ICON16_PATH + Data[8])
        if Data[9] != None:
            self.fld4.SetValue(Data[9])
        if Data[10] != None:
            self.fld5.SetValue(Data[10])
        if Data[7] != None:
            self.fld6.SetValue(Data[7])
        if Data[3] == 'N':
            self.rBtn1.SetValue(True)
        elif Data[3] == 'C':
            self.rBtn2.SetValue(True)
        elif Data[3] == 'R':
            self.rBtn3.SetValue(True)
        elif Data[3] == 'S':
            self.rBtn4.SetValue(True)
        else:
            pass
        if Data[16] != None and Data[16] != 1:
            self.cBox1.SetValue(True)
        if Data[15] != None and Data[15] == '0000':
            self.cBox2.SetValue(True)

        if Data[18] != '':
            self.Doprgitm.SetValue(Data[18])
        if Data[19] != '' and Data[19] == '100':
            self.file1.SetPath(GUI_PATH+'Temp\\'+Data[18]+'.py')

        self.Update()

    # self.Layout()

    def lstid(self, event):
        event.Skip()

    def shwicn(self, event):
        self.icon.SetBitmap(wx.Bitmap(self.fld3.GetPath(), wx.BITMAP_TYPE_ANY))
        event.Skip()

    def typitm(self, event):
        event.Skip()

    def disitm(self, event):
        event.Skip()

    def hiditm(self, event):
        event.Skip()

    def chngfil(self, event):
        ifile = self.file1.GetPath()
        self.Doprgitm.SetValue(ifile.replace(GUI_PATH,'')[:-3].replace('\\','.'))
        #event.Skip()

    def prvw(self, event):
        #print(self.file1.GetPath())
        #print(self.Doprgitm.GetValue())
        i = self.file1.GetPath()
        i1 = i.replace(GUI_PATH,'GUI.')
        i2 = i1.replace('\\','.')
        i3 = i2.replace(i[-3:],'')
        #print(i3)
        a = importlib.import_module(i3)
        #s = a.size() if 'size' in dir(a) else ()
        win1 = wx.Frame(self, -1)
        #win1.SetSize(s)
        a.main(win1)

        event.Skip()

    def opnfil(self, event):
        print(self.file1.GetPath())

        self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
        self.Pnl = PyPanel(self.Frm,self.file1.GetPath())
        self.Frm.SetSize((700, 560))
        self.Frm.Show()
        #event.Skip()

    def newfil(self, event):
        event.Skip()

    def anliz1(self, event):
        ial = Anlzfil(self.file1.GetPath())
        ial.parsefil()
        ial.showParse()
        self.Dsfilitm.SetValue(ial.getGUIfil())
        event.Skip()

    def pars1(self, event):
        event.Skip()

    def gnrt1(self, event):
        event.Skip()

    def dbfil(self, event):
        event.Skip()

    def tblfld(self, event):
        event.Skip()

    def anliz2(self, event):
        event.Skip()

    def pars2(self, event):
        event.Skip()

    def gnrt2(self, event):
        event.Skip()

    def Aply(self, event):
        D = self.getfild()
        #print(D)
        #print(self.Data)
        extid = D[0][0] + D[0][-1] + D[7] + self.C + D[2][0] + D[0][1:]
        if self.Doprgitm == '':
            hndid = 10001
        else:
            hndid = self.getHandel(self.Doprgitm.GetValue(),self.file1.GetPath())
        print(hndid)
        Dsri1 = [self.Data[0], int(D[0]), D[2], D[7], extid, hndid]
        Dsri2 = [extid, D[6], D[3].replace(ICON16_PATH, ''), D[4], D[5], D[1], 1]
        if D[8]:
            dn = 0
        else:
            dn = 1
        if D[9]:
            sh = '0000'
        else:
            sh = 'FFFF'
        Dsri3 = [D[1], 1, sh, dn]
        # print(self.Data)
        # print(Dsri1)
        self.setMDate.Table = u'mitem'
        if self.Button == 'AddNew':
            self.setMDate.Additem(u'mbarid, itemid, itemname, itemtyp, extid, handlerid ', Dsri1)
        elif self.Button == 'UpDate':
            self.setMDate.Upditem(u'itemname = ?, itemtyp = ? , handlerid = ?  where itemid = %d'% self.Data[1] ,[D[2], D[7],hndid])
            #print('write it')
        elif self.Button == 'Delete':
            self.setMDate.Delitem(u'mitem.itemid = %d'% self.Data[1])

        self.setMDate.Table = u'extended'
        if self.Button == 'AddNew':
            self.setMDate.Additem(u'extid, status, icon, shortcut, help, acclvlid, grpid', Dsri2)
        elif self.Button == 'UpDate':
            self.setMDate.Upditem(u'status = ?, icon = ?, shortcut = ? , help = ?  where extid = "%s" '% self.Data[4],[D[6], D[3].replace(ICON16_PATH, ''), D[4], D[5]])
            #print('write it')
        elif self.Button == 'Delete':
            self.setMDate.Delitem(u'extended.extid = "%s"'% self.Data[4])

        self.setMDate.Table = u'access'
        if self.Button == 'AddNew':
            self.setMDate.Additem(u'acclvlid, userid, acclvl, disenable', Dsri3)
            self.Add2Menu(D)
        elif self.Button == 'UpDate':
            self.setMDate.Upditem(u'acclvl = ? , disenable = ?  where acclvlid = "%s" ' % self.Data[11] , [sh, dn])
            self.ChngMnu(D)
            #print('write it')
        elif self.Button == 'Delete':
            self.setMDate.Delitem(u'access.acclvlid = "%s"'% self.Data[11])
            self.delmenu()

        wx.MessageBox(u'request apply, you can change or add program later. ')

        #self.Add2Menu(D)

        ml = self.GetGrandParent()
        ml.TLCtrl1.DeleteAllItems()
        ml.fillList()
        ml.Refresh()
        #print(dir(self.GetGrandParent()))
        q = self.GetParent()
        q.Close()

    # event.Skip()
    def Add2Menu(self, D):
        mw = self.FindWindowByName('main')
        mb = mw.GetMenuBar()
        lmb = mb.GetMenus()
        for l in lmb:
            if self.barname in l:
                mbc = l[0]
                if D[7] == 'S':
                    mbc.AppendSubMenu(wx.Menu(), D[2], D[5])
                    break
                if D[7] == 'C':
                    mtyp = wx.ITEM_CHECK
                elif D[7] == 'R':
                    mtyp = wx.ITEM_RADIO
                else:
                    mtyp = wx.ITEM_NORMAL
                if D[4] != None or D[4] != '':
                    nm = D[2] + '\t' + D[4]
                else:
                    nm = D[2]
                mbc.Append(int(D[0]), nm, D[5], mtyp)
                if D[3] != '':
                    mbcitm = mbc.FindItemById(int(D[0]))
                    mbcitm.SetBitmap(wx.Bitmap(D[3], wx.BITMAP_TYPE_ANY))

    def ChngMnu(self, D):
        mw = self.FindWindowByName('main')
        mb = mw.GetMenuBar()
        lmb = mb.GetMenus()
        for l in lmb:
            if self.barname in l:
                mbc = l[0]
                itmchg = mbc.FindItemById(self.Data[1])
                #print(D)
                #print(dir(itmchg))
                if D[7] == 'S':
                    itmchg.SetSubMenu(wx.Menu(),D[2])
                if D[4] != '':
                    lbl = D[2] + '\t' + D[4]
                else:
                    lbl = D[2]
                itmchg.SetItemLabel(lbl)
                if D[3] != '':
                    itmchg.SetBitmap(wx.Bitmap(D[3], wx.BITMAP_TYPE_ANY))
                if D[6] != '':
                    itmchg.SetHelp(D[6])
                itmchg.Enable(not D[8])

    def delmenu(self):
        mw = self.FindWindowByName('main')
        mb = mw.GetMenuBar()
        lmb = mb.GetMenus()
        for l in lmb:
            print(l)
            if self.barname in l:
                itms = l[0].GetMenuItems()
                print(dir(itms[-1]))
                for i in itms:
                    print(i.GetId())
                    if i.IsSeparator() and self.Data[2] == u'Separator':

                        i.Destroy()

                    elif i.GetId() == self.Data[1]:
                        l[0].RemoveItem(self.Data[1])
                    else:
                        print(i)

    def getHandel(self, imodel, pathfile):
        pr = self.getMData.AllHndl()
        m = imodel.split('.')[1]
        for p in pr:
            if m in p:
                return p[0]
        return m


    def Save(self, event):
        event.Skip()

    def Rprt(self, event):
        event.Skip()

    def SP1OnIdle(self, event):
        self.SP1.SetSashPosition(349)
        self.SP1.Unbind(wx.EVT_IDLE)

    def getfild(self):
        Data0 = self.fld0.GetValue()
        Data1 = self.fld1.GetValue()
        Data2 = self.fld2.GetValue()
        Data3 = self.fld3.GetPath()
        Data4 = self.fld4.GetValue()
        Data5 = self.fld5.GetValue()
        Data6 = self.fld6.GetValue()
        if self.rBtn1.GetValue():
            Data7 = 'N'
        elif self.rBtn2.GetValue():
            Data7 = 'C'
        elif self.rBtn3.GetValue():
            Data7 = 'R'
        elif self.rBtn4.GetValue():
            Data7 = 'S'
        else:
            Data7 = ''
        Data8 = self.cBox1.GetValue()
        Data9 = self.cBox2.GetValue()
        return [Data0, Data1, Data2, Data3, Data4, Data5, Data6, Data7, Data8, Data9]

