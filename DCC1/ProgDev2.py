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

import AI.OpnSrc as OS
from AI.Analiz import *
from AI.Generats import *


from Config.Init import *
import Res.Allicons as icon

import Database.MenuSet2 as MS
import Database.PostGet as PG
import GUI.proman as pro
import importlib
import importlib.util

_ = wx.GetTranslation
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
		# Parameter Init
		self.iSrc_api_Imp = self.getMData.GetImpCod('7777')[0][0]


		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		#self.Splt1.SetSashGravity( -1 )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.lbl1 = wx.StaticText( self.P1, wx.ID_ANY, _(u"List of Programs:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Vsz2.Add( self.lbl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.DVC1 = wx.dataview.TreeListCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		self.Col1 = self.DVC1.AppendColumn( _(u"Program name"),  200, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVC1.AppendColumn( _(u"ID"),  25, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		Vsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )

		self.filllist()

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn1.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_add.png', wx.BITMAP_TYPE_ANY ) )
		self.btn1.SetBitmap(icon.application_add.GetBitmap())
		self.btn1.SetToolTip( _(u"Add") )

		Hsz1.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn2.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_edit.png', wx.BITMAP_TYPE_ANY ) )
		self.btn2.SetBitmap(icon.application_edit.GetBitmap())
		self.btn2.SetToolTip(_(u"Edit"))
		Hsz1.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn3.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_delete.png', wx.BITMAP_TYPE_ANY ) )
		self.btn3.SetBitmap(icon.application_delete.GetBitmap())
		self.btn3.SetToolTip(_(u"Delete"))
		Hsz1.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn4.SetBitmap( wx.Bitmap( ICON16_PATH + u'application_form.png', wx.BITMAP_TYPE_ANY ))
		self.btn4.SetBitmap(icon.application_form.GetBitmap())
		self.btn4.SetToolTip(_(u"Preview"))
		Hsz1.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn5.SetBitmap( wx.Bitmap( ICON16_PATH + u'update.png', wx.BITMAP_TYPE_ANY ) )
		self.btn5.SetBitmap(icon.update.GetBitmap())
		self.btn5.SetToolTip(_(u"Update"))
		Hsz1.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn6.SetBitmap( wx.Bitmap( ICON16_PATH + u'accept_button.png', wx.BITMAP_TYPE_ANY ) )
		self.btn6.SetBitmap(icon.accept_button.GetBitmap())
		self.btn6.SetToolTip(_(u"Apply"))
		Hsz1.Add( self.btn6, 0, wx.ALL, 5 )


		self.btn7 = wx.BitmapButton(self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,wx.BU_AUTODRAW | 0)

		#self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'application_lightning.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetBitmap(icon.application_lightning.GetBitmap())
		self.btn7.SetToolTip(_(u"Generate"))
		Hsz1.Add(self.btn7, 0, wx.ALL, 5)


		Vsz2.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.titr = wx.StaticText( self.P2, wx.ID_ANY, _(u"Description:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr.Wrap( -1 )

		Vsz3.Add( self.titr, 0, wx.ALL|wx.EXPAND, 5 )

		self.Desc = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		Vsz3.Add( self.Desc, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, _(u"ID No."), wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Prog. No."), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz2.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, _(u"import "), wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl4.Wrap( -1 )

		Hsz3.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.codgnr = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz3.Add( self.codgnr, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		Vsz3.Add( Hsz3, 0, wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl6 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Directory"), wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl6.Wrap( -1 )

		Hsz5.Add( self.lbl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.PrgDir1 = wx.DirPickerCtrl( self.P2, wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		Hsz5.Add( self.PrgDir1, 1, wx.ALL, 5 )


		Vsz3.Add( Hsz5, 0, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Parameters"), wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl5.Wrap( -1 )

		Hsz4.Add( self.lbl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld4 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz4, 0, wx.EXPAND, 5 )

		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl7 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Link:"), wx.DefaultPosition, wx.Size( 58,-1 ), 0 )
		self.lbl7.Wrap( -1 )

		Hsz6.Add( self.lbl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld6 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.fld6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.chk1 = wx.CheckBox( self.P2, wx.ID_ANY, _(u"Public it"), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz6, 0, wx.EXPAND, 5 )

		self.lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz10 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl8 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Database:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl8.Wrap( -1 )

		Hsz10.Add( self.lbl8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.probtn = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.probtn.SetToolTip( _(u"Select Database Tabels and Fields for this program") )

		Hsz10.Add( self.probtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz10, 0, wx.EXPAND, 5 )

		Vsz4 = wx.BoxSizer( wx.VERTICAL )

		self.prgfld = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.prgfld, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl9 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Directory:"), wx.DefaultPosition, wx.DefaultSize, 0 )
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
			# if af.ishasimport('GUI.API'):
			# 	atimp = af.ishasimport('GUI.API')[0].split(' ')[1].replace('GUI.API.','')
			# 	subimp.append(atimp)
			# 	child2 = self.DVC1.AppendItem(child, atimp)
			# 	self.DVC1.SetItemText(child2, 0, atimp)
			# 	self.DVC1.SetItemText(child2, 1, '7777')
			if af.ishasimport(self.iSrc_api_Imp):
				atimp = af.ishasimport(self.iSrc_api_Imp)[0].split(' ')[1].replace(self.iSrc_api_Imp+'.','')
				subimp.append(atimp)
				child2 = self.DVC1.AppendItem(child, atimp)
				self.DVC1.SetItemText(child2, 0, atimp)
				self.DVC1.SetItemText(child2, 1, '7777')
			if af.ishasfromim(' . '):
				atimp = af.ishasfromim(' . ')[0].split(' ')[3]
				subimp.append(atimp)
				chil3 = self.DVC1.AppendItem(child, atimp)
				self.DVC1.SetItemText(chil3, 0, atimp)
				self.DVC1.SetItemText(chil3, 1, '7777')

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
						self.thsdcod = self.getMData.AllGuiDir(" where Guidir.hdddir = '%s' "%self.thspath.replace(MAP,'..').rstrip(SLASH) )[0][1]

			elif cod[0] == '5' or cod[0] == '1' or cod[0] == '6':
				for item in self.my_data:
					if item[1] == txt and item[0] == int(cod) :
						#print(item)
					    self.fillfield(item,item[2])
			# elif cod[0] == '7':
			# 	self.thsfile = GUI_PATH+"API"+SLASH+txt+'.py'
			# 	data = (cod,txt,'','-1','-1','-','GUI.API','','',None,None)
			# 	self.fillfield(data,'')
			# 	self.PrgDir1.SetPath(GUI_PATH+"API"+SLASH)
			elif cod[0] == '7':
				self.thsfile = SRC_PATH+"api"+SLASH+txt+'.py'
				data = (cod,txt,'','-1','-1','-','Src.api','','',None,None)
				self.fillfield(data,'')
				self.PrgDir1.SetPath(SRC_PATH+"api"+SLASH)
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
		#self.Pnl = PyPanel(self.Frm, GUI_PATH + 'Temp\\untitle.py')
		self.Pnl = OS.SrcPanel(self.Frm,GUI_PATH + 'Temp\\untitle.py' )
		self.Frm.SetMenuBar(OS.MyMenuBar1(u'Pro'))
		self.Frm.SetSize((700, 560))
		self.Frm.SetLabel('untitle.py')
		self.Frm.Show()
		event.Skip()

	def edtit( self, event ):

		self.Frm = wx.Frame(self, style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL)
		#self.Pnl = PyPanel(self.Frm, self.thsfile)
		self.Pnl = OS.SrcPanel(self.Frm, self.thsfile)
		self.Frm.SetMenuBar(OS.MyMenuBar1(u'Pro'))
		self.Frm.SetSize((700, 560))
		self.Frm.SetLabel(self.thsfile)
		self.Frm.Show()
		event.Skip()

	def delit( self, event ):
		if self.fld1.GetValue() == '':
			wx.MessageBox(_("Do you like delete program file from path"))
			hndlid = 0
		else:
			hndlid = self.fld1.GetValue()

		# print(hndlid)
		if len(self.getMData.AllHndl(u' where handler.handlerid = %d' % int(hndlid))) > 0:
			self.setMDate.Table = u'handler'
			self.setMDate.Delitem(u' handler.handlerid = %d' % int(hndlid))
		if len(self.getMData.AllHndl(u' Join PrgDesc on handler.handlerid = PrgDesc.handlerid \
		                                             where handler.handlerid = %d' % int(hndlid))) > 0:
			self.setMDate.Table = u'PrgDesc'
			self.setMDate.Delitem(u' PrgDesc.handlerid = %d' % int(hndlid))
		wx.MessageBox(_(u"Program successful delete from your list"))
		self.updat(None)
		#event.Skip()

	def prviw( self, event ):
		cdfld = self.fld2.GetValue()
		if len(cdfld) > 0:
			if cdfld[0] == '6':
				a2 = pro.DoProgram2(0,int(self.fld1.GetValue()))
				#print(a2)
				win1 = wx.Frame(self, -1)
				a2.main(win1)
			if cdfld[0] == '1':
				a2 = pro.DoProgram2(0,int(self.fld1.GetValue()))
				#print(a2)
				win1 = wx.Frame(self, -1)
				a2.main(win1)

			if cdfld[0] == '5':
				a2 = pro.DoProgram2(0, int(self.fld1.GetValue()))
				#print(a2)
				self.Frm = wx.Frame(self, -1, style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
				self.pnl = a2.MyPanel1(self.Frm, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
				                      style=wx.TAB_TRAVERSAL)
				self.Frm.Show()

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
					print('not work', e)

		event.Skip()

	def updat( self, event ):
		self.DVC1.DeleteAllItems()
		self.filllist()
		self.Refresh()
		#event.Skip()

	def aplly( self, event ):
		itm = self.DVC1.GetSelection()
		txt = self.DVC1.GetItemText(itm, 0)
		cod = self.DVC1.GetItemText(itm, 1)
		if cod == '????':
			wx.MessageBox(_(u'Please first Generate program then select the correct one to use it'))
		#print(self.FTF)
		else:
			pnl = self.FTF[0].panel
			pnl.prgfld.SetValue(txt)
			pnl.lbl9.SetLabel(_(u"Directory: ")+self.thspath)
			#print(pnl)
			q = self.GetParent()
			q.Close()
		#print(wx.GetTopLevelWindows())
		#event.Skip()

	def gnrat( self, event ):
		#print(self.thsfile,self.thspath)
		itm = self.DVC1.GetSelection()
		txt = self.DVC1.GetItemText(itm, 0)
		cod = self.DVC1.GetItemText(itm, 1)
		af = Anlzfil(self.thsfile)

		#print(txt,cod,self.thsdcod,self.thsfile,self.thspath)

		if cod == '????':
			if af.ishasmain():
				#print(u'This file main')
				af.checkSyntx()
				if af.ishasifin():
					#print(u'If is in file')
					af.checkSyntx()
			if af.ishasframe():
				mygnrt = Genrate2(self.thsfile)
				mygnrt.gnratLine(False,True,True,True,af.ishasframe())
				mygnrt.appendFile()
				lstcod = self.getMData.getHndid(self.thsdcod)
				newcod = int(self.thsdcod[0])*10000+len(lstcod)+1
				newnom = int(self.thsdcod[0])*100+len(lstcod)+1
				data = [newcod,txt.replace('.py', ''),self.thsdcod,'-1',-1,newnom]
				self.setMDate.Table = 'handler'
				self.setMDate.Additem(" handlerid, prgname, prgdir, paramtr, public, prgno", data)
				self.DVC1.DeleteAllItems()
				self.filllist()
				self.Refresh()
			elif af.ishaspanel():
				if af.ishaspanel() == 'MyPanel1':
					dlg = MyDialog1(self)
					dlg.ShowModal()
					if dlg.filname:
						newname = dlg.filname
						dircode = self.getMData.GetDirCod2(dlg.pathfil)[0][0]
						lstcod = self.getMData.getHndid(dircode)
						patfil = dlg.pathfil
						newcod = int(dircode[0]) * 10000 + len(lstcod) + 1 * 10 + int(dircode[-1])
						newnom = int(dircode[0]) * 100 + len(lstcod) + 1 * 10 + int(dircode[-1])

					elif dlg.box1:
						newname = txt
						dircode = '5555'
						lstcod = self.getMData.getHndid(dircode)
						newcod = int(dircode[0]) * 10000 + len(lstcod) + 1
						newnom = int(dircode[0]) * 10 + len(lstcod) + 1

					else:
						newname = txt[0].upper()+txt[len(txt)/2].upper()
						dircode = '8888'
						lstcod = self.getMData.getHndid(dircode)
						newcod = int(dircode[0]) * 10000 + len(lstcod) + 1
						newnom = int(dircode[0]) * 100 + len(lstcod) + 1
					dlg.Destroy()
					#print(newname,dircode,patfil)
					mygnrt = Genrate(patfil.replace('..', MAP)+SLASH+newname+'.py')
					mygnrt.createFrm(self.thsfile)

					data = [newcod, newname, dircode, '-1', -1, newnom]
					self.setMDate.Table = 'handler'
					self.setMDate.Additem(" handlerid, prgname, prgdir, paramtr, public, prgno", data)
					self.DVC1.DeleteAllItems()
					self.filllist()
					self.Refresh()

		else:
			wx.MessageBox(_(u"You can only generate the unlisted program with this code '????'"))

		#event.Skip()

	def gencod( self, event ):
	    event.Skip()

	def slctdir( self, event ):
		event.Skip()

	def public( self, event ):
		event.Skip()

	def dblst( self, event ):
		if wx.FindWindowByName(u'Database Develop') == None:
			import DCC1.DBDev2 as DB
			ifrm = wx.Frame(self, -1, style=wx.FRAME_FLOAT_ON_PARENT | wx.DEFAULT_FRAME_STYLE)
			pnl = DB.MyPanel1(ifrm, [self.GetParent()])
			ifrm.SetSize((555, 460))
			ifrm.SetTitle(u'Database use Program')
			ifrm.Show()
		else:
			wx.MessageBox(_("Double Program: Please Close Program Develop then Do this item"))

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


class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 365,165 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.filname = ''
		self.pathfil = ''
		self.myMenu = MS.GetData(u'Menu2.db',u'')

		V1 = wx.BoxSizer( wx.VERTICAL )

		H1 = wx.BoxSizer( wx.HORIZONTAL )

		self.box1 = wx.CheckBox(self, wx.ID_ANY, _(u"Create for Aui Pane"), wx.DefaultPosition, wx.DefaultSize, 0)
		H1.Add(self.box1, 0, wx.ALL, 5)

		V1.Add( H1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		H2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl1 = wx.StaticText( self, wx.ID_ANY, _(u"name of file to create"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		H2.Add( self.lbl1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		H2.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		V1.Add( H2, 1, wx.EXPAND, 5 )

		H3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self, wx.ID_ANY, _(u"choise path of file to create"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )

		H3.Add( self.lbl2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		chs1Choices = [ d[2] for d in self.myMenu.AllGuiDir(u" where Guidir.prgdir < '5000' ") ]
		self.chs1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs1Choices, 0 )
		self.chs1.SetSelection( 0 )
		H3.Add( self.chs1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		V1.Add( H3, 1, wx.EXPAND, 5 )

		H4 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		H4.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, _(u"Ok"), wx.DefaultPosition, wx.DefaultSize, 0 )
		H4.Add( self.btn2, 0, wx.ALL, 5 )


		V1.Add( H4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( V1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.box1.Bind( wx.EVT_CHECKBOX, self.foraui )
		self.btn1.Bind( wx.EVT_BUTTON, self.cncl )
		self.btn2.Bind( wx.EVT_BUTTON, self.gtit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def foraui( self, event ):
		if self.box1.GetValue():
			self.fld1.Disable()
			self.chs1.Disable()
		else:
			self.fld1.Enable()
			self.chs1.Enable()
		event.Skip()

	def cncl( self, event ):
		self.Destroy()
		event.Skip()

	def gtit( self, event ):
		self.filname = self.fld1.GetValue()
		self.pathfil = self.chs1.GetStringSelection()
		#print(self.filname,self.pathfil)
		#print(self.myMenu.GetDirCod2(self.pathfil))
		self.Destroy()
		event.Skip()


