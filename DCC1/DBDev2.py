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

from Config.Init import *

import Database.PostGet as PG

from AI.Analiz import *

###########################################################################
## Class MyPanel6
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.lbl0 = wx.StaticText( self.P1, wx.ID_ANY, u"Select database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl0.Wrap( -1 )

		Vsz2.Add( self.lbl0, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.dbfile = wx.FilePickerCtrl( self.P1, wx.ID_ANY, wx.EmptyString, u"Select Database file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		Vsz2.Add( self.dbfile, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, u"List of Tabel:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Vsz2.Add( self.lbl1, 0, wx.ALL, 5 )

		self.DVC1 = wx.dataview.TreeListCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_HAS_BUTTONS|wx.TR_DEFAULT_STYLE )
		self.Col1 = self.DVC1.AppendColumn( u"Name", 160,  wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendColumn( u"Type", 70,  wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		#self.Col3 = self.DVC1.AppendColumn( u"Name", 0,  wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		Vsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn1.SetBitmap( wx.Bitmap( ICON16_PATH + u'table_row_insert.png', wx.BITMAP_TYPE_ANY ) )
		self.btn1.SetToolTip( u"Insert" )

		Hsz1.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn2.SetBitmap(wx.Bitmap(ICON16_PATH + u'table_refresh.png', wx.BITMAP_TYPE_ANY))
		self.btn2.SetToolTip(u"Update")

		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn3.SetBitmap(wx.Bitmap(ICON16_PATH + u'table_row_delete.png', wx.BITMAP_TYPE_ANY))
		self.btn3.SetToolTip(u"Delete")

		Hsz1.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn4.SetBitmap(wx.Bitmap(ICON16_PATH + u'table_relationship.png', wx.BITMAP_TYPE_ANY))
		self.btn4.SetToolTip(u"Join")

		Hsz1.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn5.SetBitmap(wx.Bitmap(ICON16_PATH + u'table_import.png', wx.BITMAP_TYPE_ANY))
		self.btn5.SetToolTip(u"Brows")

		Hsz1.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn6.SetBitmap(wx.Bitmap(ICON16_PATH + u'accept_button.png', wx.BITMAP_TYPE_ANY))
		self.btn6.SetToolTip(u"Apply")

		Hsz1.Add( self.btn6, 0, wx.ALL, 5 )

		self.btn7 = wx.BitmapButton(self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'table_lightning.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetToolTip(u"Generate")
		Hsz1.Add(self.btn7, 0, wx.ALL, 5)


		Vsz2.Add( Hsz1, 0, wx.EXPAND, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, u"Method in program", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs1Choices = [ u"set", u"get", u"both" ]
		self.chs1 = wx.Choice( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs1Choices, 0 )
		self.chs1.SetSelection( 0 )
		Hsz2.Add( self.chs1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 0, wx.EXPAND, 5 )

		self.fldinit = wx.TextCtrl(self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
		                           wx.HSCROLL|wx.TE_MULTILINE|wx.TE_WORDWRAP )
		Vsz3.Add(self.fldinit, 1, wx.ALL | wx.EXPAND, 5)

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, u"Program Statments", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl4.Wrap( -1 )

		Hsz3.Add( self.lbl4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btnps = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz3.Add( self.btnps, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz3, 0, wx.EXPAND, 5 )

		self.fldprg = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Vsz3.Add( self.fldprg, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self.P2, wx.ID_ANY, u"SQL  Statments", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl5.Wrap( -1 )

		Hsz4.Add( self.lbl5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btnss = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz4.Add( self.btnss, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz4, 0, wx.EXPAND, 5 )

		self.fldsql = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Vsz3.Add( self.fldsql, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn7 = wx.Button( self.P2, wx.ID_ANY, u"To CVS", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.btn7, 0, wx.ALL, 5 )

		self.btn8 = wx.Button( self.P2, wx.ID_ANY, u"To Excel", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.btn8, 0, wx.ALL, 5 )

		self.btn9 = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btn9.SetToolTip( u"Extended" )

		Hsz5.Add( self.btn9, 0, wx.ALL, 5 )


		Vsz3.Add( Hsz5, 0, wx.EXPAND, 5 )


		self.P2.SetSizer( Vsz3 )
		self.P2.Layout()
		Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 232 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		#Parameter init
		self.table = u''
		self.field = u''
		self.data = u''
		self.sqfile = u''

		# Connect Events
		self.dbfile.Bind(wx.EVT_FILEPICKER_CHANGED, self.dbopn)
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctitm, id = wx.ID_ANY )
		self.DVC1.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.slctitm, id=wx.ID_ANY)
		self.btn1.Bind( wx.EVT_BUTTON, self.Addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.edtit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.comit )
		self.btn5.Bind( wx.EVT_BUTTON, self.recomt )
		self.btn6.Bind( wx.EVT_BUTTON, self.brows )

		self.chs1.Bind( wx.EVT_CHOICE, self.chgmtd )
		self.btnps.Bind( wx.EVT_BUTTON, self.prgstm )
		self.btnss.Bind( wx.EVT_BUTTON, self.sqlstm )
		self.btn7.Bind( wx.EVT_BUTTON, self.tocvs )
		self.btn8.Bind( wx.EVT_BUTTON, self.toexl )
		self.btn9.Bind( wx.EVT_BUTTON, self.extnd )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dbopn(self, event):
		self.dbfil = self.dbfile.GetPath().split('\\')[-1]
		#print(dbfil)
		self.idbfl = PG.Get(self.dbfil, u'', u'DBFields')
		self.dbdata = self.idbfl.GetFromDbf()
		#print(self.dbdata)
		self.DVC1.DeleteAllItems()
		self.filllist()
		self.chgmtd(None)


	def filllist(self):
		Droot = self.DVC1.GetRootItem()
		self.troot = self.DVC1.AppendItem(Droot,"Table")
		self.iroot = self.DVC1.AppendItem(Droot,"Indices")
		Tfilds, Indxss = AnalizdbText2(self.dbdata)
		#print(Tfilds)
		for tb in Tfilds:
			tbl = self.DVC1.AppendItem(self.troot, tb)
			for fld in Tfilds[tb]:
				ifld = self.DVC1.AppendItem(tbl, fld[0])
				self.DVC1.SetItemText(ifld, 0, fld[0])
				self.DVC1.SetItemText(ifld, 1, fld[1])



	def slctitm( self, event ):
		self.gtslt = self.DVC1.GetSelections()
		#print(self.gtslt)
		#itmtxt = self.DVC1.GetItemText(gtslt[0],0)

		#print(itmtxt)
		#cunt = len(gtslt)
		#print(cunt)

		#itmchd = self.DVC1.GetChildren()
		#print('GetChildern',itmchd)
		#print(itmchd[0].GetSelectedItemsCount())
		#frst = self.DVC1.GetFirstChild(gtslt[0])
		#nxtt = self.DVC1.GetNextItem(frst)
		#nxtt2 = self.DVC1.GetNextItem(nxtt)
		#print('1st child',self.DVC1.GetItemText(frst,0),self.DVC1.GetItemText(frst,1))
		#print('Nxt Child',self.DVC1.GetItemText(nxtt,0),self.DVC1.GetItemText(nxtt,1))
		#print('Nxt Itm',self.DVC1.GetItemText(nxtt2, 0),self.DVC1.GetItemText(nxtt2, 1))
		#wx.dataview.DataViewCtrl.GetSelectedItemsCount()


	def Addit( self, event ):
		print(self.gtslt[0])
		print(self.DVC1.GetItemText(self.gtslt[0],0))
		ItP = self.DVC1.GetItemParent(self.gtslt[0])
		ItC = self.DVC1.GetNextSibling(self.gtslt[0])
		print(ItC)
		print(self.DVC1.GetItemText(ItP,0))


	def edtit( self, event ):
		event.Skip()

	def delit( self, event ):
		event.Skip()

	def comit( self, event ):
		event.Skip()

	def recomt( self, event ):
		event.Skip()

	def brows( self, event ):
		event.Skip()


	def chgmtd( self, event ):
		inittxt = "#Add this lines to import part of program \nimport Database.PostGet as PG\n"
		inittxt2 = "#Please Add this line in body of Panel\n"
		dbf = self.dbfil
		if self.table != '':
			table = self.table
		else:
			table = u''
		if self.field != '':
			field = self.field
		else:
			field = u''
		if self.data != '':
			data = self.dbdat
		else:
			data = u''
		if self.sqfile != '':
			file = self.sqfile
		else:
			file = u''
		if self.chs1.GetStringSelection() == 'set':
			self.fldinit.SetValue(inittxt+inittxt2+f"\tMySet = PG.Post('{dbf}','{table}','{field}','{data}')\n".format(dbf,table,field,data))
		elif self.chs1.GetStringSelection() == 'get':
			self.fldinit.SetValue(inittxt+inittxt2+f"\tMyGet = PG.Get('{dbf}','{data}','{file}')\n".format(dbf,data,file))
		elif self.chs1.GetStringSelection() == 'both':
			self.fldinit.SetValue(inittxt+inittxt2+f"\tMySet = PG.Post('{dbf}','{table}','{field}','{data}')\n".format(dbf,table,field,data)
			                      +f"\tMyGet = PG.Get('{dbf}','{data}','{file}')\n".format(dbf,data,file))

		else:
			print('What method is')


	def prgstm( self, event ):
		event.Skip()

	def sqlstm( self, event ):
		event.Skip()

	def tocvs( self, event ):
		event.Skip()

	def toexl( self, event ):
		event.Skip()

	def extnd( self, event ):
		event.Skip()

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 232 )
		self.Splt1.Unbind( wx.EVT_IDLE )


