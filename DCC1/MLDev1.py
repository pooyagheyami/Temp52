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

import Database.PostGet as PG
import Database.MenuSet2 as MS

import importlib
import importlib.util

from AI.Analiz import *
from AI.ML.SL_Reg import *


import numpy as np
from matplotlib import pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

###########################################################################
## Class MyPanel7
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 555,481 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.getMData = MS.GetData(u'Menu2.db', u'')
		self.setMDate = MS.SetData(u'', u'', u'')

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.Titr1 = wx.StaticText( self.P1, wx.ID_ANY, u"Type of Machin Learning", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Titr1.Wrap( -1 )

		Vsz2.Add( self.Titr1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		chis1Choices = [ u"Supervised Learning", u"Unsupervised Learning" ]
		self.chis1 = wx.Choice( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chis1Choices, 0 )
		self.chis1.SetSelection( 0 )
		Vsz2.Add( self.chis1, 0, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, u"Problem Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Hsz1.Add( self.lbl1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chis2Choices = [ u"Regression Problem", u"Classification Problem" ]
		self.chis2 = wx.Choice( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chis2Choices, 0 )
		self.chis2.SetSelection( 0 )
		Hsz1.Add( self.chis2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz2.Add( Hsz1, 0, wx.EXPAND, 5 )

		self.TLC1 = wx.dataview.TreeListCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.TLC1.AppendColumn( u"Learn Type", 205, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.TLC1.AppendColumn( u"Method", 45, wx.ALIGN_LEFT, wx.COL_RESIZABLE )

		Vsz2.Add( self.TLC1, 1, wx.EXPAND |wx.ALL, 5 )

		self.filllist()

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.SrcShw = wx.Button( self.P1, wx.ID_ANY, u"minimizing :Show Cust Function Source", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.SrcShw, 1, wx.ALL, 5 )


		Vsz2.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn1.SetBitmap(wx.Bitmap(ICON16_PATH + u'add.png', wx.BITMAP_TYPE_ANY))
		self.btn1.SetToolTip(u"Add")
		Hsz3.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn2.SetBitmap(wx.Bitmap(ICON16_PATH + u'edit_button.png', wx.BITMAP_TYPE_ANY))
		self.btn2.SetToolTip(u"Edit")
		Hsz3.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn3.SetBitmap(wx.Bitmap(ICON16_PATH + u'delete.png', wx.BITMAP_TYPE_ANY))
		self.btn3.SetToolTip(u"Delete")
		Hsz3.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn4.SetBitmap(wx.Bitmap(ICON16_PATH + u'brain_trainer.png', wx.BITMAP_TYPE_ANY))
		self.btn4.SetToolTip(u"Preview")
		Hsz3.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn5.SetBitmap(wx.Bitmap(ICON16_PATH + u'update.png', wx.BITMAP_TYPE_ANY))
		self.btn5.SetToolTip(u"Update")
		Hsz3.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn6.SetBitmap(wx.Bitmap(ICON16_PATH + u'accept_button.png', wx.BITMAP_TYPE_ANY))
		self.btn6.SetToolTip(u"Apply")
		Hsz3.Add( self.btn6, 0, wx.ALL, 5 )

		self.btn7 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'lightning.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetToolTip(u"Generate")
		Hsz3.Add( self.btn7, 0, wx.ALL, 5 )


		Vsz2.Add( Hsz3, 0, wx.EXPAND, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.Titr2 = wx.StaticText(self.P2, wx.ID_ANY, u"Algorithm", wx.DefaultPosition, wx.DefaultSize, 0)
		self.Titr2.Wrap(-1)

		self.Vsz3.Add(self.Titr2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		Hsz11 = wx.BoxSizer(wx.HORIZONTAL)

		self.lblm = wx.StaticText(self.P2, wx.ID_ANY, u"m =  ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lblm.Wrap(-1)

		Hsz11.Add(self.lblm, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Sc1 = wx.SpinCtrl(self.P2, wx.ID_ANY, u"m", wx.DefaultPosition, wx.Size(60, -1), wx.SP_ARROW_KEYS, 0, 9999,
		                       0)
		Hsz11.Add(self.Sc1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.lbl2 = wx.StaticText(self.P2, wx.ID_ANY, u"Number of training", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl2.Wrap(-1)

		Hsz11.Add(self.lbl2, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.btnm = wx.Button(self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
		Hsz11.Add(self.btnm, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Vsz3.Add(Hsz11, 0, wx.EXPAND, 5)

		Hsz12 = wx.BoxSizer(wx.HORIZONTAL)

		self.lblx = wx.StaticText(self.P2, wx.ID_ANY, u"x (Input/features)=  ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lblx.Wrap(-1)

		Hsz12.Add(self.lblx, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.fldx = wx.TextCtrl(self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz12.Add(self.fldx, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.btnx = wx.Button(self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
		Hsz12.Add(self.btnx, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
		self.btnx.SetToolTip(u"Independent variable")
		self.Vsz3.Add(Hsz12, 0, wx.EXPAND, 5)

		Hsz13 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbly = wx.StaticText(self.P2, wx.ID_ANY, u"y (Output/target)=  ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbly.Wrap(-1)

		Hsz13.Add(self.lbly, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.fldy = wx.TextCtrl(self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz13.Add(self.fldy, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.btny = wx.Button(self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
		Hsz13.Add(self.btny, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
		self.btny.SetToolTip(u"Dependent variable")
		self.Vsz3.Add(Hsz13, 0, wx.EXPAND, 5)

		Hsz14 = wx.BoxSizer(wx.HORIZONTAL)


		self.lblt = wx.StaticText(self.P2, wx.ID_ANY, u"Shows plot of Data you enter", wx.DefaultPosition,
		                          wx.DefaultSize, 0)
		self.lblt.Wrap(-1)

		Hsz14.Add(self.lblt, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.btntt = wx.Button(self.P2, wx.ID_ANY, u"Show Plot", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
		Hsz14.Add(self.btntt, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Vsz3.Add(Hsz14, 0, wx.EXPAND, 5)

		self.lin1 = wx.StaticLine(self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
		self.Vsz3.Add(self.lin1, 0, wx.EXPAND | wx.ALL, 5)

		#self.lblA = wx.StaticText(self.P2, wx.ID_ANY, u"Use This Algorithm and Show Result", wx.DefaultPosition,
		#                          wx.DefaultSize, 0)
		#self.lblA.Wrap(-1)

		#Vsz3.Add(self.lblA, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
		Hsz15 = wx.BoxSizer(wx.HORIZONTAL)

		self.lblA = wx.StaticText(self.P2, wx.ID_ANY, u"Algorithm Here", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lblA.Wrap(-1)

		Hsz15.Add(self.lblA, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Adbtn = wx.BitmapButton(self.P2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,wx.BU_AUTODRAW | 0)
		self.Adbtn.SetBitmap(wx.Bitmap(ICON16_PATH + u'add.png', wx.BITMAP_TYPE_ANY))
		Hsz15.Add(self.Adbtn, 0, wx.ALL, 5)

		self.Edbtn = wx.BitmapButton(self.P2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,wx.BU_AUTODRAW | 0)
		self.Edbtn.SetBitmap(wx.Bitmap(ICON16_PATH + u'edit_button.png', wx.BITMAP_TYPE_ANY))
		Hsz15.Add(self.Edbtn, 0, wx.ALL, 5)

		self.Dlbtn = wx.BitmapButton(self.P2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,wx.BU_AUTODRAW | 0)
		self.Dlbtn.SetBitmap(wx.Bitmap(ICON16_PATH + u'delete.png', wx.BITMAP_TYPE_ANY))
		Hsz15.Add(self.Dlbtn, 0, wx.ALL, 5)

		self.Vsz3.Add(Hsz15, 0, wx.EXPAND, 5)


		#self.P19 = Pnl.P19_1(self.P2)
		#self.P19 = wx.Panel(self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_RAISED | wx.TAB_TRAVERSAL)
		self.Vsp19 = wx.BoxSizer(wx.VERTICAL)



		self.P2.SetSizer( self.Vsz3 )
		self.P2.Layout()
		self.Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 275 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.TLC1.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.slcchng, id=wx.ID_ANY)
		self.chis1.Bind(wx.EVT_CHOICE, self.typml)
		self.chis2.Bind(wx.EVT_CHOICE, self.typpl)
		self.SrcShw.Bind(wx.EVT_BUTTON, self.srcml)
		self.btn1.Bind(wx.EVT_BUTTON, self.addit)
		self.btn2.Bind(wx.EVT_BUTTON, self.editit)
		self.btn3.Bind(wx.EVT_BUTTON, self.delit)
		self.btn4.Bind(wx.EVT_BUTTON, self.prw)
		self.btn5.Bind(wx.EVT_BUTTON, self.upd)
		self.btn6.Bind(wx.EVT_BUTTON, self.aply)
		self.btn7.Bind(wx.EVT_BUTTON, self.gnrt)
		self.Sc1.Bind(wx.EVT_SPINCTRL, self.mtri)
		self.btnm.Bind(wx.EVT_BUTTON, self.inptri)
		self.btnx.Bind(wx.EVT_BUTTON, self.inpx)
		self.btny.Bind(wx.EVT_BUTTON, self.inpy)
		self.btntt.Bind(wx.EVT_BUTTON, self.pltdata)

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def filllist(self):
		ch1 = self.chis1.GetSelection()
		ch2 = self.chis2.GetSelection()
		if ch1 == 0:
			if ch2 == 0:
				Mroot = self.TLC1.GetRootItem()
				self.root1 = self.TLC1.AppendItem(Mroot, u'simple linear regression')
				self.LnrMtd = self.TLC1.AppendItem(self.root1, u'Some Method')
				self.TLC1.SetItemText(self.LnrMtd, 0, u'Simple Leaner ')
				self.TLC1.SetItemText(self.LnrMtd, 1, u'SL')
				self.NlnMtd = self.TLC1.AppendItem(self.root1, u'Some Method')
				self.TLC1.SetItemText(self.NlnMtd, 0, u'Simple NonLeaner ')
				self.TLC1.SetItemText(self.NlnMtd, 1, u'SN')

				self.root2 = self.TLC1.AppendItem(Mroot, u'multiple linear regression')
				self.GDMtd = self.TLC1.AppendItem(self.root2,u'Some Method')
				self.TLC1.SetItemText(self.GDMtd, 0, u'Gradient Descents')
				self.TLC1.SetItemText(self.GDMtd, 1, u'GD')
				self.NEMtd = self.TLC1.AppendItem(self.root2, u'Some Method')
				self.TLC1.SetItemText(self.NEMtd, 0, u'Normal Equation')
				self.TLC1.SetItemText(self.NEMtd, 1, u'NE')


	def typml( self, event ):
		event.Skip()

	def typpl( self, event ):
		event.Skip()

	def srcml( self, event ):
		event.Skip()

	def slcchng(self, event):
		ps = self.TLC1.GetSelections()
		self.itmcod = self.TLC1.GetItemText(ps[0], 1)
		lstpane = self.getMData.MLPansFils()
		#print(self.itmcod)
		#print(lstpane)
		for lp in lstpane:
			if self.itmcod in lp:
				myPnl = lp
		#print(self.idata,self.flds)
		#print(len(self.idata))
		i = importlib.import_module(u'DCC1.MLPane.'+myPnl[3])
		#print(len(self.P2.GetChildren()))
		#print(self.P2.HasFlag(self.P2.GetWindowStyleFlag()))
		if len(self.P2.GetChildren()) == 19:
			self.P19.Destroy()
			self.Vsp19 = wx.BoxSizer(wx.VERTICAL)

		self.P19 = i.P19(self.P2)

		self.P19.SetSizer(self.Vsp19)
		self.P19.Refresh()
		self.P19.Layout()
		self.Vsp19.Fit(self.P19)

		self.Vsz3.Add(self.P19, 1, wx.EXPAND | wx.ALL, 5)
		self.Splt1.Refresh()
		self.Splt1.Layout()
		self.Refresh()
		self.Layout()
		#self.Sc1.SetValue(len(self.idata))


	def addit( self, event ):
		dlg = wx.FileDialog(self, message="Choose Database",
		                    defaultDir=os.getcwd(),
		                    defaultFile="",
		                    wildcard="Sqlite db file(*.db,*.sqlite,*,slite3,*.db3)|*.db;*.db3;*.sqlite|All file(*.*)|*.*",
		                    style=wx.FD_OPEN | wx.FD_CHANGE_DIR)

		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
			#print(paths)
		dlg.Destroy()

		frm = wx.Dialog(self,-1)
		pnl = MyPanel2(frm,paths[0])
		frm.SetSize((600, 300))
		frm.SetLabel(u'Select Table')
		frm.ShowModal()
		self.flds = pnl.my_chois_fild
		self.idata = pnl.mydata

		frm.Destroy()
		#print(self.flds)
		#print(self.idata)
		self.Sc1.SetValue(len(self.idata))
		self.P19.Data = self.idata
		#if len(self.idata[0]) <= 2:
		#	self.TLC1.AppendItem(self.LnrMtd, u'this data select')
		#else:
		#	self.TLC1.AppendItem(self.NEMtd, u'Use this data ')
		#event.Skip()

	def editit( self, event ):
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

	def mtri( self, event ):

		event.Skip()

	def inptri( self, event ):
		frm = wx.Dialog(self, -1)
		pnl = MyPanel3(frm, self.flds, self.idata)
		frm.SetSize((500,220))
		frm.SetLabel(u'Data you use')
		frm.ShowModal()
		#frm.EndModal((pnl.xMtrx,pnl.yMtrx))
		Xm = pnl.xMtrx
		Ym = pnl.yMtrx
		frm.Destroy()
		self.Xdata= np.matrix(Xm)
		self.Ydata= np.matrix(Ym)
		self.P19.Xdata = self.Xdata
		self.P19.Ydata = self.Ydata
		#print(ixmatrix.tolist())
		#vw = ixmatrix.view()

		self.fldx.SetValue( 'np.matrix(xdata)' )
		self.fldy.SetValue( 'np.matrix(ydata)' )
		event.Skip()

	def inpx( self, event ):
		frm = wx.Dialog(self, -1)
		pnl = MyPanel4(frm,self.Xdata)
		frm.SetSize((300,180))
		frm.SetLabel(u'X matrix')
		frm.ShowModal()

		frm.Destroy()
		event.Skip()

	def inpy( self, event ):
		frm = wx.Dialog(self, -1)
		pnl = MyPanel4(frm, self.Ydata)
		frm.SetSize((300, 180))
		frm.SetLabel(u'Y matrix')
		frm.ShowModal()

		frm.Destroy()
		event.Skip()

	def pltdata( self, event ):
		#print(self.Xdata[:,1],self.Ydata[:,0])
		X = self.Xdata[:,1]
		y = self.Ydata.transpose()
		plot.plot(X, y , 'rx', markersize=10)
		plot.ylabel('data y')
		plot.xlabel('data x')
		plot.show()

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
		self.Tables.SetSelection( 2 )
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

		self.btn2 = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz2.Add(self.btn2, 0, wx.ALL, 5)

		self.btn1 = wx.Button(self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0)
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
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):

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
