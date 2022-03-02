# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
# ! /usr/bin/env python

import wx


class MyPanel1 ( wx.Panel ):
	def __init__(self, parent, id, pos, size, style):
		wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
		                  style=wx.TAB_TRAVERSAL)

		self.parent = parent


		VSiz = wx.BoxSizer(wx.VERTICAL)
		# You must write your source here

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.m_panel1, u"Access", False )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.m_panel2, u"Directory", False )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.m_panel3, u"My Form", False )

		VSiz.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )




		self.SetSizer(VSiz)
		self.Layout()