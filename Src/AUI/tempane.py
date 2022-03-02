# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
# ! /usr/bin/env python

import wx


class MyPanel1(wx.Panel):
	def __init__(self, parent, id, pos, size, style):
		wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
		                  style=wx.TAB_TRAVERSAL)

		self.parent = parent


		VSiz = wx.BoxSizer(wx.VERTICAL)
		# You must write your source here




		self.SetSizer(VSiz)
		self.Layout()