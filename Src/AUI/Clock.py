# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
# ! /usr/bin/env python

import wx
import wx.lib.gizmos as gizmos  # Formerly wx.gizmos in Classic
import time

class MyPanel1(wx.Panel):
	def __init__(self, parent, id, pos, size, style):
		wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
		                  style=wx.TAB_TRAVERSAL)

		self.parent = parent


		#VSiz = wx.BoxSizer(wx.VERTICAL)
		# You must write your source here
		led = gizmos.LEDNumberCtrl(self, -1, (0, 0), (250, 50),
		                           gizmos.LED_ALIGN_CENTER)  # | gizmos.LED_DRAW_FADED)
		led.SetForegroundColour('black')
		led.SetBackgroundColour('white')

		#VSiz.Add(led, 1,wx.ALL,5)
		self.clock = led
		self.OnTimer(None)

		self.timer = wx.Timer(self)
		self.timer.Start(1000)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

		#self.SetSizer(VSiz)
		self.Layout()

	def OnTimer(self, evt):
		t = time.localtime(time.time())
		st = time.strftime("%H:%M:%S", t)
		self.clock.SetValue(st)