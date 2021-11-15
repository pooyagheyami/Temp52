#In the name of God
#Utility for Machin Learning Panel Parameter and Algorithms
# -*- coding: utf-8 -*-

import wx
import wx.dataview
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
