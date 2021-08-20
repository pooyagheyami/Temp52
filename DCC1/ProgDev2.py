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

from AI.OpnFil import *
from AI.Analiz import *
from AI.Generats import *


from Config.Init import *

import Database.MenuSet2 as MS
import Database.PostGet as PG
import GUI.proman as pro
import importlib
import importlib.util
###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent,For_This_Frame=[], id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 544,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		self.FTF = For_This_Frame

		self.getMData = MS.GetData(u'Menu2.db', u'')
		self.setMDate = MS.SetData(u'', u'', u'')

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		#self.Splt1.SetSashGravity( -1 )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, u"List of Programs:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Vsz2.Add( self.lbl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.DVC1 = wx.dataview.TreeListCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		self.Col1 = self.DVC1.AppendColumn( u"Program name",  200, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendColumn( u"ID",  25, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		Vsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		self.filllist()

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn1.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_add.png', wx.BITMAP_TYPE_ANY ) )
		self.btn1.SetToolTip( u"Add" )

		Hsz1.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn2.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_edit.png', wx.BITMAP_TYPE_ANY ) )
		self.btn2.SetToolTip(u"Edit")
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn3.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_delete.png', wx.BITMAP_TYPE_ANY ) )
		self.btn3.SetToolTip(u"Delete")
		Hsz1.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn4.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_form.png', wx.BITMAP_TYPE_ANY ))
		self.btn4.SetToolTip(u"Preview")
		Hsz1.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn5.SetBitmap( wx.Bitmap( ICON16_PATH + u'update.png', wx.BITMAP_TYPE_ANY ) )
		self.btn5.SetToolTip(u"Update")
		Hsz1.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.btn6.SetBitmap( wx.Bitmap( ICON16_PATH + u'accept_button.png', wx.BITMAP_TYPE_ANY ) )
		self.btn6.SetToolTip(u"Apply")
		Hsz1.Add( self.btn6, 0, wx.ALL, 5 )


		self.btn7 = wx.BitmapButton(self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,wx.BU_AUTODRAW | 0)

		self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_lightning.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetToolTip(u"Generate")
		Hsz1.Add(self.btn7, 0, wx.ALL, 5)


		Vsz2.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.titr = wx.StaticText( self.P2, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr.Wrap( -1 )

		Vsz3.Add( self.titr, 0, wx.ALL|wx.EXPAND, 5 )

		self.Desc = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Vsz3.Add( self.Desc, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, u"ID No.", wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, u"Prog. No.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, u"import ", wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl4.Wrap( -1 )

		Hsz3.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.codgnr = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz3.Add( self.codgnr, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		Vsz3.Add( Hsz3, 0, wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl6 = wx.StaticText( self.P2, wx.ID_ANY, u"Directory", wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl6.Wrap( -1 )

		Hsz5.Add( self.lbl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.PrgDir1 = wx.DirPickerCtrl( self.P2, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		Hsz5.Add( self.PrgDir1, 1, wx.ALL, 5 )


		Vsz3.Add( Hsz5, 0, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self.P2, wx.ID_ANY, u"Parameters", wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl5.Wrap( -1 )

		Hsz4.Add( self.lbl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld4 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz4, 0, wx.EXPAND, 5 )

		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl7 = wx.StaticText( self.P2, wx.ID_ANY, u"Link:", wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl7.Wrap( -1 )

		Hsz6.Add( self.lbl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld6 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.fld6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.chk1 = wx.CheckBox( self.P2, wx.ID_ANY, u"Public it", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz6, 0, wx.EXPAND, 5 )

		self.lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz10 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl8 = wx.StaticText( self.P2, wx.ID_ANY, u"Database:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl8.Wrap( -1 )

		Hsz10.Add( self.lbl8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.probtn = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.probtn.SetToolTip( u"Select Database Tabels and Fields for this program" )

		Hsz10.Add( self.probtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz10, 0, wx.EXPAND, 5 )

		Vsz4 = wx.BoxSizer( wx.VERTICAL )

		self.prgfld = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.prgfld, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl9 = wx.StaticText( self.P2, wx.ID_ANY, u"Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl9.Wrap( -1 )

		Vsz4.Add( self.lbl9, 0, wx.ALL, 5 )


		Vsz3.Add( Vsz4, 1, wx.EXPAND, 5 )


		self.P2.SetSizer( Vsz3 )
		self.P2.Layout()
		Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 254 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )

		self.fromhere()


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctmnu, id = wx.ID_ANY )
		self.DVC1.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.slctitm, id=wx.ID_ANY)
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.conxmnu, id = wx.ID_ANY )
		self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_EDITING_DONE, self.endedit, id = wx.ID_ANY )
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.edtit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.prviw )
		self.btn5.Bind( wx.EVT_BUTTON, self.updat )
		self.btn6.Bind( wx.EVT_BUTTON, self.aplly )
		self.btn7.Bind( wx.EVT_BUTTON, self.gnrat )
		self.codgnr.Bind( wx.EVT_BUTTON, self.gencod )
		self.PrgDir1.Bind( wx.EVT_DIRPICKER_CHANGED, self.slctdir )
		self.chk1.Bind( wx.EVT_CHECKBOX, self.public )
		self.probtn.Bind( wx.EVT_BUTTON, self.dblst )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fromhere(self):
		if len(self.FTF) > 0:
			frmname = self.FTF[0].GetTitle()
			#print(frmname)
			self.lbl1.SetLabel("List of Programs:"+"    %s" %frmname)
	def filllist(self):
		#self.DVC1.AppendTextColumn()
		self.my_data = self.getMData.AllHndl("""left join Guidir on Guidir.prgdir = handler.prgdir 
		                                     left join PrgDesc on PrgDesc.handlerid = handler.handlerid 
		                                     where handler.handlerid < 99000 """)
		#print(self.my_data)
		allprgnm = [n[1] for n in self.my_data ]
		Aroot = self.DVC1.GetRootItem()
		self.root1 = self.DVC1.AppendItem(Aroot, "One page program All-in-One")
		self.root2 = self.DVC1.AppendItem(Aroot, "One page program for aui panes")
		self.root3 = self.DVC1.AppendItem(Aroot, "Program with one import panel ")
		self.root4 = self.DVC1.AppendItem(Aroot, "Multi program with some import ")
		self.root5 = self.DVC1.AppendItem(Aroot, "All python file in your HDD ")

		subimp = []
		for pro in self.my_data:
			#print(pro)
			thsfil = MAP + pro[8][2:] + SLASH + pro[1] + '.py'
			af = Anlzfil(thsfil)
			if pro[2] == '5555':
				child = self.DVC1.AppendItem(self.root2, pro[1])

			elif pro[2] < '5555' and pro[2] > '100':
				child = self.DVC1.AppendItem(self.root3, pro[1])

			elif pro[2] < '100':
				child = self.DVC1.AppendItem(self.root1, pro[1])

			elif pro[2] >= '6000':
				child = self.DVC1.AppendItem(self.root1, pro[1])

			else:
				print("some code is error")
			#print(af.ishasimport('GUI.API'), af.ishasfromim('GUI.API'))
			self.DVC1.SetItemText(child, 0, pro[1])
			self.DVC1.SetItemText(child, 1, str(pro[0]))
			if af.ishasimport('GUI.API'):
				atimp = af.ishasimport('GUI.API')[0].split(' ')[1].replace('GUI.API.','')
				subimp.append(atimp)
				child2 = self.DVC1.AppendItem(child, atimp)
				self.DVC1.SetItemText(child2, 0, atimp)
				self.DVC1.SetItemText(child2, 1, '7777')

		lstdir = self.getMData.AllGuiDir("  where rtrim(Guidir.prgdir,4) > '0000' and ltrim(Guidir.prgdir,4) < '8888' ")
		lstdir = [d[2] for d in lstdir ]
		#print(lstdir)
		notlsthndlr = []
		self.lsthddfil = []
		#print(allprgnm,subimp)
		for dr in lstdir:
			idr = dr.replace('..',MAP)
			#print(idr)
			for ifil in os.listdir(idr):
				if '.py' in ifil:
					if ifil.rstrip('.py') not in allprgnm and ifil != '__init__.py' and ifil != 'PAui.py' and ifil.rstrip('.py') not in subimp:
						notlsthndlr.append(ifil)
						self.lsthddfil.append(idr+'\\'+ifil)
		#print(notlsthndlr,self.lsthddfil)
		for nm in notlsthndlr:
			child2 = self.DVC1.AppendItem(self.root5,nm)
			self.DVC1.SetItemText(child2, 0, nm)
			self.DVC1.SetItemText(child2, 1, '????')

	def slctmnu( self, event ):
		#print(self.DVC1.GetSelection())
		#print(self.DVC1.GetRootItem())
		event.Skip()

	def slctitm( self, event ):
		self.nullfield()
		#print('selct', self.DVC1.GetSelection())
		itm = self.DVC1.GetSelection()
		#print('selct',self.DVC1.GetItemText(itm))
		txt = self.DVC1.GetItemText(itm,0)
		cod = self.DVC1.GetItemText(itm,1)
		#print(txt,cod)
		if cod != '':
			if cod == '????':
				for l in self.lsthddfil:
					if txt in l.split('\\'):
						self.PrgDir1.SetPath(l)
						self.thsfile = l
						self.thspath = l.replace(txt,'')
			elif cod[0] == '5' or cod[0] == '1' or cod[0] == '6':
				for item in self.my_data:
					if item[1] == txt and item[0] == int(cod) :
						#print(item)
					    self.fillfield(item,item[2])
			elif cod[0] == '7':
				self.thsfile = GUI_PATH+"API"+SLASH+txt+'.py'
				data = (cod,txt,'','-1','-1','-','GUI.API','','',None,None)
				self.fillfield(data,'')
				self.PrgDir1.SetPath(GUI_PATH+"API"+SLASH)
		else:
			if 'All-in-One' in txt:
				self.Desc.SetValue(u"Here a list of program that only in one file and when you do it all command execute")
			if 'aui' in txt:
				self.Desc.SetValue(u"Here a list of files that contains a panel class that you like to select for AuiPane Develop")
			if 'one import' in txt:
				self.Desc.SetValue(u"Here a List of files that contains a import module in GUI\API directory and it open that file ")
			if 'some import' in txt:
				self.Desc.SetValue(u"Here a List of files with some imports that contain several file and command part")
			if 'HDD' in txt:
				self.Desc.SetValue(u"Here a List of files in your GUI path and Utility that NOT listed in handlers data ")

	def nullfield(self):
		data = ('','','','','','','','','',None,None)
		cods = ''
		self.fillfield(data,cods)

	def fillfield(self, data, cods):
		if data[10] == '' or data[10] == None:
			self.Desc.SetValue('')
		else:
			self.Desc.SetValue(data[10])

		self.fld1.SetValue(str(data[0]))
		self.fld2.SetValue(str(data[5]))
		#AI.Analiz.GetImport
		self.fld3.SetValue('')
		#Get Path From handler directory data[6]+data[1]
		if data[8]!= '':
			self.thsfile = MAP+data[8][2:]+SLASH+data[1]+'.py'
			self.thspath = MAP+data[8][2:]
		    #print(self.thsfile,self.thspath)
			self.PrgDir1.SetPath(self.thspath)
		self.fld4.SetValue(str(data[3]))
		self.fld6.SetValue(str(data[4]))


	def conxmnu( self, event ):
		event.Skip()

	def endedit( self, event ):
		event.Skip()

	def addit( self, event ):

		self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
		self.Pnl = PyPanel(self.Frm, GUI_PATH + 'Temp\\untitle.py')
		self.Frm.SetSize((700, 560))
		self.Frm.Show()
		event.Skip()

	def edtit( self, event ):

		self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
		self.Pnl = PyPanel(self.Frm, self.thsfile)
		self.Frm.SetSize((700, 560))
		self.Frm.Show()
		event.Skip()

	def delit( self, event ):
		event.Skip()

	def prviw( self, event ):
		cdfld = self.fld2.GetValue()
		if len(cdfld) > 0:
			if cdfld[0] == '1':
				af = Anlzfil(self.thsfile)
				af.parsefil()
				#print(af.imprts)
				for im in af.imprts:
					if 'GUI' in im:
						#print(im)
					    a2 = im.split(' ')[1]
			elif cdfld[0] == '5':
				a2 = 'GUI.AuiPanel.'+self.DVC1.GetItemText(self.DVC1.GetSelection(),0)
			try:
				m = importlib.import_module(a2)
				self.Frm = wx.Frame(self, -1, pos=wx.DefaultPosition, size=wx.DefaultSize)
				self.pnl = m.MyPanel1(self.Frm, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL)
				self.Frm.Show()
			except ImportError as error:
				wx.MessageBox(error)
				print(error)

		elif cdfld == '':
			af = Anlzfil(self.thsfile)
			ifil = self.thsfile.replace(MAP + '\\', '')
			ifil = ifil.replace('\\', '.')
			ifil = ifil.replace('.py', '')
			m = importlib.import_module(ifil)
			if af.ishasframe():
				try:

					fr = af.ishasframe()
					myclass = getattr(m,fr)
					iframe = myclass(self)
					iframe.Show()
				except AttributeError as e:
					print('not work',e)
			elif af.ishaspanel():
				try:
					pl = af.ishaspanel()
					myclass = getattr(m, pl)
					b = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
					ipnl = myclass(b)
					b.Show()
				except AttributeError as e:
					print('nit work', e)

		event.Skip()

	def updat( self, event ):
		event.Skip()

	def aplly( self, event ):
		itm = self.DVC1.GetSelection()
		txt = self.DVC1.GetItemText(itm, 0)
		cod = self.DVC1.GetItemText(itm, 1)
		if cod == '????':
			wx.MessageBox(u'Please first Generate program then select the correct one to use it')
		mw = wx.FindWindowByName('main')
		#print(mw)
		print(self.FTF)
		#print(wx.GetTopLevelWindows())
		event.Skip()

	def gnrat( self, event ):
		print(self.thsfile,self.thspath)
		itm = self.DVC1.GetSelection()
		txt = self.DVC1.GetItemText(itm, 0)
		cod = self.DVC1.GetItemText(itm, 1)
		af = Anlzfil(self.thsfile)
		if cod == '????':
			if af.ishasframe():
				print(af.ishasframe())
				print(self.getData())

		event.Skip()


	def gencod( self, event ):
	    event.Skip()

	def slctdir( self, event ):
		event.Skip()

	def public( self, event ):
		event.Skip()

	def dblst( self, event ):
		event.Skip()

	def getData(self):
		D1 = self.fld1.GetValue()
		D2 = self.fld2.GetValue()
		D3 = self.fld3.GetValue()
		D4 = self.PrgDir1.GetPath()
		D5 = self.fld4.GetValue()
		D6 = self.fld6.GetValue()
		D7 = self.chk1.GetValue()
		return D1,D2,D3,D4,D5,D6,D7

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 254 )
		self.Splt1.Unbind( wx.EVT_IDLE )


