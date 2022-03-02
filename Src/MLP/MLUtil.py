#In the name of God
#Utility for Machin Learning Panel Parameter and Algorithms
# -*- coding: utf-8 -*-

import wx
import wx.dataview
from Config.Init import *

import Database.PostGet as PG
import Database.PostGet2 as PG2
import Database.MenuSet2 as MS

from AI.Analiz import *
import AI.OpnSrc as OS

_ = wx.GetTranslation
###########################################################################
## Class Yselect
###########################################################################


class Yselect ( wx.Panel ):

	def __init__( self, parent,felds, data, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 498,215 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.VLC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		for f1 in felds:
			self.VLC1.AppendTextColumn(f1, width=-1, align=wx.ALIGN_LEFT)

		for dt in data:
			DD = ()
			for d in dt:
				DD = DD + (str(d),)
			self.VLC1.AppendItem(DD)


		Hsz1.Add( self.VLC1, 1, wx.ALL|wx.EXPAND, 5 )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		RB1Choices = felds
		self.RB1 = wx.RadioBox( self, wx.ID_ANY, u"What of this y", wx.DefaultPosition, wx.DefaultSize, RB1Choices, 1, wx.RA_SPECIFY_COLS )
		self.RB1.SetSelection( 0 )
		Vsz1.Add( self.RB1, 1, wx.ALL, 5 )

		self.btn = wx.Button( self, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz1.Add( self.btn, 0, wx.ALL, 5 )


		Hsz1.Add( Vsz1, 0, wx.EXPAND, 5 )


		self.SetSizer( Hsz1 )
		self.Layout()

		# Connect Events
		self.RB1.Bind(wx.EVT_RADIOBOX, self.thisy)
		self.btn.Bind( wx.EVT_BUTTON, self.clos )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def thisy(self, event):
		yfld = self.RB1.GetSelection()
		#print(yfld)
		colpos = yfld
		icol = self.VLC1.GetColumn(yfld)
		#print(colpos)
		xvalu = []
		yvalu = []
		for r in range(self.VLC1.GetItemCount()):
			yvalu.append( self.VLC1.GetValue(r,colpos) )
		for r in range(self.VLC1.GetItemCount()):
			xcol = [1]
			for c in range(self.VLC1.GetColumnCount()):
				if c != colpos:
					xcol.append(self.VLC1.GetValue(r,c))
			xvalu.append(xcol)
		self.xMtrx = xvalu
		self.yMtrx = yvalu
		#print(xvalu)
		#print(yvalu)
		event.Skip()

	def clos( self, event ):
		q = self.GetParent()
		q.Close()
		event.Skip()

###########################################################################
## Class ShowMatrix
###########################################################################

class ShowMatrix ( wx.Panel ):

	def __init__( self, parent, Matrx, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,180 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz = wx.BoxSizer( wx.VERTICAL )
		iMatrix = '[\n'
		mlst = Matrx.tolist()
		#mshp = np.matrix.shape
		#print(mlst)
		#print(mshp)

		for r in range(len(mlst)):
			iMatrix += '['
			for c in range(len(mlst[r])):
				#print(mlst[r][c])
				iMatrix += str(mlst[r][c])+'  '
			iMatrix += ']\n'
		iMatrix += ']'


		self.Txt = wx.TextCtrl( self, wx.ID_ANY, iMatrix, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Vsz.Add( self.Txt, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn = wx.Button( self, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz.Add( self.btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( Vsz )
		self.Layout()

		# Connect Events
		self.btn.Bind( wx.EVT_BUTTON, self.okit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def okit( self, event ):
		q = self.GetParent()
		q.Close()
		event.Skip()

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):

	def __init__( self, parent,dbfile, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 667,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz = wx.BoxSizer( wx.VERTICAL )
		self.config = wx.GetApp().GetConfig()
		dbftype = Database_type[int(self.config.Read('DBtype'))]

		#self.dbfile = dbfile.split('\\')[-1]
		#self.idbfl = PG.Get(self.dbfile, u'', u'DBFields')
		self.idbfl2 = PG2.Get(dbfile, dbftype)
		conn = self.idbfl2.myengin.connect()
		Rprox = conn.execute('select * from sqlite_master')
		# print(Rprox.fetchall())
		self.dbdata = Rprox.fetchall()
		#self.dbdata = self.idbfl.GetFromDbf()

		Tfilds, Indxss = AnalizdbText2(self.dbdata)

		self.TablesChoices = [Tb for Tb in Tfilds]
		self.Tables = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.TablesChoices, 0 )
		self.Tables.SetSelection( 0 )
		Vsz.Add( self.Tables, 0, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer(wx.HORIZONTAL)
		#print(self.TablesChoices)
		self.fillist(self.TablesChoices[0])

		self.DLC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add(self.DLC1, 1, wx.ALL | wx.EXPAND, 5)

		FLst1Choices = self.fldlst
		self.FLst1 = wx.CheckListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, FLst1Choices,
		                             wx.LB_ALWAYS_SB | wx.LB_HSCROLL )
		Hsz1.Add(self.FLst1, 0, wx.ALL | wx.EXPAND, 5)


		self.filldata()


		Vsz.Add( Hsz1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer(wx.HORIZONTAL)

		self.btn2 = wx.Button(self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz2.Add(self.btn2, 0, wx.ALL, 5)

		self.btn1 = wx.Button(self, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz2.Add(self.btn1, 0, wx.ALL, 5)

		Vsz.Add(Hsz2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)


		self.SetSizer( Vsz )
		self.Layout()

		# Connect Events
		self.Tables.Bind(wx.EVT_CHOICE, self.chng)
		self.DLC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctit, id = wx.ID_ANY )
		#self.DLC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.domenu, id = wx.ID_ANY )
		self.DLC1.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.slctit, id = wx.ID_ANY )
		self.btn2.Bind(wx.EVT_BUTTON, self.cancl)
		self.btn1.Bind(wx.EVT_BUTTON, self.aplyit)

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def fillist(self, Table):
		#print(type(Table))
		self.filds = []
		Tfilds, Indxss = AnalizdbText2(self.dbdata)
		#self.filds = self.idbfl.GetFromString(u"Select * from %s " % Table)
		self.filds = self.idbfl2.GetFromString(u"Select * from %s " % Table)
		#print(self.filds, Tfilds[Table])
		#print([fld[0] for fld in Tfilds[Table]])
		self.fldlst = [fld[0] for fld in Tfilds[Table]]


	def filldata(self):
		self.DLC1.ClearColumns()
		self.DLC1.DeleteAllItems()

		for f1 in self.fldlst:
			self.DLC1.AppendTextColumn(f1, width=-1, align=wx.ALIGN_LEFT)

		for data in self.filds:
			DD = ()
			for d in data:
				DD = DD + (str(d),)
			self.DLC1.AppendItem(DD)

	def chng(self, event):
		ichos = self.Tables.GetSelection()
		#print(self.TablesChoices[ichos])
		self.fillist(self.TablesChoices[ichos])
		self.filldata()
		#print(self.FLst1.GetItems())
		self.FLst1.Clear()
		self.FLst1.SetItems(self.fldlst)
		event.Skip()

	def slctit( self, event ):
		event.Skip()

	def cancl( self, event ):
		q = self.GetParent()
		q.Close()
		#event.Skip()

	def aplyit( self, event ):
		self.mydata = []
		#self.my_chois_fild = self.FLst1.GetCheckedItems()
		self.my_chois_fild = self.FLst1.GetCheckedStrings()
		for data in self.filds:
			DD = ()
			for ii in range(len(data)):
				if ii in  self.FLst1.GetCheckedItems():
					DD = DD + (data[ii],)
			self.mydata.append(DD)

		q = self.GetParent()
		q.Close()
		event.Skip()
