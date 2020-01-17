#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:21:36 2020

@author: wenhan
"""

from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='Visualize Pen Input')
parser.add_argument('fname')
args = parser.parse_args()

# change source directory for own use
path = '/home/wenhan/git/UROPS2020'

#file name should be ****.scgink
file = f'{args.fname}'   

fullpath = path+'/'+file

with open("test.", "r") as f:
    
    contents = f.read()

    soup = BeautifulSoup(contents, 'xml')
    allstrokes = {}
    counter = 0
    for tag in soup.find_all("stroke"):
        text = str(tag.text).split(' ')
        x=[]
        y=[]
        for i in range(len(text)):
            if i%2==0:
                x.append(float(text[i]))
            else:
                y.append(float(text[i]))
        coordinates = {}
        coordinates['x'] = x
        coordinates['y'] = y
        
        allstrokes[counter] = coordinates
        counter+=1

f.close()

newf= open("test.scgink","w+")
newf.write('SCG_INK\n')
newf.write(str(len(allstrokes))+'\n')
for i in range(counter):
    stroke = allstrokes[i]
    pts = len(stroke['x'])
    newf.write(str(pts)+'\n')
    for j in range(pts):
        newf.write(str(stroke['x'][j])+' '+str(stroke['y'][j])+'\n')
newf.close()