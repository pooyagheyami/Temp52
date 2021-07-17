# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc
import re
try:
    from agw import hyperlink as hl
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.hyperlink as hl

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

    def __init__( self, parent , txt='' , btn='Ok' ):
        """

        :type txt: object
        """
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        url = re.search(r'(http?://\S+)', txt)

        if url != None:
            url = url.group()
            txt = txt.replace(url,'')

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, txt, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText1.Wrap( -1 )

        bSizer2.Add( self.m_staticText1, 5, wx.ALL|wx.EXPAND, 5 )

        if url != None:

            self._hyper1 = hl.HyperLinkCtrl(self, wx.ID_ANY, url, wx.DefaultPosition, wx.DefaultSize,wx.ALIGN_CENTER, URL=url)
            bSizer2.Add(self._hyper1, 5, wx.ALL|wx.EXPAND, 5)



        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_button1 = wx.Button( self, wx.ID_ANY, btn, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.onok )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onok( self, event ):
        q=self.GetParent()
        #print q
        q.Close()
        return -1


