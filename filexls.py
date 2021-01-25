# -- coding: utf-8 --
import os
from testxl import *

def check_folder(folder, strcheck):
    filextern = "xlsm"

    list = os.listdir(folder)
    #print(list)

    os.chdir(folder)
    for i in range(0,len(list)):
        if os.path.isfile(list[i]):
            if filextern in str(list[i]):
#                print(list[i])
                checkfile(list[i], strcheck)
        else:
            if '.' in str(list[i]):
                 '''print()'''
            elif 'Charlie_Base' in str(list[i]):
                print('Skip Charlie_Base')
            elif 'Charlie_Spec' in str(list[i]):
                print('Skip Charlie_Spec')
            else:
                #print('folder '+list[i])
                check_folder(list[i], strcheck)

    os.chdir('..')

#rootdir = os.getcwd()
#allfile = list_all_files(rootdir)
#print(allfile)