# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:50:38 2019

@author: 陈婕
"""

import csv

def findtable(filename, maxnum, filenum):
    wholetable = []
    with open(filename, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            wholetable.append(row)
#        print(wholetable)
    table = []
    table.append(wholetable[0])
    for i in range(len(wholetable)):
        if i != 0 and i != 1:
            if float(wholetable[i][2]) == maxnum:
                for j in range(i-10,i+11):
                    table.append(wholetable[j])
    starttime = float(table[1][0])
    for i in range(1,len(table)):
        table[i][0] = float(table[i][0]) - starttime
    newfilename = str(filenum) + '.csv'
    with open(newfilename, mode='w',newline ='') as new_file:
        new_writer = csv.writer(new_file, delimiter=',')
        for i in range(len(table)):
            new_writer.writerow(table[i])
    return table

findtable('58_lac.csv',82.6969,58)