import traceback
import gol
from filexls import *
from testxl import *
import os
import shutil
import sys
import time
import re


def main():
#    rootdir = sys.argv[1]
#    rootdir = r'C:\FW_System_Test\GVS'
#    rootdir = r'C:\FW_System_Test\GVL\Charlie_Spec\WHAT36437 General characteristics\WHAT39861 High effieiency mode'
    rootdir = r'C:\FW_System_Test\GVL\Charlie_Spec'
    print(rootdir)

    checkstr = input('Type the string you want to search... \n')

    Record_Time = [time.ctime()]
    gol.csv_write.writerow(Record_Time+['Search String:',checkstr])
    gol.csv_write.writerow(['Filename','Row','Column','Find String'])

    check_folder(rootdir, checkstr)
    gol.csv_write.writerow([gol.foundstr])

    print()
    print(gol.foundstr)
    for i in gol.a:
        print(i)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('Error =>', e)
        print('Error =>', traceback.format_exc())
        exit()
    finally:
        pass

