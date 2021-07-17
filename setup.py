
# ======================================================== #
# File automagically generated by GUI2Exe version 0.5.3
# Copyright: (c) 2007-2012 Andrea Gavana
# ======================================================== #

# Let's start with some default (for me) imports...

from distutils.core import setup
from py2exe.build_exe import py2exe

import glob
import os
import zlib
import shutil

# Remove the build folder
shutil.rmtree("build", ignore_errors=True)


class Target(object):
    """ A simple class that holds information on our executable file. """
    def __init__(self, **kw):
        """ Default class constructor. Update as you need. """
        self.__dict__.update(kw)
        

# Ok, let's explain why I am doing that.
# Often, data_files, excludes and dll_excludes (but also resources)
# can be very long list of things, and this will clutter too much
# the setup call at the end of this file. So, I put all the big lists
# here and I wrap them using the textwrap module.

data_files = [('GUI\AuiPanel', ['E:\\Mywork\\tamil\\Temp4\\GUI\\AuiPanel\\__init__.pyc',
                                'E:\\Mywork\\tamil\\Temp4\\GUI\\AuiPanel\\Rev.pyc',
                                'E:\\Mywork\\tamil\\Temp4\\GUI\\AuiPanel\\Stat.pyc']),
              ('GUI\Edit', ['E:\\Mywork\\tamil\\Temp4\\GUI\\Edit\\__init__.pyc',
                            'E:\\Mywork\\tamil\\Temp4\\GUI\\Edit\\buyit.pyc']),
              ('Logs', ['E:\\Mywork\\tamil\\Temp4\\Logs\\__init__.py',
                        'E:\\Mywork\\tamil\\Temp4\\Logs\\about.txt',
                        'E:\\Mywork\\tamil\\Temp4\\Logs\\disit.txt',
                        'E:\\Mywork\\tamil\\Temp4\\Logs\\file2.txt']),
              ('Database', ['E:\\Mywork\\tamil\\Temp4\\Database\\__init__.pyc',
                            'E:\\Mywork\\tamil\\Temp4\\Database\\Menu2.db',
                            'E:\\Mywork\\tamil\\Temp4\\Database\\wxsq.pyc']),
              ('GUI', ['E:\\Mywork\\tamil\\Temp4\\GUI\\__init__.pyc',
                       'E:\\Mywork\\tamil\\Temp4\\GUI\\BG.pyc',
                       'E:\\Mywork\\tamil\\Temp4\\GUI\\MainMenu.pyc',
                       'E:\\Mywork\\tamil\\Temp4\\GUI\\proman.pyc',
                       'E:\\Mywork\\tamil\\Temp4\\GUI\\window.pyc']),
              ('GUI\Input', ['E:\\Mywork\\tamil\\Temp4\\GUI\\Input\\__init__.pyc',
                             'E:\\Mywork\\tamil\\Temp4\\GUI\\Input\\buyit.pyc',
                             'E:\\Mywork\\tamil\\Temp4\\GUI\\Input\\faktor.pyc',
                             'E:\\Mywork\\tamil\\Temp4\\GUI\\Input\\fkt.pyc']),
              ('GUI\Program', ['E:\\Mywork\\tamil\\Temp4\\GUI\\Program\\__init__.pyc',
                               'E:\\Mywork\\tamil\\Temp4\\GUI\\Program\\buyit.pyc',
                               'E:\\Mywork\\tamil\\Temp4\\GUI\\Program\\quit.pyc']),
              ('GUI\Report', ['E:\\Mywork\\tamil\\Temp4\\GUI\\Report\\__init__.pyc',
                              'E:\\Mywork\\tamil\\Temp4\\GUI\\Report\\buyit.pyc']),
              ('GUI\Develop', ['E:\\Mywork\\tamil\\Temp4\\GUI\\Develop\\__init__.pyc',
                               'E:\\Mywork\\tamil\\Temp4\\GUI\\Develop\\buyit.pyc']),
              ('GUI\Help', ['E:\\Mywork\\tamil\\Temp4\\GUI\\Help\\__init__.pyc',
                            'E:\\Mywork\\tamil\\Temp4\\GUI\\Help\\about.pyc']),
              ('GUI\Connect', ['E:\\Mywork\\tamil\\Temp4\\GUI\\Connect\\__init__.pyc',
                               'E:\\Mywork\\tamil\\Temp4\\GUI\\Connect\\buyit.pyc']),
              ('Config', ['E:\\Mywork\\tamil\\Temp4\\Config\\__init__.pyc',
                          'E:\\Mywork\\tamil\\Temp4\\Config\\Init.pyc',
                          'E:\\Mywork\\tamil\\Temp4\\Config\\program.ini']),
              ('GUI\API', ['E:\\Mywork\\tamil\\Temp4\\GUI\\API\\__init__.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\GUI\\API\\Input.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\GUI\\API\\Input2.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\GUI\\API\\Pnl0.pyc']),
              ('Utility', ['E:\\Mywork\\tamil\\Temp4\\Utility\\__init__.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\Adaad2.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\adadfa1',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\adadtr1',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\calcu.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\calfar.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\clacal2.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\clacal3.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\getmap.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\Map1',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\Map2',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\Tclacal3.pyc',
                           'E:\\Mywork\\tamil\\Temp4\\Utility\\Tmkey1.pyc'])]

includes = ['wx', 'wx.lib', 'wx.dataview']
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = ['Config', 'Utility', 'Database', 'GUI', 'GUI.API', 'GUI.AuiPanel',
            'GUI.Connect', 'GUI.Develop', 'GUI.Edit', 'GUI.Help',
            'GUI.Input', 'GUI.Program', 'GUI.Report']
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']
icon_resources = []
bitmap_resources = [(1, 'E:\\Mywork\\tamil\\Temp4\\Res\\Icons\\calculator.bmp')]
other_resources = [(1, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Icons\\barcode.png'),
                   (2, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Icons\\calculator.bmp'),
                   (3, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Icons\\Keyboard.png'),
                   (4, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\__init__.py'),
                   (5, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\Mypic1.jpg'),
                   (6, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\Mypic2.jpg'),
                   (7, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\Mypic3.jpg'),
                   (8, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\Mypic4.jpg'),
                   (9, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\Mypic5.jpg'),
                   (10, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\Mypic6.jpg'),
                   (11, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\V6.jpg'),
                   (12, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\V10.jpg'),
                   (13, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\V16.jpg'),
                   (14, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\V17.jpg'),
                   (15, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\V18.jpg'),
                   (16, 24, 'E:\\Mywork\\tamil\\Temp4\\Res\\Pics\\V19.jpg')]


# This is a place where the user custom code may go. You can do almost
# whatever you want, even modify the data_files, includes and friends
# here as long as they have the same variable name that the setup call
# below is expecting.

# No custom code added


# Ok, now we are going to build our target class.
# I chose this building strategy as it works perfectly for me :-D

GUI2Exe_Target_1 = Target(
    # what to build
    script = "mainpro.py",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources,
    dest_base = "mainpro",    
    version = "0.1",
    company_name = "No Company",
    copyright = "No Copyrights",
    name = "Py2Exe Sample File",
    
    )

# No custom class for UPX compression or Inno Setup script

# That's serious now: we have all (or almost all) the options py2exe
# supports. I put them all even if some of them are usually defaulted
# and not used. Some of them I didn't even know about.
                    
setup(

    # No UPX or Inno Setup

    data_files = data_files,

    options = {"py2exe": {"compressed": 0, 
                          "optimize": 0,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 3,
                          "dist_dir": "dist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },

    zipfile = None,
    console = [],
    windows = [GUI2Exe_Target_1],
    service = [],
    com_server = [],
    ctypes_com_server = []
    )

# This is a place where any post-compile code may go.
# You can add as much code as you want, which can be used, for example,
# to clean up your folders or to do some particular post-compilation
# actions.

# No post-compilation code added


# And we are done. That's a setup script :-D

