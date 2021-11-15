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

		self.fldprg = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_WORDWRAP )
		Vsz3.Add( self.fldprg, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self.P2, wx.ID_ANY, u"SQL  Statments", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl5.Wrap( -1 )

		Hsz4.Add( self.lbl5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btnss = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz4.Add( self.btnss, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz4, 0, wx.EXPAND, 5 )

		self.fldsql = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_WORDWRAP )
		Vsz3.Add( self.fldsql, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.btncv = wx.Button( self.P2, wx.ID_ANY, u"To CVS", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.btncv, 0, wx.ALL, 5 )

		self.btnxl = wx.Button( self.P2, wx.ID_ANY, u"To Excel", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.btnxl, 0, wx.ALL, 5 )

		self.btnex = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnex.SetToolTip( u"Extended" )

		Hsz5.Add( self.btnex, 0, wx.ALL, 5 )

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
		self.DVC1.Bind(wx.dataview.EVT_TREELIST_ITEM_CHECKED, self.chkit)
		self.btn1.Bind( wx.EVT_BUTTON, self.insit )
		self.btn2.Bind( wx.EVT_BUTTON, self.updit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.jinit )
		self.btn5.Bind( wx.EVT_BUTTON, self.brwit )
		self.btn6.Bind( wx.EVT_BUTTON, self.aplit )
		self.btn7.Bind( wx.EVT_BUTTON, self.gnrit )

		self.chs1.Bind( wx.EVT_CHOICE, self.chgmtd )
		self.btnps.Bind( wx.EVT_BUTTON, self.prgstm )
		self.btnss.Bind( wx.EVT_BUTTON, self.sqlstm )
		self.btncv.Bind( wx.EVT_BUTTON, self.tocvs )
		self.btnxl.Bind( wx.EVT_BUTTON, self.toexl )
		self.btnex.Bind( wx.EVT_BUTTON, self.extnd )

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
		self.Tfilds, self.Indxss = AnalizdbText2(self.dbdata)
		#print(Tfilds)
		for tb in self.Tfilds:
			tbl = self.DVC1.AppendItem(self.troot, tb)
			for fld in self.Tfilds[tb]:
				ifld = self.DVC1.AppendItem(tbl, fld[0])
				self.DVC1.SetItemText(ifld, 0, fld[0])
				self.DVC1.SetItemText(ifld, 1, fld[1])


	def chkit(self, event):
		self.gtslt = self.DVC1.GetSelections()
		itmtxt = self.DVC1.GetItemText(self.gtslt[0], 0)
		if itmtxt in [f[0] for fl in self.Tfilds.values() for f in fl ]:
			prnt = self.DVC1.GetItemParent(self.gtslt[0])
			if self.DVC1.AreAllChildrenInState(prnt,1):
				self.DVC1.CheckItem(prnt, 1)
			else:
				self.DVC1.CheckItem(prnt, 2)
			#if self.Tfilds[self.DVC1.GetItemText(prnt, 0)]
			#print(self.DVC1.AreAllChildrenInState(prnt,1))
		if itmtxt in self.Tfilds:
			flds = [f[0] for f in self.Tfilds[itmtxt]]
			if self.DVC1.GetCheckedState(self.gtslt[0]) == 1:
				self.DVC1.CheckItemRecursively(self.gtslt[0], 1)
			elif self.DVC1.GetCheckedState(self.gtslt[0]) == 0:
				self.DVC1.CheckItemRecursively(self.gtslt[0], 0)



	def ChkTicks(self):
		frstitm = self.DVC1.GetRootItem()
		nxitm = self.DVC1.GetNextItem(frstitm)
		tbltiklst = {}
		fldtiklst = []
		#print(self.DVC1.GetItemText(nxitm, 0),self.DVC1.GetCheckedState(nxitm))
		# if self.DVC1.GetCheckedState(frstitm):
		# 	self.DVC1.CheckItemRecursively(frstitm,1)
		# else:
		# 	self.DVC1.UncheckItem(frstitm)
		for fld in self.Tfilds:
			nxitm = self.DVC1.GetNextItem(nxitm)
			tblnm = u''
			if self.DVC1.GetCheckedState(nxitm):
				tblnm = self.DVC1.GetItemText(nxitm, 0)
			fldtiklst = []
			for f in self.Tfilds[fld]:
				nxitm = self.DVC1.GetNextItem(nxitm)
				if self.DVC1.GetCheckedState(nxitm):
					fldtiklst.append(self.DVC1.GetItemText(nxitm, 0))
				#tbltiklst.append(self.DVC1.GetItemText(nxitm, 0))
			if tblnm != u'':
				tbltiklst[tblnm] = fldtiklst

		return tbltiklst

	def insit( self, event ):
		#self.gtslt = self.DVC1.GetSelections()
		#itmtxt = self.DVC1.GetItemText(self.gtslt[0], 0)
		sqlsnts = self.ChkTicks()
		txt = u''
		for tbl in sqlsnts.keys():
			txt += '\n'
			txt += u'\tself.MySet.Tabel = %s \n'%tbl
			fild = u''
			for fld in sqlsnts.get(tbl):
				fild += fld + ','
			txt += u'\t#AllData = ['
			for d in range(len(sqlsnts.get(tbl))):
				txt += u' Data%d' %d + ','
			txt = txt.rstrip(',')
			txt += u'] #You can add data to put here\n'
			txt += u'\tself.MySet.Addrecord( " '+fild.rstrip(',')+ u' ", AllData )\n'

		#print(txt)
		self.fldprg.SetValue(txt)

	def updit( self, event ):
		sqlsnts = self.ChkTicks()
		smfild = [ f for fld in sqlsnts.values() for f in fld ]
		#print(sqlsnts,'\n',smfild)
		frm = wx.Dialog(self, -1)
		pnl = MyPanel3(frm, smfild)
		frm.SetSize((400, 125))
		frm.SetLabel(u'Select Key feild')
		frm.ShowModal()
		if pnl.acept:
			choic = pnl.chs2.GetStringSelection()

		frm.Destroy()
		txt = u''
		for tbl in sqlsnts.keys():
			txt += '\n'
			txt += u'\tself.MySet.Tabel = %s \n' % tbl
			fild = u''
			contor = 0
			for fld in sqlsnts.get(tbl):
				if fld != choic:
					fild += fld + '=? ,'
					contor += 1
			txt += u'\t#AllData = ['
			Data = u''
			for d in range(contor):
				Data += u' Data%d' %d + ','
			Data = Data.rstrip(',')
			#print(Data)
			txt += Data + u'] #You can add data to put here\n'
			txt += u'\t#self.KeyData = #can put need data here\n'
			txt += u'\tself.MySet.Updaterecord( " ' + fild.rstrip(',')
			txt += ' Where '+ choic + ' = %s " %self.KeyData , AllData )\n'

		self.fldprg.SetValue(txt)

		event.Skip()

	def delit( self, event ):
		sqlsnts = self.ChkTicks()
		smfild = [f for fld in sqlsnts.values() for f in fld]
		# print(sqlsnts,'\n',smfild)
		frm = wx.Dialog(self, -1)
		pnl = MyPanel3(frm, smfild)
		frm.SetSize((400, 125))
		frm.SetLabel(u'Select Key feild')
		frm.ShowModal()
		if pnl.acept:
			choic = pnl.chs2.GetStringSelection()

		frm.Destroy()
		txt = u''
		for tbl in sqlsnts.keys():
			txt += '\n'
			txt += u'\tself.MySet.Tabel = %s \n' % tbl

			txt += u'\t#self.KeyData = #can put need data here\n'
			txt += u'\tself.MySet.Deleterecord( " ' #+ fild.rstrip(',')
			txt += choic + ' = %s " %self.KeyData ) \n'
			#txt += ' Where ' + choic + ' = %s " %self.KeyData , AllData )\n'

		self.fldprg.SetValue(txt)
		event.Skip()

	def jinit( self, event ):
		#print(self.ChkTicks())
		sqlsnts = self.ChkTicks()
		Join = ''
		Jkey = []
		Tbls = [T for T in sqlsnts.keys()]
		Bchs = False
		Btbl = u''
		for i in range(len(Tbls)-1):
			frm = wx.Dialog(self, -1)
			pnl = MyPanel5(frm, sqlsnts)
			frm.SetSize((550, 155))
			frm.SetLabel(u'Select Key feild')
			if Bchs:
				pnl.chs1.SetStringSelection(Btbl)
				pnl.chs1.Disable()
				pnl.chs2.SetItems([Btbl+'.'+f for f in sqlsnts[Btbl]])
				pnl.chs3.SetItems([Tbls[0]+'.'+f for f in sqlsnts[Tbls[0]]] )
			frm.ShowModal()
			if pnl.acept:
				if i == 0:
					Btbl = pnl.chs1.GetStringSelection()
					Tbls.remove(Btbl)
					Bchs = True
				else:
					pass
				Jkey.append(pnl.chs2.GetStringSelection()+' = '+pnl.chs3.GetStringSelection())
				Jslc = pnl.chs3.GetStringSelection().split('.')[0]
				Tbls.remove(Jslc)
				#print(Tbls,Jslc)
			else:
				break
			frm.Destroy()
		#print(Btbl, Jkey)
		Join += " Select "
		Fields = [T+'.'+F for T in sqlsnts.keys() for F in sqlsnts[T]]
		#print(Fields)
		for Fld in Fields:
			Join += Fld + ' ,'
		Join = Join.rstrip(',')
		Join += " From "+Btbl+"\n"
		for J in Jkey:
			Join += " Inner Join " + J.split('=')[-1].split('.')[0] + " On " + J + "\n"
		#print(Join)
		self.fldsql.SetValue(Join)

		#self.fldsql.SetValue(sqltxt)

	def brwit( self, event ):
		self.gtslt = self.DVC1.GetSelections()
		myfild = self.DVC1.GetItemText(self.gtslt[0], 0)
		for fld in self.Tfilds:
			if myfild == fld:
				thsfld = [f[0] for f in self.Tfilds[fld]]
		frm = wx.Dialog(self, -1)
		pnl = MyPanel2(frm, self.dbfil,thsfld, myfild)
		frm.SetSize((600, 300))
		frm.SetLabel(u'Select Table')
		frm.ShowModal()

		frm.Destroy()

	def aplit( self, event ):
		event.Skip()

	def gnrit( self, event ):
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
			self.fldinit.SetValue(inittxt+inittxt2+f"\tself.MySet = PG.Post('{dbf}','{table}','{field}','{data}')\n".format(dbf,table,field,data))
		elif self.chs1.GetStringSelection() == 'get':
			self.fldinit.SetValue(inittxt+inittxt2+f"\tself.MyGet = PG.Get('{dbf}','{data}','{file}')\n".format(dbf,data,file))
		elif self.chs1.GetStringSelection() == 'both':
			self.fldinit.SetValue(inittxt+inittxt2+f"\tself.MySet = PG.Post('{dbf}','{table}','{field}','{data}')\n".format(dbf,table,field,data)
			                      +f"\tself.MyGet = PG.Get('{dbf}','{data}','{file}')\n".format(dbf,data,file))
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


###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):

	def __init__( self, parent, DBF, fields, Table, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz = wx.BoxSizer( wx.VERTICAL )
		self.DBF = DBF.split('\\')[-1]

		self.idbfl = PG.Get(self.DBF, u'', u'')
		self.idata = self.idbfl.GetFromString(u' select * from %s' %Table)

		self.DVC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_VERT_RULES )
		#self.fld1 = self.DVC1.AppendTextColumn( u"Name", 0, wx.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.DATAVIEW_COL_RESIZABLE )
		#self.fld2 = self.DVC1.AppendTextColumn( u"Name", 0, wx.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.DATAVIEW_COL_RESIZABLE )
		Vsz.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		#for Col in range(len(self.idata[0])):
		#	self.DVC1.AppendTextColumn(u"field", -1 )
		for Col in fields:
			self.DVC1.AppendTextColumn(Col, -1 )

		for data in self.idata:
			DD = ()
			for d in data:
				DD = DD + (str(d),)
			self.DVC1.AppendItem(DD)


		self.m_button8 = wx.Button( self, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( Vsz )
		self.Layout()

		# Connect Events
		self.m_button8.Bind( wx.EVT_BUTTON, self.cols )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cols( self, event ):
		q = self.GetParent()
		q.Close()


###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):

	def __init__( self, parent,fldlst, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 396,124 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"Key of Field UpDate", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs2Choices = fldlst
		self.chs2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs2Choices, 0 )
		self.chs2.SetSelection( 0 )
		Hsz2.Add( self.chs2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.codfld = wx.TextCtrl(self, wx.ID_ANY, u"SomeData", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
		Hsz2.Add(self.codfld, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )


		Hsz3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Cancle or Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"Ok or Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.cncl )
		self.btn2.Bind( wx.EVT_BUTTON, self.aply )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cncl( self, event ):
		self.acept = False
		q = self.GetParent()
		q.Close()

	def aply( self, event ):
		self.acept = True
		q = self.GetParent()
		q.Close()

###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):

	def __init__( self, parent,tabls, flds1, flds2, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,175 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"Base Table For Join", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.lbl1.Wrap( -1 )

		Hsz1.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs1Choices = tabls
		self.chs1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs1Choices, 0 )
		self.chs1.SetSelection( 0 )
		Hsz1.Add( self.chs1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"Key of Field For Join", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs2Choices = flds1
		self.chs2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs2Choices, 0 )
		self.chs2.SetSelection( 0 )
		Hsz2.Add( self.chs2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs3Choices = flds2
		self.chs3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs3Choices, 0 )
		self.chs3.SetSelection( 0 )
		Hsz2.Add( self.chs3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		#self.chk1 = wx.CheckBox( self, wx.ID_ANY, u"Use All field", wx.DefaultPosition, wx.DefaultSize, 0 )
		#Hsz3.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Hsz3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Cancle & Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"Ok & Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		#self.chk1.Bind( wx.EVT_CHECKBOX, self.chkall )
		self.btn1.Bind( wx.EVT_BUTTON, self.cncl )
		self.btn2.Bind( wx.EVT_BUTTON, self.aply )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	#def chkall( self, event ):
	#	event.Skip()

	def cncl( self, event ):
		self.acept = False
		q = self.GetParent()
		q.Close()

	def aply( self, event ):
		self.acept = True
		q = self.GetParent()
		q.Close()

###########################################################################
## Class MyPanel5
###########################################################################

class MyPanel5 ( wx.Panel ):

	def __init__( self, parent, Data, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,145 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Data = Data

		Btbl = [T for T in Data.keys()]
		Bfld = [Btbl[0] + '.' + F for F in Data[Btbl[0]]]
		Jfld = [Btbl[1] + '.' + F for F in Data[Btbl[1]]]

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"Base Table For Join", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.lbl1.Wrap( -1 )

		Hsz1.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs1Choices = Btbl
		self.chs1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs1Choices, 0 )
		self.chs1.SetSelection( 0 )
		Hsz1.Add( self.chs1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"Key of Field For Join", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs2Choices = Bfld
		self.chs2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs2Choices, 0 )
		self.chs2.SetSelection( 0 )
		Hsz2.Add( self.chs2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs3Choices = Jfld
		self.chs3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs3Choices, 0 )
		self.chs3.SetSelection( 0 )
		Hsz2.Add( self.chs3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )


		Hsz3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Cancle & Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"Ok & Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.chs1.Bind(wx.EVT_CHOICE, self.tblch)
		self.btn1.Bind( wx.EVT_BUTTON, self.cncl )
		self.btn2.Bind( wx.EVT_BUTTON, self.aply )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tblch(self, event):
		n = self.chs1.GetSelection()
		#c = self.chs1.GetCount()
		#print(n,c)
		T1 = self.chs1.GetStringSelection()
		fld1 = self.Data[T1]
		self.chs2.SetItems([T1+'.'+f for f in fld1])
		if n  == 0:
			m = 1
		else:
			m = 0
		T2 = self.chs1.GetString(m)
		fld2 = self.Data[T2]
		self.chs3.SetItems([T2+'.'+f for f in fld2])

		event.Skip()

	def cncl( self, event ):
		self.acept = False
		q = self.GetParent()
		q.Close()

	def aply( self, event ):
		self.acept = True
		q = self.GetParent()
		q.Close()


