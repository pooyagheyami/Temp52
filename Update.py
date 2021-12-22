#In the name of God
#Script for Update Project
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, shutil

main_direct = [u'AI',u'Config',u'Database',u'DCC1',u'GUI','GUI\\Main']
sub_direct = {u'GUI':[u'Main',u'Temp']}
main_file = {u'AI':[u'Analiz.py',u'Generats.py',u'OpnSrc.py',u'WinDev.py',u'DBgen.py'],
	             u'Config':[u'Init.py'],u'Database':[u'MenuSet2.py',u'PostGet.py',u'wxsq.py'],
	             u'DCC1':[u'AuiPan2.py',u'DBDev2.py',u'ListPro2.py',
	                      u'MenuDev2.py',u'ProgDev2.py',u'Proper2.py',u'ToolBar2.py',u'MLDev2.py'],
	             u'GUI':[u'BG2.py',u'MainMenu2.py',u'MainTool.py',u'proman.py',u'Start.py',u'window2.py'],
	             u'GUI\\Main':[u'DBv1.py',u'MDv1.py',u'PAv1.py',u'PGv1.py',u'PPv1.py',u'TBv1.py',u'TPv1.py',u'MLv1.py']

	              }

source_dirct = 'C:\\MyTstML\\'
target_dirct = os.getcwd() + '\\'
for dirct in main_direct:
    for update_file in main_file[dirct]:
        shutil.copyfile(source_dirct + dirct + '\\' + update_file, target_dirct + dirct + '\\' + update_file)
print(u'successful Update')


'''
def chk_update(lst_update,zip_file_name):
    for dir in list_of_main_file.keys():
        for fil in  list_of_main_file[dir] :
            if fil in lst_update:
                update_file(zip_file_name,fil,dir)


def update_file(zip_file_name,file_need_update,path_file):
    if zipfile.is_zipfile(zip_file_name):
        zipfil = zipfile.ZipFile(zip_file_name,u'r')
        nmlst = zipfil.namelist()
        for fil in nmlst:
            zipfil.extract(fil,path_file)
        zipfil.close()
'''