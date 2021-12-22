# In the name of God
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# Start some program and splash


import wx
import wx.adv
from Config.Init import *

class MySplashScreen(wx.adv.SplashScreen):
    def __init__(self, window):
        self.window = window
        self.config = wx.GetApp().GetConfig()

        mysplash = self.config.Read("Splash")
        bmp = wx.Bitmap(mysplash, wx.BITMAP_TYPE_ANY)

        wx.adv.SplashScreen.__init__(self, bmp,
                                 wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
                                 7000, None, style=wx.BORDER_NONE|
                                     #wx.BORDER_SIMPLE|
                                     #wx.FRAME_NO_TASKBAR|
                                     wx.STAY_ON_TOP)

        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.count = 0
        #wx.Sleep(1)
        self.CrtCtrl()
        self.tmr = wx.Timer(self, 1)
        self.tmr.Start(75)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.Bind(wx.EVT_TIMER, self.TimerHandler, self.tmr)

        wx.BeginBusyCursor()

        self.fc = wx.CallLater(2000, self.ShowMain)


    def CrtCtrl(self):
        rect = self.GetClientRect()
        new_size = (rect.width, 9)
        self.text = wx.StaticText(self,-1,"Loading...",pos=(0, rect.height-9),size=(new_size),style=wx.ALIGN_CENTRE_HORIZONTAL)
        self.text.SetBackgroundColour(wx.WHITE)
        self.text.SetForegroundColour(wx.BLACK)
        #rect = self.GetClientRect()
        self.gauge = wx.Gauge(self,-1,range=50,size=(-1, 9),pos=(0, rect.height))
        #rect = self.GetClientRect()

        self.gauge.SetSize(new_size)
        self.SetSize((rect.width, rect.height + 9))
        #self.gauge.SetPosition((0, rect.height))

    def TimerHandler(self, event):

        self.count = self.count + 1
        if self.count >= 90:
            self.count = 0
        self.gauge.SetValue(self.count)


    def OnClose(self, evt):
        # Make sure the default handler runs too so this window gets destroyed
        #evt.Skip()
        self.Hide()
        self.tmr.Stop()
        # if the timer is still running then go ahead and show the main frame now
        if self.fc.IsRunning():
            self.fc.Stop()
            self.ShowMain()
        evt.Skip()

    def ShowMain(self):
        wx.CallAfter(wx.EndBusyCursor)

        SIZE = wx.DisplaySize()
        frame = self.window.MainWin()
        #frame = window2.MainWin()
        frame.SetSize(SIZE)
        frame.SetPosition((1, 1))
        #frame.CenterOnScreen()
        frame.EnableFullScreenView(True)
        #frame.ShowFullScreen()
        frame.Show()

        if self.fc.IsRunning():
            self.Raise()
        # wx.CallAfter(frame.ShowTip)