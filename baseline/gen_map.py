#!/usr/bin/env python
from __future__ import print_function
import lxml.etree as etree
import random
import matplotlib.pyplot as plt
import numpy as np
def rand():
    return random.randint(0, 1)
def draw(field, text_num):
    nrows, ncols = 20, 20
    image = np.empty((nrows, ncols))
    for i in range(0, 20):
        for j in range(0, 20):
            image[i][j] = field[i][j]
    image = image.reshape((nrows, ncols))
    plt.matshow(image)
    name = text_num + '.png'
    plt.savefig(name)
def gen_field():
    k = 21
    field = []
    for i in range(20):
        field.append([])
        for j in range(20):
            field[i].append(0)
    for i in range(4):
        for j in range(4):
            x = rand()
            if x == 1:
                for u in range(i * 5, (i + 1) * 5):
                    field[u][j * 5] = 1
                for u in range(j * 5, (j + 1) * 5):
                    field[i * 5][u] = 1

    ans = []
    for i in range (20):
        res = []
        for j in range(20):
            res.append(field[i][j])
            #print(field[i][j])
        ans.append(res)
    return ans

for k in range(20):
    root = etree.Element("root")
    map = etree.SubElement(root, "map")
    width = etree.SubElement(map, "width")
    width.text = "20"
    height = etree.SubElement(map, "height")
    height.text = "20"
    startx = etree.SubElement(map, "startx", number="0")
    startx.text = "5"
    starty = etree.SubElement(map, "starty", number="0")
    starty.text = "3"
    finishx = etree.SubElement(map, "finishx", number="0")
    finishx.text = "4"
    finishy = etree.SubElement(map, "finishy", number="0")
    finishy.text = "7"
    grid = etree.SubElement(map, "grid")
    field = gen_field()
    for i in range(int(height.text)):
        row = etree.SubElement(grid, "row")
        a = ""
        for j in range(int(width.text)):
            x = field[i][j]
            a += str(x)
            if (j + 1 != int(width.text)):
                a += " "
            row.text = a
    algorithm = etree.SubElement(root, "algorithm", MapNameSufix="AStar")
    metrictype = etree.SubElement(algorithm, "metrictype")
    metrictype.text = "euclid"
    searchtype = etree.SubElement(algorithm, "searchtype")
    searchtype.text = "astar"
    hweight = etree.SubElement(algorithm, "hweight")
    hweight.text = "1"
    breakingties = etree.SubElement(algorithm, "breakingties")
    breakingties.text = "g-max"
    linecost = etree.SubElement(algorithm, "linecost")
    linecost.text = "1"
    diagonalcost = etree.SubElement(algorithm, "diagonalcost")
    diagonalcost.text = "1.41421356237"
    bottleneck = etree.SubElement(algorithm, "bottleneck")
    bottleneck.text = "0"
    allowdiagonal = etree.SubElement(algorithm, "allowdiagonal")
    allowdiagonal.text = "1"
    
    options = etree.SubElement(root, "options")
    loglevel = etree.SubElement(options, "loglevel")
    loglevel.text = "1"
    logpath = etree.SubElement(options, "logpath")
    logfilename = etree.SubElement(options, "logfilename")
    
    log = etree.SubElement(root, "log")
    mapfilename = etree.SubElement(log, "mapfilename")
    text_num = str(k + 1)
    mapfilename.text = text_num + ".xml"
    summary = etree.SubElement(log, "summary", numberofsteps="2",nodescreated="4",length="11",time="0.1")
    path = etree.SubElement(log, "path")
    for i in range(int(height.text)):
        row = etree.SubElement(path, "row")
        row.text = root[0][6][i].text
    hplevel = etree.SubElement(log, "hplevel")
    etree.SubElement(hplevel, "section", {'number':'0', 'start.x':'5', 'start.y' : '3', 'finish.x' : '1', 'finish.y' : '4', 'length' : '4'})
    etree.SubElement(hplevel, "section", {'number':'1', 'start.x':'1', 'start.y' : '4', 'finish.x' : '1', 'finish.y' : '6'}, length="3")
    etree.SubElement(hplevel, "section", {'number':'2', 'start.x':'1', 'start.y' : '6', 'finish.x' : '4', 'finish.y' : '7'}, length="4")
    draw(field, text_num)
    #print(etree.tostring(root, pretty_print=True))
    tree = etree.ElementTree(root)
    tree.write("/Users/denissurin/Downloads/isyt2017rl-master/baseline/data/my_raw_test/" + mapfilename.text)

