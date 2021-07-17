# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview as dv

import Database.MenuSet2 as MS

from Config.Init import *
###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        Vsz1 = wx.BoxSizer( wx.VERTICAL )

        Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

        #self.TTC1 = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        #Hsz1.Add( self.TTC1, 1, wx.ALL|wx.EXPAND, 5 )
        self.TTC1 = dv.TreeListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        self.TTC1.AppendColumn(u'ID',wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE)
        self.TTC1.AppendColumn(u'Name', wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE)
        self.TTC1.AppendColumn(u'Help', wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE)
        self.TTC1.AppendColumn(u'Program', wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE)
        Hsz1.Add(self.TTC1, 1, wx.ALL | wx.EXPAND, 5)

        self.MyMenu = MS.GetData(u'Menu2.db', u'')
        self.DoMenu = MS.SetData(u'', u'', u'')

        self.fillitem()

        Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

        Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnadd = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz2.Add( self.btnadd, 0, wx.ALL, 5 )

        self.btnedt = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz2.Add( self.btnedt, 0, wx.ALL, 5 )

        self.btndel = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz2.Add( self.btndel, 0, wx.ALL, 5 )


        Vsz1.Add( Hsz2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( Vsz1 )
        self.Layout()

        # Connect Events
        self.TTC1.Bind( dv.EVT_TREELIST_ITEM_ACTIVATED, self.actitm )
        self.TTC1.Bind(dv.EVT_TREELIST_ITEM_CHECKED, self.actitm)
        self.TTC1.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.rclkitm )
        self.btndel.Bind( wx.EVT_BUTTON, self.deltol )
        self.btnedt.Bind( wx.EVT_BUTTON, self.edttol )
        self.btnadd.Bind( wx.EVT_BUTTON, self.addtol )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def actitm( self, event ):
        self.slctitm = event.GetEventObject().GetItemText(event.GetItem())
        #self.rootitm = event.GetEventObject().GetRootItem()
        #print(self.slctitm)
        #print(self.rootitm)
        for itm in self.altol:
            #print(itm)
            if int(self.slctitm) == itm[0]:
                self.mydata = itm
            #elif self.slctitm == '---'  and itm[1] == None :
            #    self.mydata = itm
        self.edttol(None)
        event.Skip()

    def rclkitm( self, event ):
        event.Skip()

    def deltol( self, event ):
        sitm = self.TTC1.GetItemText(self.TTC1.GetSelections()[0])
        for itm in self.altol:
            if int(sitm) == itm[0]:
                self.mydata = itm
        self.Frm = wx.Frame(self)
        self.Pnl = MyPanel2(self.Frm, self.mydata, u"Delete")
        self.Frm.SetSize((520, 310))
        self.Frm.Show()
        event.Skip()

    def edttol( self, event ):
        self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
        self.Pnl = MyPanel2(self.Frm, self.mydata, u"Edit")
        self.Frm.SetSize((500, 310))
        self.Frm.Show()

    def addtol( self, event ):
        self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
        self.Pnl = MyPanel2(self.Frm, [], u"Add")
        self.Frm.SetSize((500, 310))
        self.Frm.Show()

    def fillitem(self):
        isz = (16, 16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        #fileidx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        #smileidx = il.Add(images.Smiles.GetBitmap())

        self.TTC1.SetImageList(il)
        self.il = il

        #broot = self.TTC1.AddRoot(u'Toolbar')
        root1 = self.TTC1.GetRootItem()
        broot = self.TTC1.AppendItem(root1, u'Tool Bar')

        #self.TTC1.SetItemImage(broot,fldridx,wx.TreeItemIcon_Normal)
        #self.TTC1.SetItemImage(broot,fldropenidx,wx.TreeItemIcon_Expanded)
        self.altol = self.MyMenu.GetAllTB("left join handler on toolbar.handlerid = handler.handlerid \
                                           left join access on toolbar.acclvlid = access.acclvlid")
        dictool = self.regrouptollbar(self.altol)

        for t in dictool:
            gritm = self.TTC1.AppendItem(broot, str(t))
            self.TTC1.SetItemText(gritm, 0, str(t))
            #self.TTC1.SetItemImage(gritm,fldridx,wx.TreeItemIcon_Normal)
            #self.TTC1.SetItemImage(gritm,fldropenidx,wx.TreeItemIcon_Expanded)
            for i in dictool[t]:

                if i[1] == None or i[1] == '':
                    ditm = self.TTC1.AppendItem(gritm,u'---')
                    self.TTC1.SetItemText(ditm , 0, str(i[0]))
                    self.TTC1.SetItemText(ditm, 1, u'---')
                    self.TTC1.SetItemText(ditm, 2, u'---')
                    self.TTC1.SetItemText(ditm, 3, u'---')

                else:
                    slcticn = il.Add(wx.Bitmap(ICON16_PATH+i[2],wx.BITMAP_TYPE_ANY))
                    bitm = self.TTC1.AppendItem(gritm,i[1])
                    self.TTC1.SetItemText(bitm, 0, str(i[0]))
                    self.TTC1.SetItemText(bitm, 1, i[1])
                    self.TTC1.SetItemText(bitm, 2, i[3])
                    self.TTC1.SetItemText(bitm, 3, i[4])
                    self.TTC1.SetItemImage(bitm,fldridx,wx.TreeItemIcon_Normal) # wx.NO_IMAGE
                    self.TTC1.SetItemImage(bitm,slcticn,wx.TreeItemIcon_Selected)
        #self.TTC1.Expand(broot)

    def regrouptollbar(self, tooldata):
        result = {}

        for item in tooldata:
            if item[0]//100 not in result:
                newitm = [(item[0],item[1],item[2],item[3],item[8])]
                result[item[0]//100] = newitm
            else:
                result[item[0]//100].append((item[0],item[1],item[2],item[3],item[8]))
        #print(result)
        return result

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):

    def __init__( self, parent, Data, Button, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 495,276 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        Vsz1 = wx.BoxSizer( wx.VERTICAL )

        Hsz0 = wx.WrapSizer( wx.HORIZONTAL, 0 )

        self.Button = Button
        self.Data = Data
        #print(self.Data)
        if self.Data != []:
            grp = self.Data[0]//100
        else:
            grp = 1



        self.txtg = wx.StaticText( self, wx.ID_ANY, u"Group", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtg.Wrap( -1 )

        Hsz0.Add( self.txtg, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble1 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 10, 1.000000, 1 )
        self.m_spinCtrlDouble1.SetDigits( 0 )
        self.m_spinCtrlDouble1.SetValue(grp)
        Hsz0.Add( self.m_spinCtrlDouble1, 0, wx.ALL, 5 )

        self.txt0 = wx.StaticText( self, wx.ID_ANY, u"Toolbar Id", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt0.Wrap( -1 )

        Hsz0.Add( self.txt0, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld0 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        Hsz0.Add( self.fld0, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.txt1 = wx.StaticText( self, wx.ID_ANY, u"Access id", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt1.Wrap( -1 )

        Hsz0.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        Hsz0.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.btnlst = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        Hsz0.Add( self.btnlst, 0, wx.ALL, 5 )


        Vsz1.Add( Hsz0, 1, wx.EXPAND, 5 )

        Hsz1 = wx.WrapSizer( wx.HORIZONTAL, 0 )

        self.txt2 = wx.StaticText( self, wx.ID_ANY, u"Tool name", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.txt2.Wrap( -1 )

        Hsz1.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz1.Add( self.fld2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"Line", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz1.Add( self.m_checkBox3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

        Hsz2 = wx.WrapSizer( wx.HORIZONTAL, 0 )

        self.txt3 = wx.StaticText( self, wx.ID_ANY, u"Toolbar Icon", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.txt3.Wrap( -1 )

        Hsz2.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.file1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.png;*.bmp;*.jpg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
        Hsz2.Add( self.file1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz2.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )

        Hsz3 = wx.WrapSizer( wx.HORIZONTAL, 0 )

        self.txt4 = wx.StaticText( self, wx.ID_ANY, u"Short text", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.txt4.Wrap( -1 )

        Hsz3.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz3.Add( self.fld3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt5 = wx.StaticText( self, wx.ID_ANY, u"Long text", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt5.Wrap( -1 )

        Hsz3.Add( self.txt5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz3.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )

        Hsz4 = wx.WrapSizer( wx.HORIZONTAL, 0 )

        self.txt6 = wx.StaticText( self, wx.ID_ANY, u"Program", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.txt6.Wrap( -1 )

        Hsz4.Add( self.txt6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.file2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*;*.py", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
        Hsz4.Add( self.file2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.fld5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz4.Add( self.fld5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        Vsz1.Add( Hsz4, 1, wx.EXPAND, 5 )

        Hsz5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.Box1 = wx.CheckBox( self, wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz5.Add( self.Box1, 0, wx.ALL, 5 )

        self.Box2 = wx.CheckBox( self, wx.ID_ANY, u"Hiden", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz5.Add( self.Box2, 0, wx.ALL, 5 )


        Vsz1.Add( Hsz5, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        Hsz6 = wx.WrapSizer( wx.HORIZONTAL, 0 )


        Hsz6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn1 = wx.Button( self, wx.ID_ANY, u"Cancle", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz6.Add( self.btn1, 0, wx.ALL, 5 )

        self.btn2 = wx.Button( self, wx.ID_ANY, Button, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz6.Add( self.btn2, 0, wx.ALL, 5 )


        Vsz1.Add( Hsz6, 0, wx.EXPAND, 5 )


        self.SetSizer( Vsz1 )
        self.Layout()
        if self.Data != []:
            self.filldata()

        # Connect Events
        self.btnlst.Bind( wx.EVT_BUTTON, self.lstid )
        self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.adlin )
        self.file1.Bind( wx.EVT_FILEPICKER_CHANGED, self.icnfil )
        self.file2.Bind( wx.EVT_FILEPICKER_CHANGED, self.prgfil )
        self.Box1.Bind( wx.EVT_CHECKBOX, self.disbl )
        self.Box2.Bind( wx.EVT_CHECKBOX, self.hidn )
        self.btn1.Bind( wx.EVT_BUTTON, self.cncl )
        self.btn2.Bind( wx.EVT_BUTTON, self.Doit )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def filldata(self):
        if self.Data[1] == None:
            self.disallline()
        else:
            self.fld0.SetValue(str(self.Data[0]))
            self.fld1.SetValue(self.Data[6])
            self.fld2.SetValue(self.Data[1])
            self.fld3.SetValue(self.Data[3])
            self.fld4.SetValue(self.Data[4])
            self.fld5.SetValue(self.Data[8])
            if self.Data[14] != 'FFFF':
                self.Box2.SetValue(1)
            if self.Data[15] != 1:
                self.Box1.SetValue(1)
            self.file1.SetPath(ICON32_PATH+self.Data[2])
            self.m_bitmap1.SetBitmap(wx.Bitmap(ICON32_PATH+self.Data[2],wx.BITMAP_TYPE_ANY))

    def disallline(self):
        self.fld0.Disable()
        self.fld1.Disable()
        self.fld2.Disable()
        self.fld3.Disable()
        self.fld4.Disable()
        self.fld5.Disable()
        self.file1.Disable()
        self.file2.Disable()
        self.m_checkBox3.SetValue(1)

    def lstid( self, event ):
        event.Skip()

    def adlin( self, event ):
        self.disallline()

        event.Skip()

    def icnfil( self, event ):
        self.m_bitmap1.SetBitmap(wx.Bitmap(self.file1.GetPath(), wx.BITMAP_TYPE_ANY))
        event.Skip()

    def prgfil( self, event ):
        event.Skip()

    def disbl( self, event ):
        event.Skip()

    def hidn( self, event ):
        event.Skip()

    def cncl( self, event ):
        q = self.GetParent()
        q.Close()

    def Doit( self, event ):
        getdata = MS.GetData(u'Menu2.db',u'')
        setdata = MS.SetData(u'toolbar',u'',u'')
        chkdata = getdata.GetAllTB()
        thsdata = self.getData()
        #print(thsdata)
        if self.Button == "Add":
            if getdata.GetAllTB(u"where toolid = %s "% int(thsdata[0])) != []:
                wx.MessageBox(u"you must use a new code please change id")
            elif int(thsdata[0])//100 != self.m_spinCtrlDouble1.GetValue():
                wx.MessageBox(u"your first number of code must equal with group ")
            else:
                icn = thsdata[6].split("\\")[-1]
                ihd = self.gethandler(thsdata[7].split("\\")[-1].replace(".py",''))

                Data = [int(thsdata[0]), thsdata[2], icn, thsdata[3], thsdata[4], ihd, thsdata[1]]
                setdata.Additem(u'toolid, toolname, toolicon, shrttxt, lngtxt, handlerid, acclvlid',Data)
                setdata.Table = u'access'
                if thsdata[8]:
                    disen = 0
                else:
                    disen = 1
                if thsdata[9]:
                    shwid = '0000'
                else:
                    shwid = 'FFFF'
                Data2 = [thsdata[1], 1, shwid, disen]
                setdata.Additem(u'acclvlid, userid, acclvl, disenable',Data2)
                wx.MessageBox(u"successful add Toolbar to program")

                self.AddTool(thsdata)

                ml = self.GetGrandParent()
                ml.TTC1.DeleteAllItems()
                ml.fillitem()
                ml.Refresh()

                q = self.GetParent()
                q.Close()

        elif self.Button == u"Edit":
            icn = thsdata[6].split("\\")[-1]
            ihd = self.gethandler(thsdata[7].split("\\")[-1].replace(".py", ''))
            Data3 = [thsdata[2], icn , thsdata[3], thsdata[4], ihd, thsdata[1]]
            setdata.Upditem(u'toolname = ? , toolicon = ? , shrttxt = ? , lngtxt = ? , handlerid = ? , acclvlid = ? where  toolid = %d '% int(thsdata[0]), Data3)
            if thsdata[8]:
                disen = 0
            else:
                disen = 1
            if thsdata[9]:
                shwid = '0000'
            else:
                shwid = 'FFFF'
            Data4 = [1, shwid, disen]
            setdata.Table = u'access'
            setdata.Upditem(u'userid = ? , acclvl = ?, disenable = ? where acclvlid = "%s" '% thsdata[1], Data4)
            ml = self.GetGrandParent()
            ml.TTC1.DeleteAllItems()
            ml.fillitem()
            ml.Refresh()
            q = self.GetParent()
            q.Close()


        elif self.Button == u"Delete":
            setdata.Delitem(u"toolbar.toolid = %d "% int(thsdata[0]))
            setdata.Table = u"access"
            setdata.Delitem(u'access.acclvlid = "%s" ' % thsdata[1])
            ml = self.GetGrandParent()
            ml.TTC1.DeleteAllItems()
            ml.fillitem()
            ml.Refresh()
            self.DelTool(thsdata)
            q = self.GetParent()
            q.Close()


        else:
            wx.MessageBox(u'some error here')
            print(u'some error here')
        event.Skip()

    def getData(self):
        D0 = self.fld0.GetValue()
        D1 = self.fld1.GetValue()
        D2 = self.fld2.GetValue()
        D3 = self.fld3.GetValue()
        D4 = self.fld4.GetValue()
        D5 = self.fld5.GetValue()
        D6 = self.file1.GetPath()
        D7 = self.file2.GetPath()
        D8 = self.Box1.GetValue()
        D9 = self.Box2.GetValue()
        return [D0,D1,D2,D3,D4,D5,D6,D7,D8,D9]

    def gethandler(self, prg):
        #print(prg)
        getdata = MS.GetData(u'Menu2.db', u'')
        if prg == '':
            return 10001
        hdrid,mbrid = getdata.getHndlr(prg)[0]

        #print(hdrid,mbrid)
        mdir = getdata.gethddir(mbrid)
        #print(mdir)
        return int(hdrid)

    def AddTool(self, D):
        mw = self.FindWindowByName('main')
        tb = mw.GetToolBar()

        ppos = tb.GetToolPos(int(D[0])-1)
        #print(ppos)
        if ppos != -1:
            tb.InsertTool(ppos+1, int(D[0]), str(D[2]), wx.Bitmap(D[6]), wx.NullBitmap, wx.ITEM_NORMAL, str(D[3]), str(D[4]) )
            #tb.InsertTool(ppos, int(D[0]), str(D[2]), wx.Bitmap(D[6]), wx.NullBitmap, wx.ITEM_NORMAL)

        else:
            tb.AddTool(int(D[0]), str(D[2]), wx.Bitmap(D[6]), wx.NullBitmap, wx.ITEM_NORMAL, str(D[3]), str(D[4]) )
        tb.Realize()



    def DelTool(self, D):
         mw = self.FindWindowByName('main')
         tb = mw.GetToolBar()
         tb.DeleteTool(int(D[0]))
