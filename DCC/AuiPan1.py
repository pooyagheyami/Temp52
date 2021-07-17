# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx

from Config.Init import *

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 649,391 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        Vsz1 = wx.BoxSizer( wx.VERTICAL )

        Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

        Vsz11 = wx.BoxSizer( wx.VERTICAL )

        self.txt1 = wx.StaticText( self, wx.ID_ANY, u"Aui Pans List:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt1.Wrap( -1 )

        Vsz11.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        PAList1Choices = self.Openlst()
        #PAList1Choices = []
        self.PAList1 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, PAList1Choices, 0 )
        Vsz11.Add( self.PAList1, 1, wx.ALL, 5 )


        Hsz1.Add( Vsz11, 0, wx.EXPAND, 5 )

        Vsz12 = wx.BoxSizer( wx.VERTICAL )

        Hsz11 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt2 = wx.StaticText( self, wx.ID_ANY, u"Panid", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt2.Wrap( -1 )

        Hsz11.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        Hsz11.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt3 = wx.StaticText( self, wx.ID_ANY, u"doking", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt3.Wrap( -1 )

        Hsz11.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        chs1Choices = [ u"Top", u"Left", u"Center", u"Right", u"Bottum" ]
        self.chs1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs1Choices, 0 )
        self.chs1.SetSelection( 1 )
        Hsz11.Add( self.chs1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt4 = wx.StaticText( self, wx.ID_ANY, u"Leyer", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt4.Wrap( -1 )

        Hsz11.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.lyr = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 9, 0.000000, 1 )
        self.lyr.SetDigits( 0 )
        Hsz11.Add( self.lyr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.chk1 = wx.CheckBox( self, wx.ID_ANY, u"Pin Button", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chk1.SetValue(True)
        Hsz11.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz12.Add( Hsz11, 1, wx.EXPAND, 5 )

        Hsz12 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt5 = wx.StaticText( self, wx.ID_ANY, u"Dock", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt5.Wrap( -1 )

        Hsz12.Add( self.txt5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        chs2Choices = [ u"Dock", u"Float" ]
        self.chs2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs2Choices, 0 )
        self.chs2.SetSelection( 0 )
        Hsz12.Add( self.chs2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt6 = wx.StaticText( self, wx.ID_ANY, u"Resize", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt6.Wrap( -1 )

        Hsz12.Add( self.txt6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        chs3Choices = [ u"Resizable", u"Fixed" ]
        self.chs3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs3Choices, 0 )
        self.chs3.SetSelection( 0 )
        Hsz12.Add( self.chs3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt7 = wx.StaticText( self, wx.ID_ANY, u"Pane Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt7.Wrap( -1 )

        Hsz12.Add( self.txt7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.PSw = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        Hsz12.Add( self.PSw, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.PSh = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        Hsz12.Add( self.PSh, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz12.Add( Hsz12, 1, wx.EXPAND, 5 )

        Hsz13 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt8 = wx.StaticText( self, wx.ID_ANY, u"name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt8.Wrap( -1 )

        Hsz13.Add( self.txt8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz13.Add( self.fld2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt9 = wx.StaticText( self, wx.ID_ANY, u"Best Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt9.Wrap( -1 )

        Hsz13.Add( self.txt9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.BSw = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        Hsz13.Add( self.BSw, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.BSh = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        Hsz13.Add( self.BSh, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz12.Add( Hsz13, 1, wx.EXPAND, 5 )

        Hsz14 = wx.BoxSizer( wx.HORIZONTAL )

        self.chk2 = wx.CheckBox( self, wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz14.Add( self.chk2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.chk3 = wx.CheckBox( self, wx.ID_ANY, u"Hide", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz14.Add( self.chk3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz12.Add( Hsz14, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        Hsz15 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt10 = wx.StaticText( self, wx.ID_ANY, u"Program", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt10.Wrap( -1 )

        Hsz15.Add( self.txt10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fil1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
        Hsz15.Add( self.fil1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz12.Add( Hsz15, 1, wx.EXPAND, 5 )

        Hsz16 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn1 = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz16.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btn2 = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz16.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btn3 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz16.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnprw = wx.Button( self, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz16.Add( self.btnprw, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz12.Add( Hsz16, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        Hsz1.Add( Vsz12, 1, wx.EXPAND, 5 )


        Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

        Vsz2 = wx.BoxSizer( wx.VERTICAL )

        self.lin1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        Vsz2.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )


        Vsz1.Add( Vsz2, 0, wx.EXPAND, 5 )

        Vsz3 = wx.BoxSizer( wx.VERTICAL )

        Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

        self.txt11 = wx.StaticText( self, wx.ID_ANY, u"Link Database", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt11.Wrap( -1 )

        Hsz2.Add( self.txt11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fld3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz2.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz3.Add( Hsz2, 0, wx.EXPAND, 5 )

        Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn4 = wx.Button( self, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz3.Add( self.btn4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btn5 = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz3.Add( self.btn5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt12 = wx.StaticText( self, wx.ID_ANY, u"Table", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt12.Wrap( -1 )

        Hsz3.Add( self.txt12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.tblst = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        Hsz3.Add( self.tblst, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt13 = wx.StaticText( self, wx.ID_ANY, u"field list", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt13.Wrap( -1 )

        Hsz3.Add( self.txt13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fldlst = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        Hsz3.Add( self.fldlst, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        Vsz3.Add( Hsz3, 1, wx.EXPAND, 5 )

        Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn6 = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
        Hsz4.Add( self.btn6, 0, wx.ALL, 5 )


        Vsz3.Add( Hsz4, 0, wx.EXPAND, 5 )


        Vsz1.Add( Vsz3, 0, wx.EXPAND, 5 )


        self.SetSizer( Vsz1 )
        self.Layout()

        # Connect Events
        self.PAList1.Bind( wx.EVT_LISTBOX_DCLICK, self.slctpn )
        self.chs1.Bind( wx.EVT_CHOICE, self.dokng )
        self.lyr.Bind( wx.EVT_TEXT, self.gtlyr )
        self.lyr.Bind( wx.EVT_TEXT_ENTER, self.gtlyr )
        self.chk1.Bind( wx.EVT_CHECKBOX, self.pinbtn )
        self.chs2.Bind( wx.EVT_CHOICE, self.dkflt )
        self.chs3.Bind( wx.EVT_CHOICE, self.rsizfix )
        self.chk2.Bind( wx.EVT_CHECKBOX, self.disabl )
        self.chk3.Bind( wx.EVT_CHECKBOX, self.shohid )
        self.fil1.Bind( wx.EVT_FILEPICKER_CHANGED, self.progfil )
        self.btn1.Bind( wx.EVT_BUTTON, self.addpn )
        self.btn2.Bind( wx.EVT_BUTTON, self.edtpn )
        self.btn3.Bind( wx.EVT_BUTTON, self.delpn )
        self.btnprw.Bind( wx.EVT_BUTTON, self.prwiv )
        self.btn4.Bind( wx.EVT_BUTTON, self.opndb )
        self.btn5.Bind( wx.EVT_BUTTON, self.edtdb )
        self.btn6.Bind( wx.EVT_BUTTON, self.gnret )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def Openlst(self):
        self.PAlst = []
        lst = []
        with open(GUI_PATH+u'AuiPanel'+SLASH+'PAui.p', 'r') as f:
            pans = f.readlines()
            for p in pans:
                self.PAlst.append(p.split('\n'))
                lst.append(p.split(',')[0])
            print(self.PAlst,lst)
        return lst


    def slctpn( self, event ):
        event.Skip()

    def dokng( self, event ):
        event.Skip()

    def gtlyr( self, event ):
        event.Skip()


    def pinbtn( self, event ):
        event.Skip()

    def dkflt( self, event ):
        event.Skip()

    def rsizfix( self, event ):
        event.Skip()

    def disabl( self, event ):
        event.Skip()

    def shohid( self, event ):
        event.Skip()

    def progfil( self, event ):
        event.Skip()

    def addpn( self, event ):
        event.Skip()

    def edtpn( self, event ):
        event.Skip()

    def delpn( self, event ):
        event.Skip()

    def prwiv( self, event ):
        event.Skip()

    def opndb( self, event ):
        event.Skip()

    def edtdb( self, event ):
        event.Skip()

    def gnret( self, event ):
        event.Skip()