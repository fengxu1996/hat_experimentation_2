# -*- coding: utf-8 -*-
# !/usr/bin/env python

path1 = r"E:\FengXu\Data\awardYear_englishName_affID_chineseName.txt"
path2 = r"E:\FengXu\result\1_JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName.txt"

with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        if len(line) != 6:
            print(line)