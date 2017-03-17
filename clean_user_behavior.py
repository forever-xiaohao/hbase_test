# -*- coding: utf-8 -*-
"""
@Time : 2017/3/7 - 10:18
@Auther : Hao Chen
第三步清理
这一步的清理主要是将第二步处理数据，与第一步处理之后的用户行为数据进行一次merge,去除不在商品子集中的用户购买的商品行为数据
"""
import pandas as pd
import numpy as np
clean_user_behaviors_path = './output/clean_data.csv'
buy_item_p_path = './output/buy_item_p.csv'

behavior_user_data = pd.DataFrame(pd.read_csv(clean_user_behaviors_path))
buy_item_p_id = list(pd.read_csv(buy_item_p_path)['f_item_id']) # 商品子集里的商品ID

final_behaviors_data = behavior_user_data[behavior_user_data['item_id'].isin(buy_item_p_id)] # 得到商品子集里的用户行为数据
print '清理之前用户的行为数据量：'
print behavior_user_data.shape[0]
print '清理之后用户的行为数据量：'
print final_behaviors_data.shape[0]
print '总共清理的数据：'
print behavior_user_data.shape[0] - final_behaviors_data.shape[0]

print '清理之后用户行为数据预览：'
print final_behaviors_data.head()
item_behavior_4_list = []
group2 = final_behaviors_data.groupby(['behavior_type'])
for group_name, group_data in group2:
    if group_name == 4:
        item_behavior_4_list = list(group_data['item_id'].drop_duplicates()) # 在有过行为操作的商品子集里查找有购买操作的商品id

print '商品子集里有过购买操作的商品子集个数：'
print len(item_behavior_4_list)
item_behavior_4_list = pd.DataFrame(item_behavior_4_list)
item_behavior_4_list.to_csv('./output/p_item_behaviors_id.csv', encoding='utf-8', index=None)

# final_behaviors_data.to_csv('./output/final_user_behaviors_data.csv',encoding='utf-8',index=None)
"""
final_behaviors_item = behavior_user_data.merge(buy_item_p_id,how='left',left_on='item_id',right_on='f_item_id').dropna()
print '清理之前用户的行为数据量：'
print behavior_user_data.shape[0]
print '清理之后用户的行为数据量：'
print final_behaviors_item.shape[0]
print '总共清理的数据：'
print behavior_user_data.shape[0]-final_behaviors_item.shape[0]

final_behaviors_user_list = ['user_id','item_id','behavior_type','user_geohash','item_category','time']
final_user_data = final_behaviors_item[final_behaviors_user_list]
print '清理之后用户行为数据的基本信息：'
print final_user_data.info()
print '清理之后用户行为数据预览：'
print final_user_data.head()

final_user_data.to_csv('./output/final__user_behaviors_data.csv',encoding='utf-8',index=None)
"""
