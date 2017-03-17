# -*- coding: utf-8 -*-
"""
@Time : 2017/3/7 - 16:03
@Auther : Hao Chen
该程序是过滤掉在商品子集中，无收藏、购物车、购买的用户行为数据
"""
import pandas as pd
import numpy as np
import datetime
from pandas_tools import inspect_data_info,tianchi_time_handle
item_id_p_path = './output/not_in_item_id.csv'
p_item_behavior_id_path = './output/p_item_behaviors_id.csv'

item_id_p_data = pd.read_csv(item_id_p_path)
print item_id_p_data.head()
p_item_behavior_id_data = pd.read_csv(p_item_behavior_id_path)
print 'item的数据长度：%i'%item_id_p_data.size
print 'p_item的数据长度：%i'%p_item_behavior_id_data.size
item_final_id = pd.concat([item_id_p_data['not_p_item'],p_item_behavior_id_data['p_item']],axis=0)
item_list = list(item_final_id)

print item_final_id.size
print item_final_id.head()
clean_data = pd.read_csv('./output/clean_data.csv')
print type(clean_data)
clean_2_data =clean_data[clean_data['item_id'].isin(item_list)]


print '原有数据量：%i条。'%clean_data.shape[0]
print '清理了%i条。'%(clean_data.shape[0] - clean_2_data.shape[0])

clean_2_data.to_csv('./output/clean_2_data.csv',encoding='utf-8',index=None)

print '清洗之后的数据信息：-------------------------------------------'
inspect_data_info(clean_2_data)






