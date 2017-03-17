# -*- coding: utf-8 -*-
"""
@Time : 2017/3/7 - 9:23
@Auther : Hao Chen
第二步清理
1、对商品子集进行过滤----过滤掉没有在商品子集中的数据（对商品子集无收藏、购物车、购买）
2、不考虑商品的空间问题
"""
import pandas as pd
import numpy as np

item_data_path = './dataset/fresh_comp_offline/tianchi_fresh_comp_train_item.csv'
buy_item_data_path = './output/buy_user_data.csv'

item_data = pd.read_csv(item_data_path) # 获得商品子集列表
buy_item = pd.read_csv(buy_item_data_path) # 获得购买商品用户的列表

# 从购买商量数据集中得到用户购买的商品ID
buy_item_id = pd.DataFrame(buy_item['item_id'].drop_duplicates()) # 去掉重复值
print buy_item_id.info()
print '用户购买的商品有%i个。' %buy_item_id.shape[0]

# 商品子集中商品ID
item_list = ['item_id','item_category']
item_data2 = item_data[item_list].drop_duplicates()
item_data2.columns = [('f_' + i) for i in item_list]
item_id = pd.DataFrame(item_data2)
print item_id.info()
print '商品子集中的商品有%i个。' %item_id.shape[0]
final_item_id = pd.DataFrame()
final_item_id = buy_item_id.merge(item_id,how='left',left_on='item_id',right_on='f_item_id')

null_item_data = final_item_id[final_item_id['f_item_category'].isnull()]
null_item_id = null_item_data['item_id'].drop_duplicates() # 不在商品子集里的商品ID

print '不在商品子集中的商品个数：'
print null_item_id.size
null_item_id.to_csv('./output/not_in_item_id.csv',encoding='utf-8',index=None)
final_item_id = final_item_id.drop_duplicates()# 去掉重复值
print '在商品子集中用户有操作的商品有%i种。'%final_item_id.shape[0]
print final_item_id.head()
final_item = final_item_id[['f_item_id','f_item_category']].dropna()
final_item.to_csv('./output/buy_item_p.csv',encoding='utf-8',index=None)


