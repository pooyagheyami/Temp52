#In the name of God
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

#main_dirct = []
#main_file  = {}

'''
def main():
	with open('dir2.txt', 'r') as f:
		filelist = f.readlines()

	for fl in filelist:
		fl1 = fl.replace('\n','')
		if '-' in fl1:
			break
		if  fl1 != '' and '\\' in fl1:
			fl2 = fl1.split('\\')
			if fl2[0] not in main_dirct:

				main_dirct.append(fl2[0])
				main_file[main_dirct[-1]] = []

			if len(fl2) > 2:
				if fl2[0]+'\\'+fl2[1] not in main_dirct:

					main_dirct.append(fl2[0]+'\\'+fl2[1])
					main_file[main_dirct[-1]] = []

			if fl2[-1] not in main_file[main_dirct[-1]]:
				#lst_fil.append(fl2[-1])
				main_file[main_dirct[-1]].append(fl2[-1])
	print(filelist)
	print(main_file)
	print(main_dirct)
'''

main_direct = ['AI', 'Config', 'Database', 'DCC1', 'GUI', 'GUI\\Temp', 'GUI\\API', 'GUI\\AuiPanel', 'GUI\\Main', 'Res']

main_file = {
	'AI': ['OpnSrc.py', 'Generats.py', 'DBgen.py', 'Analiz.py'],
    'Config': ['system1.ini', 'option.ini', 'MLmethod.ini', 'Init.py'],
    'Database': ['wxsq.py', 'PostGet2.py', 'PostGet.py', 'MenuSet2.py'],
	'DCC1': ['Proper2.py', 'MenuDev2.py', 'DBDev2.py', 'ToolBar2.py', 'ProgDev2.py', 'MLDev2.py', 'ListPro2.py', 'AuiPan2.py'],
	'GUI': ['window2.py', 'Start.py', 'proman.py', 'MainTool.py', 'MainMenu2.py', 'BG2.py'],
	'GUI\\Temp': ['untitle.py', 'Demo.py'],
	'GUI\\API': ['SamPnl.py'],
	'GUI\\AuiPanel': ['tempane.py', 'PAui.py'],
	'GUI\\Main': ['TPv1.py', 'TBv1.py', 'PPv1.py', 'PGv1.py', 'PAv1.py', 'MLv1.py', 'MDv1.py', 'DBv1.py'],
	'Res': ['Allicons.py'],
}

def main():
	source_dirct = 'c:\\MPT5\\'
	target_dirct = os.getcwd()+'\\'
	for dirct in main_direct:
		for update_file in main_file[dirct]:
			shutil.copyfile(source_dirct+dirct+'\\'+update_file,target_dirct+dirct+'\\'+update_file)

	print(u'successful Update')


if __name__ == '__main__':
	main()