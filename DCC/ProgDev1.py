# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx

import importlib

import Database.MenuSet2 as MS
import AI.Analiz as AZ

from Config.Init import *

_ = wx.GetTranslation

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        Vsz1 = wx.BoxSizer( wx.VERTICAL )

        Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

        self.GetData = MS.GetData(u'Menu2.db',u'')

        #mjoin = """ left join mitem on handler.handlerid = mitem.handlerid \
        #            left join menubar on mitem.mbarid = menubar.mbarid """
        self.mylist = self._meklst()
        #self.mylist = GetData.AllHndl(ext= mjoin + " where handler.handlerid < 99000 ")
        #print(self.mylist)

        self.Title = wx.StaticText( self, wx.ID_ANY, _(u"List of Program in Application "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Title.Wrap( -1 )

        Hsz1.Add( self.Title, 0, wx.ALL, 5 )


        Vsz1.Add( Hsz1, 0, wx.EXPAND, 5 )

        Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

        Vsz2 = wx.BoxSizer( wx.VERTICAL )

        LPro1Choices = [i[1] for i in self.mylist ]
        self.LPro1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, LPro1Choices, wx.LB_ALWAYS_SB )
        Vsz2.Add( self.LPro1, 1, wx.ALL, 5 )


        Hsz2.Add( Vsz2, 1, wx.EXPAND, 5 )

        Vsz3 = wx.BoxSizer( wx.VERTICAL )

        Hsz10 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt1 = wx.StaticText( self, wx.ID_ANY, _(u"Id No."), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt1.Wrap( -1 )

        Hsz10.Add( self.txt1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz10.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt2 = wx.StaticText( self, wx.ID_ANY, _(u"Prog. No."), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt2.Wrap( -1 )

        Hsz10.Add( self.txt2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz10.Add( self.fld2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz3.Add( Hsz10, 0, wx.EXPAND, 5 )

        Hsz11 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt3 = wx.StaticText( self, wx.ID_ANY, _(u"Do name"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt3.Wrap( -1 )

        Hsz11.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz11.Add( self.fld3, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.prw = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        self.prw.SetToolTip( _(u"Preview" ))

        Hsz11.Add( self.prw, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz3.Add( Hsz11, 0, wx.EXPAND, 5 )

        Hsz12 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt4 = wx.StaticText( self, wx.ID_ANY, _(u"Directory"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt4.Wrap( -1 )

        Hsz12.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fdir = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
        self.fdir.SetToolTip( _(u"Browse" ))

        Hsz12.Add( self.fdir, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz3.Add( Hsz12, 0, wx.EXPAND, 5 )

        Hsz13 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt5 = wx.StaticText( self, wx.ID_ANY, _(u"Parameters"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt5.Wrap( -1 )

        Hsz13.Add( self.txt5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz13.Add( self.fld5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz3.Add( Hsz13, 0, wx.EXPAND, 5 )

        Hsz14 = wx.BoxSizer( wx.HORIZONTAL )

        self.box1 = wx.CheckBox( self, wx.ID_ANY, _(u"Public it"), wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz14.Add( self.box1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt6 = wx.StaticText( self, wx.ID_ANY, _(u"Link:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt6.Wrap( -1 )

        Hsz14.Add( self.txt6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz14.Add( self.fld6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz3.Add( Hsz14, 0, wx.EXPAND, 5 )

        Hsz15 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn1 = wx.Button( self, wx.ID_ANY, _(u"Open Edit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz15.Add( self.btn1, 0, wx.ALL, 5 )

        self.btn2 = wx.Button( self, wx.ID_ANY, _(u"Add New"), wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz15.Add( self.btn2, 0, wx.ALL, 5 )

        self.btn3 = wx.Button( self, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz15.Add( self.btn3, 0, wx.ALL, 5 )


        Vsz3.Add( Hsz15, 0, wx.EXPAND, 5 )


        Hsz2.Add( Vsz3, 1, wx.EXPAND, 5 )


        Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )

        Vsz4 = wx.BoxSizer( wx.VERTICAL )

        self.lin1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        Vsz4.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )


        Vsz1.Add( Vsz4, 0, wx.EXPAND, 5 )

        Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn4 = wx.Button( self, wx.ID_ANY, _(u"Open"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn4.SetToolTip( _(u"Open Database" ))

        Hsz3.Add( self.btn4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btn5 = wx.Button( self, wx.ID_ANY, _(u"New"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn5.SetToolTip( _(u"New Database" ))

        Hsz3.Add( self.btn5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt7 = wx.StaticText( self, wx.ID_ANY, _(u"Tabels Used"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt7.Wrap( -1 )

        Hsz3.Add( self.txt7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.tbls = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz3.Add( self.tbls, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz1.Add( Hsz3, 0, wx.EXPAND, 5 )

        Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt8 = wx.StaticText( self, wx.ID_ANY, _(u"List Fields use"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt8.Wrap( -1 )

        Hsz4.Add( self.txt8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.lflds = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz4.Add( self.lflds, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz1.Add( Hsz4, 0, wx.EXPAND, 5 )

        Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt9 = wx.StaticText( self, wx.ID_ANY, _(u"action type"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt9.Wrap( -1 )

        Hsz5.Add( self.txt9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        actypChoices = []
        self.actyp = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, actypChoices, 0 )
        self.actyp.SetSelection( 0 )
        Hsz5.Add( self.actyp, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Hsz5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn6 = wx.Button( self, wx.ID_ANY, _(u"Setting..."), wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz5.Add( self.btn6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz1.Add( Hsz5, 0, wx.EXPAND, 5 )

        Hsz6 = wx.BoxSizer( wx.HORIZONTAL )


        Hsz6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn7 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz6.Add( self.btn7, 0, wx.ALL, 5 )

        self.btn8 = wx.Button( self, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz6.Add( self.btn8, 0, wx.ALL, 5 )


        Vsz1.Add( Hsz6, 0, wx.EXPAND, 5 )


        self.SetSizer( Vsz1 )
        self.Layout()

        # Connect Events
        self.LPro1.Bind( wx.EVT_LISTBOX, self.lstkt )
        self.LPro1.Bind( wx.EVT_LISTBOX_DCLICK, self.chkit )
        self.prw.Bind( wx.EVT_BUTTON, self.proprw )
        self.fdir.Bind( wx.EVT_DIRPICKER_CHANGED, self.chgdir )
        self.box1.Bind( wx.EVT_CHECKBOX, self.poblic )
        self.btn1.Bind( wx.EVT_BUTTON, self.opnedit )
        self.btn2.Bind( wx.EVT_BUTTON, self.addnew )
        self.btn3.Bind( wx.EVT_BUTTON, self.delpro )
        self.btn4.Bind( wx.EVT_BUTTON, self.opndata )
        self.btn5.Bind( wx.EVT_BUTTON, self.newdata )
        self.actyp.Bind( wx.EVT_CHOICE, self.chstyp )
        self.btn6.Bind( wx.EVT_BUTTON, self.sting )
        self.btn7.Bind( wx.EVT_BUTTON, self.cancl )
        self.btn8.Bind( wx.EVT_BUTTON, self.aply )

    def __del__( self ):
        pass

    def _meklst(self):
        mylist = []
        tst1 = []
        tst2 = []
        mjoin = """ left join mitem on handler.handlerid = mitem.handlerid \
                    left join menubar on mitem.mbarid = menubar.mbarid """

        mlist = self.GetData.AllHndl(ext=mjoin + " where handler.handlerid < 99000  and handler.prgdir = menubar.mbarid")
        for itm in mlist:
            #print(itm[1],itm[14])
            if itm[1] not in tst1 :
                mylist.append(itm)
                tst1.append(itm[1])
                tst2.append(itm[14])
            if itm[14] not in tst2:
                mylist.append(itm)
                tst1.append(itm[1])
                tst2.append(itm[14])
        #print(mylist)
        return mylist
    # Virtual event handlers, overide them in your derived class
    def lstkt( self, event ):
        iprog = event.GetEventObject().GetStringSelection()
        nlst = event.GetEventObject().GetSelection()
        #print(iprog,nlst,self.mylist[nlst])
        fl, pth = self.analiz(iprog,self.mylist[nlst][14])
        Data = [str(self.mylist[nlst][0]), self.mylist[nlst][2], fl, pth, self.mylist[nlst][3], '']
        self.fillfld(Data)

        event.Skip()

    def chkit( self, event ):
        event.Skip()

    def fillfld(self, D):
        self.fld1.SetValue(D[0])
        self.fld2.SetValue(D[1])
        self.fld3.SetValue(D[2])
        self.fdir.SetPath(D[3])
        self.fld5.SetValue(D[4])
        self.fld6.SetValue(D[5])
        if D[5] != '':
            self.box1.SetValue(1)

    def proprw( self, event ):
        a2 = self.fld3.GetValue()
        if a2 != '':
            try:
                m = importlib.import_module(a2)
                self.Frm = wx.Frame(self, -1, pos=wx.DefaultPosition, size=wx.DefaultSize)
                self.pnl = m.MyPanel1(self.Frm)
                self.Frm.Show()
            except ImportError as error:
                wx.MessageBox(error)
                print(error)
        event.Skip()

    def chgdir( self, event ):
        event.Skip()

    def poblic( self, event ):
        event.Skip()

    def opnedit( self, event ):
        event.Skip()

    def addnew( self, event ):
        event.Skip()

    def delpro( self, event ):
        pronam = self.LPro1.GetStringSelection()
        pronum = self.LPro1.GetSelection()

        for pro in self.mylist:
            if pro[1] == pronam:
                #print(pro)
                SetData = MS.SetData(u'', u'', u'')
                SetData.Table = u'handler'
                SetData.Delitem('handlerid = %d ' % pro[0])
                wx.MessageBox(_("program delete from list"))
                self.LPro1.Delete(pronum)

        event.Skip()

    def opndata( self, event ):
        event.Skip()

    def newdata( self, event ):
        event.Skip()

    def chstyp( self, event ):
        event.Skip()

    def sting( self, event ):
        event.Skip()

    def cancl( self, event ):
        q = self.GetParent()
        q.Close()

    def aply( self, event ):
        q = self.GetParent()
        q.Close()


    def analiz(self, file, path):
        if path == None:
            return ''
        for root, dirs, files in os.walk(GUI_PATH):

            if file+'.py' in files:
                #print(root,dirs,files)
                #print(os.path.exists(root+"\\"+file+'.py'))
                if path.split('.')[-1] == root.split('\\')[-1]:
                    mpath = root
        if mpath == None:
            return ''
        else:
            #print(mpath)
            impfil = AZ.Anlzfil(mpath + '\\' + file + '.py')
            #impfil = AZ.Anlzfil(GUI_PATH+path+'\\'+file+'.py')
            impfil.parsefil()
            for imp in impfil.imprts:
                if 'GUI' in imp:
                    return imp.split(' ')[1],mpath
            else:
                return ''
