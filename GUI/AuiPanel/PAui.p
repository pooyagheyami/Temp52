Rev.py, Left, PinButton, Dock, Resizable, Size, 200 400, Layer, 1, Show
Stat.py, Bottom, PinButton, Dock, Resizable, Size, 400 300, Layer, 2, Show

self.m_panel1, .Center() .Caption( u"Float1" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Gripper().Dock().Resizable().FloatingSize( wx.Size( 569,76 ) ).DockFixed( True ).Row( 1 ).Position( 1 ).BestSize( wx.Size( 400,400 ) ).MinSize( wx.Size( 100,100 ) ).MaxSize( wx.Size( 450,-1 ) ).Layer( 1 ).CentrePane().DefaultPane()
self.m_panel1, .Center() .Caption( u"Float1" ).CloseButton( False ).MinimizeButton( True ).PaneBorder( False ).Gripper().Dock().Resizable().FloatingSize( wx.Size( 569,76 ) ).DockFixed( True ).BottomDockable( False ).TopDockable( False ).LeftDockable( False ).RightDockable( False ).Row( 2 ).Position( 1 ).BestSize( wx.Size( 400,400 ) ).MinSize( wx.Size( 100,100 ) ).MaxSize( wx.Size( 450,-1 ) ).Layer( 3 ).CentrePane().DefaultPane()

