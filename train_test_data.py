# -*- coding: utf-8 -*-
"""
@Time : 2017/3/8 - 15:11
@Auther : Hao Chen
训练集和测试集构造
训练集：前29天的数据
测试集：最后一天18号的数据
"""
import pandas as pd
import numpy as np
import datetime
from pandas_tools import inspect_data_info,tianchi_time_handle

def run_main():
    # 读取清洗之后的数据
    clean_data_path = './output/clean_2_data.csv'
    # 读取数据
    clean_data = pd.read_csv(clean_data_path)
    ## 对时间进行处理,去掉小时，函数返回数据集
    behaviors_data = tianchi_time_handle(clean_data)
    inspect_data_info(behaviors_data)
    behaviors_data.to_string('./output/behaviors_data.csv',index=None)


"""
    # 抽取时间
    time = sorted(list(behaviors_data

    ['time'].drop_duplicates()))
    train_time = time[:-1]
    print train_time
    test_time = time[-1:]
    print test_time
    ## 分割训练集，测试集
    index_list = ['user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category','time']
    train_data = behaviors_data[behaviors_data['time'].isin(train_time)]
    print '训练集数据的基本信息：'
    inspect_data_info(train_data)
    train_data[index_list].to_csv('./output/train_data.csv',encoding='utf-8',index=None)
    test_data = behaviors_data[behaviors_data['time'].isin(test_time)].reset_index()
    test_data[index_list].to_csv('./output/test_data.csv',encoding='utf-8',index=None)
    print '测试集数据的基本信息：'
    inspect_data_info(test_data)
"""
if __name__ == '__main__':
    run_main()


