# -*- coding: utf-8 -*-
"""
@Time : 2017/3/6 - 16:45
@Auther : Hao Chen
"""
import pandas as pd
import numpy as np
import os
import datetime
"""
from pandas_tools import inspect_data_info,clean_spider_data
clean_user_data_path = './output/buy_user_data.csv'
user_data = pd.read_csv(clean_user_data_path)
inspect_data_info(user_data)
clean_user = user_data['user_id'].drop_duplicates()
print clean_user.size
dict1={'buy_item': [1,2,3,4,5,6,7]}
dict2={'item_id': [1,3,4,6,8],
       'category':['a','c','d','g','f']}

df_obj_1 = pd.DataFrame(dict1)
df_obj_2 = pd.DataFrame(dict2)
test = df_obj_1.merge(df_obj_2,how='left',left_on='buy_item',right_on='item_id')
print df_obj_1
print df_obj_2
test = pd.DataFrame(test)
print test
print test[test['category'].isnull()]
"""
t = ['2016-03-21 12','2014-05-26 16','2014-12-11 2']
str = list(t)
# 将时间切分，只要年月日
time_Y_m_d = [time1.split(' ')[0] for time1 in str]
# datelset = [datetime.datetime.strptime(time,'%Y-%m-%d') for time in str]
# 将日期字符串转换成日期
date_lst = [datetime.datetime.strptime(endate,'%Y')]

