# -*- coding: utf-8 -*-
"""
@Time : 2017/3/5 - 12:57
@Auther : Hao Chen
"""
import zipfile
def unzip(zip_filepath,dest_path):
    """
    解压文件
    :param zip_filepath:
    :param dest_path:
    :return:
    """
    with zipfile.ZipFile(zip_filepath) as zf:
        zf.extractall(path=dest_path)
def get_file_name_list(zip_filepath):
    """
    获取数据文件名
    :param zip_filepath:
    :return:
    """
    with zipfile.ZipFile(zip_filepath) as zf:
        return zf.namelist()