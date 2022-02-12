# In the name of God
# -*- coding: utf-8 -*-
# !usr/bin/env python

import wx
import GUI.API.SamPnl as SPnl
from Config.Init import *


class Demoframe(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, style=wx.FRAME_FLOAT_ON_PARENT | wx.DEFAULT_FRAME_STYLE)
		self.parent = parent
		#you can add code here before create panel

		self.panel = SPnl.MyPanel1(self)

	def closeit(self):
		self.Close(True)


def size():
	return (-1, -1)


def main(panel=None):
	parent = panel.GetParent()
	frame = Demoframe(parent)
	frame.SetTitle(u'Demo')
	frame.SetSize((500, 300))
	frame.Show()


if __name__ == '__main__':
	main()
