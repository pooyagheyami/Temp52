# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import wx.stc as stc

import Database.MenuSet2 as MS
from . import MitemFrm2 as MF

from Config.Init import *

_ = wx.GetTranslation

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 646,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        Vsz1 = wx.BoxSizer( wx.VERTICAL )

        self.Spw1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3DSASH|wx.SP_NO_XP_THEME )
        self.Spw1.Bind( wx.EVT_IDLE, self.Spw1OnIdle )

        self.pnl1 = wx.Panel( self.Spw1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Vsz2 = wx.BoxSizer( wx.VERTICAL )

        self.TLCtrl1 = wx.dataview.TreeListCtrl( self.pnl1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,wx.dataview.TL_CHECKBOX|wx.dataview.TL_DEFAULT_STYLE|wx.dataview.TL_MULTIPLE )
        self.TLCtrl1.AppendColumn( _(u"ID"), wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
        self.TLCtrl1.AppendColumn( _(u"Name"), wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
        self.TLCtrl1.AppendColumn( _(u"dir"), wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
        self.TLCtrl1.AppendColumn( _(u"access"), wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )

        Vsz2.Add( self.TLCtrl1, 1, wx.EXPAND |wx.ALL, 5 )

        self.MyMenu = MS.GetData(u'Menu2.db', u'')
        self.DoMenu = MS.SetData(u'',u'',u'')

        self.fillList()

        self.pnl1.SetSizer( Vsz2 )
        self.pnl1.Layout()
        Vsz2.Fit( self.pnl1 )
        self.pnl2 = wx.Panel( self.Spw1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Vsz3 = wx.BoxSizer( wx.VERTICAL )

        self.btn1 = wx.Button( self.pnl2, wx.ID_ANY, _(u"Add"), wx.DefaultPosition, wx.DefaultSize, 0 )
        Vsz3.Add( self.btn1, 0, wx.ALL, 5 )

        self.btn2 = wx.Button( self.pnl2, wx.ID_ANY, _(u"Edit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        Vsz3.Add( self.btn2, 0, wx.ALL, 5 )

        self.btn3 = wx.Button( self.pnl2, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0 )
        Vsz3.Add( self.btn3, 0, wx.ALL, 5 )


        Vsz3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn4 = wx.Button( self.pnl2, wx.ID_ANY, _(u"Separator"), wx.DefaultPosition, wx.DefaultSize, 0 )
        Vsz3.Add( self.btn4, 0, wx.ALL, 5 )


        self.pnl2.SetSizer( Vsz3 )
        self.pnl2.Layout()
        Vsz3.Fit( self.pnl2 )
        self.Spw1.SplitVertically( self.pnl1, self.pnl2, 532 )
        Vsz1.Add( self.Spw1, 1, wx.EXPAND, 5 )

        VL = wx.BoxSizer(wx.VERTICAL)

        self.Line = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        VL.Add(self.Line, 0, wx.EXPAND | wx.ALL, 5)

        Vsz1.Add(VL, 0, wx.EXPAND, 5)

        Hz1 = wx.BoxSizer(wx.HORIZONTAL)

        self.btna = wx.Button(self, wx.ID_ANY, _(u"New Bar"), wx.DefaultPosition, wx.DefaultSize, 0)
        Hz1.Add(self.btna, 0, wx.ALL, 5)

        self.btnb = wx.Button(self, wx.ID_ANY, _(u"Change Bar"), wx.DefaultPosition, wx.DefaultSize, 0)
        Hz1.Add(self.btnb, 0, wx.ALL, 5)

        self.btnc = wx.Button(self, wx.ID_ANY, _(u"Delete Bar"), wx.DefaultPosition, wx.DefaultSize, 0)
        Hz1.Add(self.btnc, 0, wx.ALL, 5)

        Vsz1.Add(Hz1, 0, wx.EXPAND, 5)

        self.txt = stc.StyledTextCtrl()

        self.SetSizer( Vsz1 )
        self.Layout()

        # Connect Events
        self.TLCtrl1.Bind( wx.dataview.EVT_TREELIST_ITEM_CHECKED, self.DoshowItm )
        self.TLCtrl1.Bind( wx.dataview.EVT_TREELIST_ITEM_CONTEXT_MENU, self.Thismenu )
        self.TLCtrl1.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.Thismenu)
        self.btn1.Bind( wx.EVT_BUTTON, self.Additm )
        self.btn2.Bind( wx.EVT_BUTTON, self.edititm )
        self.btn3.Bind( wx.EVT_BUTTON, self.delitm )
        self.btn4.Bind( wx.EVT_BUTTON, self.aplyit )
        self.btna.Bind(wx.EVT_BUTTON, self.Nbar)
        self.btnb.Bind(wx.EVT_BUTTON, self.Cbar)
        self.btnc.Bind(wx.EVT_BUTTON, self.Dbar)

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def DoshowItm( self, event ):
        print(event.GetEventObject())
        print(dir(event.GetEventObject()))
        event.Skip()

    def Thismenu( self, event ):
        ps = self.TLCtrl1.GetSelections()
        self.itmcod = self.TLCtrl1.GetItemText(ps[0],0)
        self.itmnam = self.TLCtrl1.GetItemText(ps[0],1)
        self.itmdir = self.TLCtrl1.GetItemText(ps[0],2)
        self.itmacc = self.TLCtrl1.GetItemText(ps[0],3)
        if int(self.itmcod) < 1000 and int(self.itmcod)%10 == 1:
            self.Cbar(None)
        elif int(self.itmcod) > 1000:
            #print(self.itmnam)
            self.edititm(None)
        else:
            print(self.itmnam,self.itmcod)
        event.Skip()

    def fillList(self):
        broot = self.TLCtrl1.GetRootItem()
        roots = self.MyMenu.AllBar("where mbarid < 9999")
        def getSubmenu(itmid, chditm, titl):
            subitems = self.MyMenu.ShowItem(itmid)
            for sub in subitems:
                subitm = self.TLCtrl1.AppendItem(chditm, titl)
                self.TLCtrl1.SetItemText(subitm, 0, str(sub[1]))
                if sub[6] == 'S':
                    getSubmenu(sub[1], subitm, sub[3])
                else:
                    self.TLCtrl1.SetItemText(subitm, 1, sub[3])
                    self.TLCtrl1.SetItemText(subitm, 2, sub[4])
                self.TLCtrl1.SetItemText(subitm, 3, sub[5])

            #return self.MyMenu.ShowItem(itmid)
        for r in roots:
            grp_roots = self.TLCtrl1.AppendItem(broot, 'Bar Menu')
            self.TLCtrl1.SetItemText(grp_roots, 0, str(r[0]))
            self.TLCtrl1.SetItemText(grp_roots, 1, r[1])
            self.TLCtrl1.SetItemText(grp_roots, 2, r[2])
            self.TLCtrl1.SetItemText(grp_roots, 3, r[3])
            items = self.MyMenu.ShowItem(r[0])
            # items = self.MyMenu.AmenuItm(r[0])
            #print(items)
            for i in items:
                chditm = self.TLCtrl1.AppendItem(grp_roots, 'Items Menu')
                self.TLCtrl1.SetItemText(chditm, 0, str(i[1]))
                if i[6] == 'S':
                    #subitms  = getSubmenu(i[1])
                    #print(subitms)
                    getSubmenu(i[1], chditm, i[3])
                    #for sub in subitms:
                    #    subitm = self.TLCtrl1.AppendItem(chditm, i[3])
                    #    self.TLCtrl1.SetItemText(subitm, 1, sub[3])
                    #    self.TLCtrl1.SetItemText(subitm, 2, sub[4])
                    #    self.TLCtrl1.SetItemText(subitm, 3, sub[5])

                if i[3] == None or i[3] == '':
                    self.TLCtrl1.SetItemText(chditm, 1, '---')
                    self.TLCtrl1.SetItemText(chditm, 2, '---')
                else:
                    self.TLCtrl1.SetItemText(chditm, 1, str(i[3]))
                    self.TLCtrl1.SetItemText(chditm, 2, str(i[4]))
                self.TLCtrl1.SetItemText(chditm, 3, str(i[5]))


    def Additm( self, event ):
        ps = self.TLCtrl1.GetSelections()
        self.itmcod = self.TLCtrl1.GetItemText(ps[0], 0)

        itdd = self.MyMenu.getmItem(int(self.itmcod))
        #print(itdd)
        if itdd == []:
            itmdd = [self.itmcod,'','']
        else:
            itmdd = [itdd[0][0],itdd[0][1],itdd[0][3]]
        #print(self.itmcod,itdd[0],itdd[3])
        self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
        self.Pnl = MF.MyPanel1(self.Frm,itmdd,u'AddNew')
        self.Frm.SetSize((720,360))
        self.Frm.Show()
        #event.Skip()


    def edititm( self, event ):
        ps = self.TLCtrl1.GetSelections()
        self.itmcod = self.TLCtrl1.GetItemText(ps[0], 0)

        itdd = self.MyMenu.getmItem(int(self.itmcod))[0]
        print(itdd)
        self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
        self.Pnl = MF.MyPanel1(self.Frm,itdd,'UpDate')
        self.Frm.SetSize((720, 360))
        self.Frm.Show()
        #event.Skip()

    def delitm( self, event ):
        ps = self.TLCtrl1.GetSelections()
        self.itmcod = self.TLCtrl1.GetItemText(ps[0], 0)

        itdd = self.MyMenu.getmItem(int(self.itmcod))[0]
        self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
        self.Pnl = MF.MyPanel1(self.Frm,itdd, 'Delete')
        self.Frm.SetSize((720, 360))
        self.Frm.Show()
        #event.Skip()

    def aplyit( self, event ):
        ps = self.TLCtrl1.GetSelections()
        self.itmcod = self.TLCtrl1.GetItemText(ps[0], 0)

        itdd = self.MyMenu.getmItem(int(self.itmcod))[0]
        litm = self.MyMenu.gItem(itdd[0])
        #print(itdd)
        #print(int(litm[-1][1])+1)
        self.DoMenu.Table = 'mitem'
        self.DoMenu.Additem(u'mbarid, itemid',[itdd[0],int(litm[-1][1])+1])
        mw = self.FindWindowByName('main')
        mb = mw.GetMenuBar()
        #lmb = mb.GetMenus()
        mbr = mb.FindItem(itdd[1])
        #indx = mbr[1].FindChildItem(itdd[1])[1]
        mbr[1].AppendSeparator()
        self.TLCtrl1.DeleteAllItems()
        self.fillList()
        self.Refresh()
        self.Layout()


    def Nbar(self, event):
        title = _("Note:   Avoid duplicate code for create and choose the correct format [991] [99az] \
                 A list of definition and access codes can be viewed at the last button in first row [...] \
                 You can use the same directories for the several menu bar . ")
        self.Frm = wx.Dialog(self)
        self.Pnl = MyPanel3(self.Frm,['','','','',[(u'',u'',u'',u'')]], _('Create'),title)
        self.Frm.SetSize((500, 235))
        self.Frm.SetTitle(_('New Menu Bar'))
        self.Frm.ShowModal()
        self.TLCtrl1.DeleteAllItems()
        self.fillList()
        self.Refresh()
        self.Layout()
        self.Frm.Destroy()

    def Cbar(self, event):
        title = _("Note:   Avoid duplicate code for changes and choose the correct format [991] [99az] \
                 A list of definition and access codes can be viewed at the last button in first row [...]\
                 You can use the same directories for the several menu bar . ")
        ps = self.TLCtrl1.GetSelections()
        self.itmcod = self.TLCtrl1.GetItemText(ps[0], 0)
        self.itmnam = self.TLCtrl1.GetItemText(ps[0], 1)
        self.itmdir = self.TLCtrl1.GetItemText(ps[0], 2)
        self.itmacc = self.TLCtrl1.GetItemText(ps[0], 3)
        self.accrcd = self.MyMenu.Acclvl(self.itmacc)
        dd = [self.itmnam,self.itmcod,self.itmacc,self.itmdir,self.accrcd]
        self.Frm = wx.Dialog(self)
        self.Pnl = MyPanel3(self.Frm,dd,_('Change'),title)
        self.Frm.SetSize((500, 235))
        self.Frm.SetTitle(_('Change Menu Bar'))
        self.Frm.ShowModal()
        self.TLCtrl1.DeleteAllItems()
        self.fillList()
        self.Refresh()
        self.Layout()
        self.Frm.Destroy()

    def Dbar(self, event):
        title = _(" Note : that by deleting the menu bar, all the items below it will also be removed \
                  Only the programs attached to the items will not be removed and the code will remain \
                  You can assign them to other items or create a new item . ")
        ps = self.TLCtrl1.GetSelections()
        self.itmcod = self.TLCtrl1.GetItemText(ps[0], 0)
        self.itmnam = self.TLCtrl1.GetItemText(ps[0], 1)
        self.itmdir = self.TLCtrl1.GetItemText(ps[0], 2)
        self.itmacc = self.TLCtrl1.GetItemText(ps[0], 3)
        self.accrcd = self.MyMenu.Acclvl(self.itmacc)
        dd = [self.itmnam, self.itmcod, self.itmacc, self.itmdir,self.accrcd]
        self.Frm = wx.Dialog(self)
        self.Pnl = MyPanel3(self.Frm,dd,_('Delete'),title)
        self.Frm.SetSize((500, 235))
        self.Frm.SetTitle(_('Delete Menu Bar'))
        self.Frm.ShowModal()
        if self.Pnl.Action:
            wx.MessageBox(_(u'Menu Bar and Access and Sub Item successfully Deleted'))
        self.TLCtrl1.DeleteAllItems()
        self.fillList()
        self.Refresh()
        self.Layout()
        self.Frm.Destroy()

    def Spw1OnIdle( self, event ):
        self.Spw1.SetSashPosition( 532 )
        self.Spw1.Unbind( wx.EVT_IDLE )



###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):

    def __init__( self, parent,Data,Buttom ,title,id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,235 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.Data = Data
        self.Buttom = Buttom
        self.GetMenu = MS.GetData(u'Menu2.db',u'')
        self.SetMenu = MS.SetData(u'',u'',u'')
        self.Action = False
        self.box1val = 1
        self.box2val = 'FFFF'
        self.oldbar = self.Data[0]

        Vsz1 = wx.BoxSizer(wx.VERTICAL)

        Vst = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(self, wx.ID_ANY, title, wx.DefaultPosition, wx.DefaultSize,0)
        self.title.Wrap(1)
        Vst.Add(self.title, 1, wx.ALL | wx.EXPAND, 5)

        Vsz1.Add(Vst, 1, wx.EXPAND, 5)

        Hsz1 = wx.BoxSizer(wx.HORIZONTAL)

        self.txt1 = wx.StaticText(self, wx.ID_ANY, _(u"Bar name"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt1.Wrap(-1)

        Hsz1.Add(self.txt1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld1 = wx.TextCtrl(self, wx.ID_ANY, self.Data[0], wx.DefaultPosition, wx.DefaultSize, 0)
        Hsz1.Add(self.fld1, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt2 = wx.StaticText(self, wx.ID_ANY, _(u"ID"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt2.Wrap(-1)

        Hsz1.Add(self.txt2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld2 = wx.TextCtrl(self, wx.ID_ANY, self.Data[1], wx.DefaultPosition, wx.Size(50, -1), 0)
        Hsz1.Add(self.fld2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt3 = wx.StaticText(self, wx.ID_ANY, _(u"Access"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt3.Wrap(-1)

        Hsz1.Add(self.txt3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.fld3 = wx.TextCtrl(self, wx.ID_ANY, self.Data[2], wx.DefaultPosition, wx.Size(50, -1), 0)
        Hsz1.Add(self.fld3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.atobtn = wx.Button(self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        Hsz1.Add(self.atobtn, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.atobtn.SetToolTip(_(u"Automatic code generate"))

        Vsz1.Add(Hsz1, 0, wx.EXPAND, 5)

        Hsz2 = wx.BoxSizer(wx.HORIZONTAL)

        self.txt4 = wx.StaticText(self, wx.ID_ANY, _(u"Directory"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt4.Wrap(-1)

        Hsz2.Add(self.txt4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.dirct = wx.DirPickerCtrl(self, wx.ID_ANY, GUI_PATH+self.Data[3][4:], _(u"Select a folder"), wx.DefaultPosition,
                                      wx.DefaultSize, wx.DIRP_DEFAULT_STYLE | wx.DIRP_SMALL)
        Hsz2.Add(self.dirct, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        Vsz1.Add(Hsz2, 0, wx.EXPAND, 5)

        Hsz3 = wx.BoxSizer(wx.HORIZONTAL)

        self.box1 = wx.CheckBox(self, wx.ID_ANY, _(u"Disable"), wx.DefaultPosition, wx.DefaultSize, 0)
        Hsz3.Add(self.box1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.box2 = wx.CheckBox(self, wx.ID_ANY, _(u"Hiden"), wx.DefaultPosition, wx.DefaultSize, 0)
        Hsz3.Add(self.box2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        if self.Data[4][0][2] == '0000':
            self.box2.SetValue(True)
        if self.Data[4][0][3] == 0:
            self.box1.SetValue(True)

        Vsz1.Add(Hsz3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        Hsz4 = wx.BoxSizer(wx.HORIZONTAL)

        Hsz4.Add((0, 0), 1, wx.EXPAND, 5)

        self.btn1 = wx.Button(self, wx.ID_ANY, _(u"Cancle"), wx.DefaultPosition, wx.DefaultSize, 0)
        Hsz4.Add(self.btn1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btn2 = wx.Button(self, wx.ID_ANY, Buttom, wx.DefaultPosition, wx.DefaultSize, 0)
        Hsz4.Add(self.btn2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        Vsz1.Add(Hsz4, 0, wx.EXPAND, 5)

        self.SetSizer(Vsz1)
        self.Layout()

        # Connect Events
        self.atobtn.Bind( wx.EVT_BUTTON, self.atocod )
        self.dirct.Bind(wx.EVT_DIRPICKER_CHANGED, self.bardir)
        self.box1.Bind(wx.EVT_CHECKBOX, self.disbar)
        self.box2.Bind(wx.EVT_CHECKBOX, self.hidbar)
        self.btn1.Bind(wx.EVT_BUTTON, self.cancl)
        self.btn2.Bind(wx.EVT_BUTTON, self.doit)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def atocod(self, event):
        if self.Buttom == _('Create'):
            allbar = self.GetMenu.AllBar('where mbarid < 9999')
            print(allbar)
            if allbar != [] :
                print(allbar[-1][0]+100)
                alphabt = '_abcdefghijklmnopqrstuvwxyz'
                lnumstr = str(allbar[-1][0]+100)[0]
                rnumstr = str(allbar[-1][0]+100)[-1]
                self.fld2.SetValue(str(allbar[-1][0]+100))
                self.fld3.SetValue(lnumstr+rnumstr+alphabt[int(lnumstr)]+alphabt[int(rnumstr)])
            else:

                self.fld2.SetValue(str(101))
                self.fld3.SetValue('11aa')

    def bardir(self, event):
        mydir = event.GetEventObject().GetPath()
        mydir.replace(GUI_PATH,u"GUI.")
        #print(mydir)

        self.newdir = mydir.replace(GUI_PATH,u"GUI.")
        #print(self.newdir)

    def disbar(self, event):
        if event.GetEventObject().GetValue():
            self.box1val = 0
        else:
            self.box1val = 1
        #print(self.box1val)

    def hidbar(self, event):
        if event.GetEventObject().GetValue():
            self.box2val = '0000'
        else:
            self.box2val = 'FFFF'
        #print(self.box2val)

    def cancl(self, event):
        self.Action = False
        q = self.GetParent()
        q.Close()

    def doit(self, event):
        mw = self.FindWindowByName('main')
        if mw.GetMenuBar() != None:
            mb = mw.GetMenuBar()
        else:
            mb = mw.NewMenu()
        if event.GetEventObject().GetLabel() == _('Create'):
            data1 = self.fld1.GetValue()
            data2 = self.fld2.GetValue()
            data3 = self.fld3.GetValue()
            mydir = self.dirct.GetPath()
            self.newdir = mydir.replace(GUI_PATH, u"GUI.")
            self.SetMenu.Table = u'menubar'
            self.SetMenu.Additem(u'mbarid , mbarname , mbardir ,  acclvlid ', (data2,data1,self.newdir,data3))
            data4 = self.box1val
            data5 = self.box2val
            self.SetMenu.Table = u'access'
            self.SetMenu.Additem(u'acclvlid , userid , acclvl , disenable ',(data3, 1, data5, data4))

            mb.Append(wx.Menu(),data1)


        elif event.GetEventObject().GetLabel() == _('Change'):
            data1 = self.fld1.GetValue()
            mydir = self.dirct.GetPath()
            self.newdir = mydir.replace(GUI_PATH,u"GUI.")
            self.SetMenu.Table = u'menubar'
            self.SetMenu.Upditem(u'mbarname = ? , mbardir = ?  where mbarid = %s ' % self.Data[1],(data1,self.newdir))
            mb.SetMenuLabel(mb.FindMenu(self.oldbar),data1)

        elif event.GetEventObject().GetLabel() == _('Delete'):
            self.SetMenu.Table = u'menubar'
            self.SetMenu.Delitem(u" menubar.mbarid = %s" % self.Data[1] )
            self.SetMenu.Table = u'access'
            self.SetMenu.Delitem(u" access.acclvlid = '%s' "% self.Data[2])
            if len(self.GetMenu.gBarItm(self.Data[1])) != 0:
                for itm in self.GetMenu.gBarItm(self.Data[1]):
                    self.SetMenu.Table = u'mitem'
                    self.SetMenu.Delitem(u" mitem.itemid = %s " % itm[1] )
                    self.SetMenu.Table = u'extended'
                    self.SetMenu.Delitem(u" extended.extid = '%s' " % itm[2])

            mb.Remove(mb.FindMenu(self.Data[0]))

        else:
            event.Skip()

        self.Action = True
        q = self.GetParent()
        q.Close()

