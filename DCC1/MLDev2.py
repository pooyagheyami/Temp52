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

from  Config.Init import *
import Res.Allicons as icon

import Database.PostGet as PG
import Database.MenuSet2 as MS

import importlib
import importlib.util

from AI.Analiz import *
import AI.OpnSrc as OS

_ = wx.GetTranslation

###########################################################################
## Class MyPanel9
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 555,480 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.getMData = MS.GetData(u'Menu2.db', u'')
		self.setMDate = MS.SetData(u'', u'', u'')

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.Titr1 = wx.StaticText( self.P1, wx.ID_ANY, _(u"Type of Machin Learning"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Titr1.Wrap( -1 )

		Vsz2.Add( self.Titr1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Hsz1 = wx.BoxSizer(wx.HORIZONTAL)

		#chis1Choices = [ u"Supervised Learning (11)",u"Semi-Supervised Learning (15)",u"Unsupervised Learning (21)",u"Reinforcement Learning (31)" ]
		chis1Choices = [l for l in OpenListML()[0].values()]
		self.chis1 = wx.Choice( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chis1Choices, 0 )
		self.chis1.SetSelection( 0 )
		#Vsz2.Add( self.chis1, 0, wx.ALL|wx.EXPAND, 5 )

		Hsz1.Add(self.chis1, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.MLset = wx.BitmapButton(self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
		                             wx.BU_AUTODRAW | 0)

		self.MLset.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_BUTTON))
		Hsz1.Add(self.MLset, 0, wx.ALL, 5)

		# Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		#
		# self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, u"Problem Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		# self.lbl1.Wrap( -1 )
		#
		# Hsz1.Add( self.lbl1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		#
		# chis2Choices = [ u"Regression Problem", u"Classification Problem" ]
		# self.chis2 = wx.Choice( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chis2Choices, 0 )
		# self.chis2.SetSelection( 0 )
		# Hsz1.Add( self.chis2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		#
		#
		Vsz2.Add( Hsz1, 0, wx.EXPAND, 5 )

		self.TLC1 = wx.dataview.TreeListCtrl(self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE)
		self.TLC1.AppendColumn(_(u"Learn Type"), 205, wx.ALIGN_LEFT, wx.COL_RESIZABLE)
		self.TLC1.AppendColumn(_(u"Method"), 45, wx.ALIGN_LEFT, wx.COL_RESIZABLE)

		Vsz2.Add(self.TLC1, 1, wx.EXPAND | wx.ALL, 5)

		self.filllist()

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.SlcDta = wx.Button(self.P1, wx.ID_ANY, _(u"Select Data"), wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz2.Add(self.SlcDta, 1, wx.ALL, 5)

		self.ConDta = wx.Button(self.P1, wx.ID_ANY, _(u"Conect Data"), wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz2.Add(self.ConDta, 1, wx.ALL, 5)

		Vsz2.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn1.SetBitmap(wx.Bitmap(ICON16_PATH + u'add.png', wx.BITMAP_TYPE_ANY))
		self.btn1.SetBitmap(icon.add.GetBitmap())
		self.btn1.SetToolTip(_(u"Add"))
		Hsz3.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn2.SetBitmap(wx.Bitmap(ICON16_PATH + u'edit_button.png', wx.BITMAP_TYPE_ANY))
		self.btn2.SetBitmap(icon.edit_button.GetBitmap())
		self.btn2.SetToolTip(_(u"Edit"))
		Hsz3.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn3.SetBitmap(wx.Bitmap(ICON16_PATH + u'delete.png', wx.BITMAP_TYPE_ANY))
		self.btn3.SetBitmap(icon.delete.GetBitmap())
		self.btn3.SetToolTip(_(u"Delete"))
		Hsz3.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn4.SetBitmap(wx.Bitmap(ICON16_PATH + u'brain_trainer.png', wx.BITMAP_TYPE_ANY))
		self.btn4.SetBitmap(icon.brain_trainer.GetBitmap())
		self.btn4.SetToolTip(_(u"Preview"))
		Hsz3.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn5.SetBitmap(wx.Bitmap(ICON16_PATH + u'update.png', wx.BITMAP_TYPE_ANY))
		self.btn5.SetBitmap(icon.update.GetBitmap())
		self.btn5.SetToolTip(_(u"Update"))
		Hsz3.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn6.SetBitmap(wx.Bitmap(ICON16_PATH + u'accept_button.png', wx.BITMAP_TYPE_ANY))
		self.btn6.SetBitmap(icon.accept_button.GetBitmap())
		self.btn6.SetToolTip(_(u"Apply"))
		Hsz3.Add( self.btn6, 0, wx.ALL, 5 )

		self.btn7 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'lightning.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetBitmap(icon.lightning.GetBitmap())
		self.btn7.SetToolTip(_(u"Generate"))
		Hsz3.Add( self.btn7, 0, wx.ALL, 5 )


		Vsz2.Add( Hsz3, 0, wx.EXPAND, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		Hsz15 = wx.BoxSizer( wx.HORIZONTAL )

		self.lblA = wx.StaticText( self.P2, wx.ID_ANY, _(u"Algorithm Pane Parameter "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblA.Wrap( -1 )

		Hsz15.Add( self.lblA, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Adbtn = wx.BitmapButton( self.P2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.Adbtn.SetBitmap(wx.Bitmap(ICON16_PATH + u'add.png', wx.BITMAP_TYPE_ANY))
		self.Adbtn.SetBitmap(icon.add.GetBitmap())
		Hsz15.Add( self.Adbtn, 0, wx.ALL, 5 )

		self.Edbtn = wx.BitmapButton( self.P2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.Edbtn.SetBitmap(wx.Bitmap(ICON16_PATH + u'edit_button.png', wx.BITMAP_TYPE_ANY))
		self.Edbtn.SetBitmap(icon.edit_button.GetBitmap())
		Hsz15.Add( self.Edbtn, 0, wx.ALL, 5 )

		self.Dlbtn = wx.BitmapButton( self.P2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		#self.Dlbtn.SetBitmap(wx.Bitmap(ICON16_PATH + u'delete.png', wx.BITMAP_TYPE_ANY))
		self.Dlbtn.SetBitmap(icon.delete.GetBitmap())
		Hsz15.Add( self.Dlbtn, 0, wx.ALL, 5 )


		Vsz3.Add( Hsz15, 0, wx.EXPAND, 5 )

		self.Lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.Lin1, 0, wx.EXPAND |wx.ALL, 5 )

		lstpane = self.getMData.MLPansFils(u' Join MLinfo on MLPane.MLPid = MLinfo.MLPid')
		Src_dir = self.getMData.GetImpCod('4444')[0][0]

		self.ChsBok = wx.Choicebook( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.PLP19 = []
		j = 0

		for lp in lstpane:
			print(lp)
			#i = importlib.import_module(u'GUI.MLPane.' + lp[1])
			i = importlib.import_module(Src_dir+'.' + lp[1])
			self.PLP19.append(i.P19(self.ChsBok))
			if j == 0:
				fp = True
			else:
				fp = False
			self.ChsBok.AddPage(self.PLP19[j], lp[3], fp)
			j += 1

		Vsz3.Add( self.ChsBok, 1, wx.EXPAND |wx.ALL, 5 )


		self.P2.SetSizer( Vsz3 )
		self.P2.Layout()
		Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 275 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.chis1.Bind( wx.EVT_CHOICE, self.typml )
		#self.chis2.Bind( wx.EVT_CHOICE, self.typpl )
		self.MLset.Bind(wx.EVT_BUTTON, self.MLsting)
		self.TLC1.Bind( wx.dataview.EVT_TREELIST_SELECTION_CHANGED, self.slctit )
		self.SlcDta.Bind(wx.EVT_BUTTON, self.selctdata)
		self.ConDta.Bind(wx.EVT_BUTTON, self.conctdata)
		#self.SrcShw.Bind( wx.EVT_BUTTON, self.srcml )
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.editit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.prw )
		self.btn5.Bind( wx.EVT_BUTTON, self.upd )
		self.btn6.Bind( wx.EVT_BUTTON, self.aply )
		self.btn7.Bind( wx.EVT_BUTTON, self.gnrt )
		self.Adbtn.Bind( wx.EVT_BUTTON, self.addAl )
		self.Edbtn.Bind( wx.EVT_BUTTON, self.edtAl )
		self.Dlbtn.Bind( wx.EVT_BUTTON, self.delAl )
		self.ChsBok.Bind( wx.EVT_CHOICEBOOK_PAGE_CHANGED, self.chgedpg )
		self.ChsBok.Bind( wx.EVT_CHOICEBOOK_PAGE_CHANGING, self.chgngpg )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def filllist(self):
		ch1 = self.chis1.GetStringSelection()
		#ch2 = self.chis2.GetSelection()
		coding,algcod = OpenListML()
		#support-vector machines, linear regression, logistic regression, neural networks, and nearest neighbor methods,
		#lstml = self.getMData.AllML()
		#print(lstml)
		#lstml1 = self.getMData.AllML(u' where MLinfo.MLPid < %d ' %11999)
		#print(ch1)
		for mcod in coding:
			if ch1 == coding[mcod]:
				#print(mcod)
				self.codings = mcod
				myfrng = mcod[0]
				mylrng = mcod[1]
		mylst = []
		for cod in algcod:
			if cod[0] > myfrng and cod[1] < mylrng:
				fcod = cod[0]
				tcod = cod[1]
				mylst = self.getMData.AllML(u' where MLinfo.MLPid < %d and MLinfo.MLPid >= %d' %(tcod,fcod))
			if mylst != []:
				Mroot = self.TLC1.GetRootItem()
				self.rootm = self.TLC1.AppendItem(Mroot, algcod[cod])

				for mtd in mylst:
					self.mlmtd = self.TLC1.AppendItem(self.rootm, u'Some Method')
					self.TLC1.SetItemText(self.mlmtd, 0, mtd[1])
					self.TLC1.SetItemText(self.mlmtd, 1, mtd[2])

	def MLsting(self, event):
		itxt = fil2txt(CONFIG_PATH+"MLmethod.ini")
		dlg = wx.Dialog(self, -1, "Setting of ML Coding")
		pnl = MyPanel3(dlg, CONFIG_PATH+"MLmethod.ini", itxt)
		dlg.SetSize((380,380))
		dlg.ShowModal()
		dlg.Destroy()

	def typml( self, event ):
		self.TLC1.DeleteAllItems()
		self.filllist()
		self.TLC1.Refresh()

	#def typpl( self, event ):
	#	event.Skip()

	def slctit( self, event ):
		event.Skip()

	def selctdata(self, event):
		dlg = wx.FileDialog(self, message=_("Choose Database"),
		                    defaultDir=os.getcwd(),
		                    defaultFile="",
		                    wildcard="Sqlite db file(*.db,*.sqlite,*,slite3,*.db3)|*.db;*.db3;*.sqlite|All file(*.*)|*.*",
		                    style=wx.FD_OPEN | wx.FD_CHANGE_DIR)

		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
		# print(paths)
		dlg.Destroy()

		frm = wx.Dialog(self, -1)
		pnl = MyPanel2(frm, paths[0])
		frm.SetSize((600, 300))
		frm.SetLabel(_(u'Select Table'))
		frm.ShowModal()
		self.flds = pnl.my_chois_fild
		self.idata = pnl.mydata

		frm.Destroy()
		chos = self.ChsBok.GetChoiceCtrl()

		#print(chos.GetSelection())
		#print(chos.GetString(chos.GetSelection()))
		#print(self.PLP19[chos.GetSelection()])
		pnl = self.PLP19[chos.GetSelection()]
		pnl.Sc1.SetValue(len(self.idata))
		pnl.idata = self.idata
		pnl.flds = self.flds
		# print(self.flds)
		# print(self.idata)
		# self.Sc1.SetValue(len(self.idata))
		# self.P19.Data = self.idata

		event.Skip()

	def conctdata(self, event):
		event.Skip()

	def srcml( self, event ):

		event.Skip()

	def addit( self, event ):
		newfile = GUI_PATH + 'Temp\\untitle.py'
		self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
		self.Pnl = OS.SrcPanel(self.Frm, newfile)
		self.Frm.SetMenuBar(OS.MyMenuBar1(u'ML'))
		self.Frm.SetSize((700, 500))
		self.Frm.SetLabel(u'untitle.py')
		self.Frm.Show()


		event.Skip()

	def editit( self, event ):
		myslct = self.TLC1.GetSelection()
		myalg = self.TLC1.GetItemText(myslct, 1)
		# print(myalg)
		thsfile = self.getMData.MLPansgetAl(myalg)[0][1]

		self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
		self.Pnl = OS.SrcPanel(self.Frm, SRC_PATH + 'mla\\' + thsfile + '.py')
		self.Frm.SetMenuBar(OS.MyMenuBar1(u'ML'))
		self.Frm.SetSize((700, 500))
		self.Frm.SetLabel(SRC_PATH + 'mla\\' + thsfile+'.py')
		self.Frm.Show()
		event.Skip()

	def delit( self, event ):
		event.Skip()

	def prw( self, event ):
		event.Skip()

	def upd( self, event ):
		event.Skip()

	def aply( self, event ):
		event.Skip()

	def gnrt( self, event ):
		event.Skip()

	def addAl( self, event ):
		self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
		#self.Pnl = PyPanel(self.Frm, GUI_PATH + 'Temp\\untitle.py')
		self.Pnl = OS.SrcPanel(self.Frm, GUI_PATH + 'MLPane\\Untitle.py')
		self.Frm.SetMenuBar(OS.MyMenuBar1(u'AL'))
		self.Frm.SetSize((700, 560))
		self.Frm.SetLabel(u'untitle.py')
		self.Frm.Show()
		event.Skip()

	def edtAl( self, event ):
		chos = self.ChsBok.GetChoiceCtrl()
		ipg = self.ChsBok.GetSelection()
		chname = chos.GetString(ipg)
		#print(chos.GetString(chos.GetSelection()),chname)
		#print(ipg)
		Pnlid = self.getMData.MLPanid(chname)[0][0]
		#print(Pnlid)
		Pnlfil = self.getMData.MLPansFils(u' where MLPane.MLPid = %d '%Pnlid)[0][1]
		#print(Pnlfil)
		self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
		#self.Pnl = PyPanel(self.Frm, GUI_PATH + 'MLPane\\'+Pnlfil+u'.py')
		self.Pnl = OS.SrcPanel(self.Frm, SRC_PATH + 'mlp\\' + Pnlfil + u'.py')
		self.Frm.SetMenuBar(OS.MyMenuBar1(u'AL'))
		self.Frm.SetSize((700, 560))
		self.Frm.SetLabel(SRC_PATH + 'mlp\\' + Pnlfil + u'.py')
		self.Frm.Show()
		event.Skip()

	def delAl( self, event ):
		event.Skip()

	def chgedpg( self, event ):
		event.Skip()

	def chgngpg( self, event ):
		event.Skip()

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 275 )
		self.Splt1.Unbind( wx.EVT_IDLE )


###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):

	def __init__( self, parent,dbfile, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 667,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz = wx.BoxSizer( wx.VERTICAL )
		self.dbfile = dbfile.split('\\')[-1]
		self.idbfl = PG.Get(self.dbfile, u'', u'DBFields')
		self.dbdata = self.idbfl.GetFromDbf()

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
		self.filds = self.idbfl.GetFromString(u"Select * from %s " % Table)

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


###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):

	def __init__( self, parent, fileini, txtini, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 382,381 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz = wx.BoxSizer( wx.VERTICAL )

		self.titr = wx.StaticText( self, wx.ID_ANY, fileini, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr.Wrap( -1 )

		Vsz.Add( self.titr, 0, wx.ALL|wx.EXPAND, 5 )

		self.inifil = wx.TextCtrl( self, wx.ID_ANY, txtini, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_WORDWRAP )
		Vsz.Add( self.inifil, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( Vsz )
		self.Layout()

	def __del__( self ):
		pass

