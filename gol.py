'''define the gobal varies that can be used in all files'''
import csv


csvfile = open('Record_Result.csv', 'a', newline='')
csv_write = csv.writer(csvfile, dialect='excel')

a = []
foundstr = "................................    NO Found    ............................."