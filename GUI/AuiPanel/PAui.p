Netbook.py, Right, PinButton, Dock, Resizable, Size, 1500 1200, Layer, 0, Show,
Rev.py, Left, PinButton, Dock, Resizable, Size, 200 400, Layer, 1, Show,
Stat.py, Center, PinButton, Dock, Resizable, Size, 1600 1300, Layer, 0, Hide,

self.m_panel1, .Center() .Caption( u"Float1" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Gripper().Dock().Resizable().FloatingSize( wx.Size( 569,76 ) ).DockFixed( True ).Row( 1 ).Position( 1 ).BestSize( wx.Size( 400,400 ) ).MinSize( wx.Size( 100,100 ) ).MaxSize( wx.Size( 450,-1 ) ).Layer( 1 ).CentrePane().DefaultPane()
self.m_panel1, .Center() .Caption( u"Float1" ).CloseButton( False ).MinimizeButton( True ).PaneBorder( False ).Gripper().Dock().Resizable().FloatingSize( wx.Size( 569,76 ) ).DockFixed( True ).BottomDockable( False ).TopDockable( False ).LeftDockable( False ).RightDockable( False ).Row( 2 ).Position( 1 ).BestSize( wx.Size( 400,400 ) ).MinSize( wx.Size( 100,100 ) ).MaxSize( wx.Size( 450,-1 ) ).Layer( 3 ).CentrePane().DefaultPane()


self.m_panel1, wx.aui.AuiPaneInfo() .Name( u"auiname" ).Left() .Caption( u"captionstr" ).CaptionVisible( False ).CloseButton( False ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).PaneBorder( False ).Gripper().Hide().Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).DockFixed( True ).BottomDockable( False ).TopDockable( False ).LeftDockable( False ).RightDockable( False ).Floatable( False ).CentrePane().DefaultPane() )
self.m_panel2, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
