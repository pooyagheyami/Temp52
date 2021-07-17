# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 430,455 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"Database", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.txt1.Wrap( -1 )

		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.filedb = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		Hsz1.Add( self.filedb, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz1, 0,wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"Method", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.txt2.Wrap( -1 )

		Hsz2.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs1Choices = [ u"Input", u"Output" ]
		self.chs1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs1Choices, 0 )
		self.chs1.SetSelection( 0 )
		Hsz2.Add( self.chs1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.line2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		Hsz2.Add( self.line2, 0, wx.EXPAND |wx.ALL, 5 )


		Hsz2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Change Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"To CVS", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn3 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz2.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		Vsz11 = wx.BoxSizer( wx.VERTICAL )

		self.txt3 = wx.StaticText( self, wx.ID_ANY, u"Tables List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt3.Wrap( -1 )

		Vsz11.Add( self.txt3, 0, wx.ALL, 5 )

		TblstChoices = []
		self.Tblst = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, TblstChoices, 0 )
		Vsz11.Add( self.Tblst, 1, wx.ALL|wx.EXPAND, 5 )


		Hsz3.Add( Vsz11, 1, wx.EXPAND, 5 )

		Vsz12 = wx.BoxSizer( wx.VERTICAL )

		self.txt4 = wx.StaticText( self, wx.ID_ANY, u"Feilds List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt4.Wrap( -1 )

		Vsz12.Add( self.txt4, 0, wx.ALL, 5 )

		FldlstChoices = []
		self.Fldlst = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, FldlstChoices, 0 )
		Vsz12.Add( self.Fldlst, 1, wx.ALL|wx.EXPAND, 5 )


		Hsz3.Add( Vsz12, 1, wx.EXPAND, 5 )

		Vsz13 = wx.BoxSizer( wx.VERTICAL )

		self.txt5 = wx.StaticText( self, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt5.Wrap( -1 )

		Vsz13.Add( self.txt5, 0, wx.ALL, 5 )

		self.line1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
		Vsz13.Add( self.line1, 0, wx.EXPAND |wx.ALL, 5 )

		self.rdio1 = wx.RadioButton(self, wx.ID_ANY, u"Join", wx.DefaultPosition, wx.DefaultSize, 0)
		Vsz13.Add(self.rdio1, 0, wx.ALL, 5)

		self.rdio2 = wx.RadioButton(self, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0)
		Vsz13.Add(self.rdio2, 0, wx.ALL, 5)

		self.rdio3 = wx.RadioButton(self, wx.ID_ANY, u"Insert", wx.DefaultPosition, wx.DefaultSize, 0)
		Vsz13.Add(self.rdio3, 0, wx.ALL, 5)

		self.rdio4 = wx.RadioButton(self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0)
		Vsz13.Add(self.rdio4, 0, wx.ALL, 5)

		self.rdio5 = wx.RadioButton(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
		Vsz13.Add(self.rdio5, 0, wx.ALL, 5)

		self.rdio6 = wx.RadioButton(self, wx.ID_ANY, u"peer to peer", wx.DefaultPosition, wx.DefaultSize, 0)
		Vsz13.Add(self.rdio6, 0, wx.ALL, 5)


		Hsz3.Add( Vsz13, 1, wx.EXPAND, 5 )


		Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt6 = wx.StaticText( self, wx.ID_ANY, u"Where Clause", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt6.Wrap( -1 )

		Hsz4.Add( self.txt6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		dlmntChoices = [ u"=", u"Is", u">", u"<", u">=", u"=>", u"In", u"Is Null" ]
		self.dlmnt = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dlmntChoices, 0 )
		self.dlmnt.SetSelection( 0 )
		Hsz4.Add( self.dlmnt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz4, 0, wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt7 = wx.StaticText( self, wx.ID_ANY, u"Program Statement", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt7.Wrap( 1 )

		Hsz5.Add( self.txt7, 0, wx.ALL, 5 )

		self.filprg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Hsz5.Add( self.filprg, 1, wx.ALL, 5 )

		self.btn4 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE|wx.BU_EXACTFIT )
		Hsz5.Add( self.btn4, 0, wx.ALL, 5 )


		Vsz1.Add( Hsz5, 0, wx.EXPAND, 5 )

		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt8 = wx.StaticText( self, wx.ID_ANY, u"SQL Statement", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt8.Wrap( 1 )

		Hsz6.Add( self.txt8, 0, wx.ALL, 5 )

		self.fldsql = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Hsz6.Add( self.fldsql, 1, wx.ALL, 5 )

		self.btn5 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE|wx.BU_EXACTFIT )
		Hsz6.Add( self.btn5, 0, wx.ALL, 5 )


		Vsz1.Add( Hsz6, 0, wx.EXPAND, 5 )

		Hsz7 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn6 = wx.Button( self, wx.ID_ANY, u"Make SQL", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz7.Add( self.btn6, 0, wx.ALL, 5 )

		self.btn7 = wx.Button( self, wx.ID_ANY, u"Copy Line", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz7.Add( self.btn7, 0, wx.ALL, 5 )

		self.btn8 = wx.Button( self, wx.ID_ANY, u"To Program", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz7.Add( self.btn8, 0, wx.ALL, 5 )


		Vsz1.Add( Hsz7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.filedb.Bind( wx.EVT_FILEPICKER_CHANGED, self.dbfil )
		self.chs1.Bind( wx.EVT_CHOICE, self.dbmtd )
		self.btn1.Bind( wx.EVT_BUTTON, self.chgdata )
		self.btn2.Bind( wx.EVT_BUTTON, self.tocvs )
		self.btn3.Bind( wx.EVT_BUTTON, self.othrfil )
		self.Tblst.Bind( wx.EVT_LISTBOX, self.slctbl )
		self.Tblst.Bind( wx.EVT_LISTBOX_DCLICK, self.slctbl )
		self.Fldlst.Bind( wx.EVT_LISTBOX, self.fldlst )
		self.Fldlst.Bind( wx.EVT_LISTBOX_DCLICK, self.fldlst )
		self.dlmnt.Bind( wx.EVT_CHOICE, self.chs2 )
		self.btn4.Bind( wx.EVT_BUTTON, self.cpyps )
		self.btn5.Bind( wx.EVT_BUTTON, self.cpysql )
		self.btn6.Bind( wx.EVT_BUTTON, self.mksql )
		self.btn7.Bind( wx.EVT_BUTTON, self.cpylin )
		self.btn8.Bind( wx.EVT_BUTTON, self.toprg )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dbfil( self, event ):
		event.Skip()

	def dbmtd( self, event ):
		event.Skip()

	def chgdata( self, event ):
		event.Skip()

	def tocvs( self, event ):
		event.Skip()

	def othrfil( self, event ):
		event.Skip()

	def slctbl( self, event ):
		event.Skip()


	def fldlst( self, event ):
		event.Skip()


	def chs2( self, event ):
		event.Skip()

	def cpyps( self, event ):
		event.Skip()

	def cpysql( self, event ):
		event.Skip()

	def mksql( self, event ):
		event.Skip()

	def cpylin( self, event ):
		event.Skip()

	def toprg( self, event ):
		event.Skip()


