#In the name of GOD

import wx
import wx.xrc
import wx.lib.gizmos as gizmos  # Formerly wx.gizmos in Classic
import time

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 319,153 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )



        led = gizmos.LEDNumberCtrl(self, -1, (0, 0), (250, 50),
                                   gizmos.LED_ALIGN_CENTER)  # | gizmos.LED_DRAW_FADED)
        led.SetForegroundColour('black')
        led.SetBackgroundColour('white')
        self.clock = led
        self.OnTimer(None)

        self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)


    def __del__( self ):
        pass

    def OnTimer(self, evt):
        t = time.localtime(time.time())
        st = time.strftime("%H:%M:%S", t)
        self.clock.SetValue(st)


class MyFrame1 ( wx.Frame ):
    def __init__(self, parent):
        wx.Frame.__init__(self,parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 100,50 ), style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.bS1 = wx.BoxSizer(wx.HORIZONTAL)
        clock = MyPanel2(self)
        self.bS1.Add(clock, 0, wx.EXPAND | wx.ALL, 1)

        self.SetSizer(self.bS1)
        self.Layout()