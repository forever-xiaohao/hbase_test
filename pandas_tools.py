# -*- coding: utf-8 -*-
"""
@Time : 2017/3/5 - 12:56
@Auther : Hao Chen
"""
import pandas as pd
import numpy as np
def inspect_data_info(df_data):
    """
    查看数据的基本信息
    :param df_data:
    :return:
    """
    print '数据基本信息：'
    print df_data.info()

    print '数据有%i行，%i列' %(df_data.shape[0],df_data.shape[1])

    print df_data.head()

def clean_spider_data(df_data,save_filepath=''):
    """
    清理爬虫数据
    :param df_data:
    :return:
    """
    user_list = [] # 列表存储正常用户ID
    df_group = df_data.groupby(['behavior_type'])
    for group_name,group_data in df_group:
        print group_name
        print type(group_name)
        if group_name == 4:
            user_list = list(group_data['user_id'].drop_duplicates())
            group_data.to_csv('./output/buy_user_data.csv',encoding='utf-8',index=None)

    user_clean_data = df_data[df_data['user_id'].isin(user_list)]
    print '购买商品的用户有：%i个' %len(user_list)
    print '清除数据有%i行。' %(df_data.shape[0]-user_clean_data.shape[0])
    if save_filepath !=  '':
        user_clean_data.to_csv(save_filepath,encoding='utf-8',index=None)
    return user_clean_data

def tianchi_time_handle(clean_data):
    """
    对时间进行处理，只保留年月日
    :param clean_data:
    :return: 处理之后的数据集
    """
    # 获取时间列
    date_lst = list(clean_data['time'])
    # 将时间切分，只保留年月日
    date_time = [time.split(' ')[0] for time in date_lst]
    # 保存数据为DataFrame格式
    final_time = pd.DataFrame(date_time, columns=['time'])
    ## 将数据拼接
    # 索引列表
    behaviors_lst = ['user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category']
    other_data = clean_data[behaviors_lst]
    clean_data = pd.concat([other_data, final_time['time']], axis=1)
    return clean_data

