#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:36:34 2019

@author: mac
"""



import sys
sys.path.append(r'/Users/mac/Desktop/data/')
import autoPlot2 as aup

# 601-722
file_name = 'data-20190601-20190722-900'



input_filename='/Users/mac/Desktop/data/'+file_name+'.csv'
print(input_filename)
aup.get_index_names(input_filename)

# 601 722
#aup.auto_plot_num(input_filename,  [30], '精制-成品6月1日-7月22日')
#aup.auto_plot_numD(input_filename, [30], '成品塔-成品采出量6月22日-7月22日',8,13,0,-1)
#
#aup.auto_plot_num(input_filename,  [31], '成品塔-V-117温度6月1日-7月22日')
#aup.auto_plot_numD(input_filename,  [31], '成品塔-V-117温度6月22日-7月22日', 0,100,10,-1)

#aup.auto_plot_num(input_filename,  [32], '成品塔-V-117液位6月1日-7月22日')
#aup.auto_plot_numD(input_filename,  [32], '成品塔-V-117液位6月22日-7月22日', 30,50,0,-1)


#aup.auto_plot_numD(input_filename, [2], '精制-回收塔系统6月1日-7月22日',90,98)
#
#aup.auto_plot_num(input_filename,  [3], '精制-回收塔系统6月1日-7月22日')
#aup.auto_plot_numD(input_filename, [3], '精制-回收塔系统6月1日-7月22日',70,95)
#
#aup.auto_plot_num(input_filename,  [4], '精制-回收塔系统6月1日-7月22日')
#aup.auto_plot_numD(input_filename, [4], '精制-回收塔系统6月1日-7月22日',50,95)
#
#aup.auto_plot_num(input_filename,  [5], '精制-回收塔系统6月1日-7月22日')
#aup.auto_plot_numD(input_filename, [5], '精制-回收塔系统6月1日-7月22日',0,20)
#
#aup.auto_plot_num(input_filename,  [6], '精制-回收塔系统6月1日-7月22日')
#aup.auto_plot_numD(input_filename, [6], '精制-回收塔系统6月1日-7月22日',45,65)
#
#aup.auto_plot_num(input_filename,  [7], '精制-回收塔系统6月1日-7月22日')
#aup.auto_plot_numD(input_filename, [7], '精制-回收塔系统6月1日-7月22日',64,74)
#
#aup.auto_plot_num(input_filename,  [8], '精制-回收塔系统6月1日-7月22日')
#aup.auto_plot_numD(input_filename, [8], '精制-回收塔系统6月1日-7月22日',113,120)
