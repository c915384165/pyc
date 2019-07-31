#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 12:42:38 2019

@author: macpro
"""
###################################################################
###################################################################
# This function is used for auto plot line
###################################################################

# import numpy pandas matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv 
# import LinearRegression
# from sklearn.linear_model import LinearRegression

#######################################
# 中文显示
#######################################
import matplotlib
matplotlib.rcParams['font.family']='Arial Unicode MS'
matplotlib.rcParams['axes.unicode_minus'] = False

# plt.figure(dpi=128, figsize=(8,5))


def get_index_names(input_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for index, column_header in enumerate(header_row):
            print(index, column_header)
#        header_row = next(reader)
#        for index, column_header in enumerate(header_row):
#            print(index, column_header)



def auto_plot(input_csv_file_name, y_column_number, plt_x_label, plt_y_label, save_fig_name,
              fig_title):
    file_name = input_csv_file_name
    df = pd.read_csv(file_name)
    # CSV in date&time
    df['date&time'] = pd.to_datetime(df['date&time'])
    my_time_date = np.asarray(df['date&time'])
#    print(my_time_date[0])
#    print(my_time_date[-1])
#    plt.xlim(my_time_date[0], my_time_date[-1])
    a = df[y_column_number]
    plt.figure(dpi=128, figsize=(11,4))
    plt.xlabel(plt_x_label, fontsize=14)
    plt.ylabel(plt_y_label, fontsize=14)
    plt.title(fig_title, fontsize=16)
#    plt.ylim(0,1)
    plt.grid(True)
#    plt.xlim(my_time_date[0], my_time_date[-1])
#    plt.ylim()
    plt.plot(my_time_date, a)
    plt.gcf().autofmt_xdate()
    plt.savefig(save_fig_name, dpi=128)


def auto_plotD(input_csv_file_name, y_column_number, plt_x_label, plt_y_label, save_fig_name,
              fig_title, ylim_min, ylim_max):
    file_name = input_csv_file_name
    df = pd.read_csv(file_name)
    # CSV in date&time
    df['date&time'] = pd.to_datetime(df['date&time'])
    my_time_date = np.asarray(df['date&time'])
    #######################################
    # 平均值线
#    meanA = a.mean()
    # aArray = np.linspace(meanA,meanA,len(x))
    #######################################
#    print(my_time_date[0])
#    print(my_time_date[-1])
#    plt.xlim(my_time_date[0], my_time_date[-1])
    a = df[y_column_number]
    plt.figure(dpi=128, figsize=(11,4))
    plt.xlabel(plt_x_label, fontsize=14)
    plt.ylabel(plt_y_label, fontsize=14)
    plt.title(fig_title, fontsize=16)
    plt.ylim(ylim_min,ylim_max)
    plt.grid(True)
#    plt.xlim(my_time_date[0], my_time_date[-1])
#    plt.ylim()
    plt.plot(my_time_date, a)
    plt.gcf().autofmt_xdate()
    plt.savefig(save_fig_name, dpi=128)
#########################################
# get the min/max list of numbers
########################################
    
    
def get_minlistindex(input_array, nums):
    min_list3 = []
    copy_array = input_array.copy()
    mean_value = input_array.mean()
    for i in range(nums):
        min_index = np.argmin(copy_array)
        min_list3.append(min_index)
        copy_array[min_index] = mean_value
    return min_list3


def get_maxlistindex(input_array, nums):
    max_list3 = []
    copy_array = input_array.copy()
    mean_value = input_array.mean()
    for i in range(nums):
        max_index = np.argmax(copy_array)
        max_list3.append(max_index)
        copy_array[max_index] = mean_value
    return max_list3


def auto_analysis(input_csv, y_column, plt_y_label):
    file_name = input_csv
    df = pd.read_csv(file_name)
    # CSV in date&time
    df['date&time'] = pd.to_datetime(df['date&time'])
    my_time_date = np.asarray(df['date&time'])
    a = np.asarray(df[y_column])
    # plt max min
    maxlist = get_maxlistindex(a, 3)
    minlist = get_minlistindex(a, 3)
    x = 1
    for i in maxlist:
        print('%s 第 %d 大值是 %.4f 在 %s' % (plt_y_label,x , a[i], pd.to_datetime(my_time_date[i])))
        x = x+1
    y = 1
    for i in minlist:
        print('%s 第 %d 小值是 %.4f 在 %s' % (plt_y_label,y , a[i], pd.to_datetime(my_time_date[i])))
        y = x+1
#    print('%s 最小值是 %.4f 在 %s' % (plt_y_label, a[min_id], pd.to_datetime(my_time_date[min_id])))
    print('%s 平均值为：%.4f' % (plt_y_label, a.mean()))
    print('最大增加值：%.4f, 最大增幅百分比： %.2f %%' % ((a[maxlist[0]]-a.mean()), (a[maxlist[0]]-a.mean())/a.mean()*100))
    print('最大降低值：%.4f, 最大降幅百分比： %.2f %%' % ((a.mean()-a[minlist[0]]), (a.mean()-a[minlist[0]])/a.mean()*100))


def auto_plot_num(input_csv_file_name, y_column_number, fig_title):
    index_name_list = []
    with open(input_csv_file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for index, column_header in enumerate(header_row):
            index_name_list.append(column_header)
    for i in y_column_number:
        fig_name = fig_title + '_fig-' + str(i)
        auto_plot(input_csv_file_name, index_name_list[i], '日期',
                 index_name_list[i], fig_name, fig_title)
        auto_analysis(input_csv_file_name, index_name_list[i], index_name_list[i])


def auto_plot_numD(input_csv_file_name, y_column_number, fig_title, ylim_min, ylim_max):
    index_name_list = []
    with open(input_csv_file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for index, column_header in enumerate(header_row):
            index_name_list.append(column_header)
    for i in y_column_number:
        fig_name = fig_title + '_fig-' + str(i)
        auto_plotD(input_csv_file_name, index_name_list[i], '日期',
                 index_name_list[i], fig_name, fig_title, ylim_min, ylim_max)
        auto_analysis(input_csv_file_name, index_name_list[i], index_name_list[i])


