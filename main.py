# -*- coding: utf-8 -*-
"""
@Time : 2017/3/5 - 12:55
@Auther : Hao Chen
第一步清理
"""
import pandas as pd
import numpy as np
import os
from zip_tools import get_file_name_list,unzip
from pandas_tools import inspect_data_info,clean_spider_data

# 文件路径
dataset_path = './dataset' # 文件所在文件夹
zip_filename = 'fresh_comp_offline.zip' # 压缩文件名
zip_filepath = os.path.join(dataset_path,zip_filename) # 压缩文件的路径

filename_list = get_file_name_list(zip_filepath)
Item_filepath = os.path.join(dataset_path,filename_list[1])
user_filepath = os.path.join(dataset_path,filename_list[2])

print user_filepath
print Item_filepath

def run_main():
    """
    主函数
    :return:
    """
    ## 解压数据
    print '开始解压数据：'
    unzip(zip_filepath,dataset_path) # 第一个参数是要解压文件路径，第二个参数是解压之后文件存放位置
    print '解压完成。'

    ## 读取数据
    user_data = pd.read_csv(user_filepath)
    Item_data = pd.read_csv(Item_filepath)

    # 查看数据基本信息
    print '查看数据基本信息：'

    print '用户行为数据信息：'
    inspect_data_info(user_data)

    print '商品信息：'
    inspect_data_info(Item_data)

    ## 数据清洗
    # 删除爬虫数据，这里默认是将只有浏览标记的信息全部删除
    clean_data = clean_spider_data(user_data,'./output/clean_data.csv')

    print '清洗之后的数据信息：-------------------------------------------'
    inspect_data_info(clean_data)
if __name__ == '__main__':
    run_main()