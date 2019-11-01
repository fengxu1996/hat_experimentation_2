# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
# 上一个程序把co-author合并了(同authorID,同name为同一个人. 同affID, 同name为同一个人)
#
# 现在考虑用之前讨论的方式去筛选(即:
# 1. 找杰青们的first year的min和max，当作筛选条件1（上一个程序已经找过了）
# min max为1980 2007
# 2016太晚了，发现对有些杰青，数据集里只有他获奖后的论文，获奖前没有论文，（要把这些杰青删掉）
#
# 2. 用 学术年龄>=10 作为条件筛选，学术年龄用co-author的 last paper year 减去 first paper year
# 对co-author用这个条件筛选的话，对杰青也应该这样筛选下（保留last paper year - first paper year >= 10的杰青，大概还剩929人）
# )
#
# 这里先找 co-author 的 first paper year 和 last paper year
# 上一步找到了r"E:\FengXu\result1\coAuthorPaperID_coAuthorPaperYear.txt"
#
# 已有
# r"E:\FengXu\result1\coAuthorID_coAuthorPaperMinYear_coAuthorPaperMaxYear.txt"
# 续上,继续找
#
# 上一个程序得到path_out1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
#             r"(affID_sortedName)\1\fxID_affID_sortedName_coAuthorID_coAuthorPaperMinYear_coAuthorPaperMaxYear.txt"

这里计算每个唯一fxID对应的minYear 和lastYear，然后开始利用上面（1980 <= minYear <= 2007）和（last paper year - first paper year >= 10）

"""
import pandas as pd
import csv

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\1\fxID_affID_sortedName_coAuthorID_coAuthorPaperMinYear_coAuthorPaperMaxYear.txt"

data = pd.read_csv(path1, sep='\t')
data = data.astype
data1 = data.groupby(['fxID'])['coAuthorPaperMinYear'].min()
data2 = data.groupby(['fxID'])['coAuthorPaperMaxYear'].max()

data1 = data1.reset_index()
data2 = data2.reset_index()

data1.columns = ['fxID', 'minYear']
data2.columns = ['fxID', 'maxYear']

data_ = pd.merge(data1, data2, on=['fxID'], how='inner')
print('筛选前co-author的个数', data_.shape[0])

# data_ = data_[1980 <= data_['minYear'] <= 2007]
data_ = data_[((1980 <= data_['minYear'])&(data_['minYear'] <= 2007))]
print('筛选条件一', data_.shape[0])

data_ = data_[data_['maxYear'] - data_['minYear'] >= 10]
print('筛选条件二', data_.shape[0])

path_out1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\1\filter_" \
            r"fxID_minYear_maxYear.txt"
data_.to_csv(path_out1, sep='\t', index=False)
