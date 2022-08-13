import random

import numpy as np
import csv


'''
# 单行写入
header = ['id', '观看人数', '点赞数', '评论数']
data = [1, 1, 'English', 100]

with open('score.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    for i in range(1000):
        writer.writerow([i,random.randint(0,1000),random.randint(50,1000),random.randint(0,1000)])
'''


'''
# 多行写入
header = ['id', 'stu_id', 'course_name', 'course_score']
data = [
    [1, 1, 'English', 100],
    [2, 1, 'Math', 95],
    [3, 2, 'English', 96]
]

with open('score.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)
'''

# 读取csv文件
# with open('score.csv', encoding='UTF8') as f:
#     for row in csv.reader(f, skipinitialspace=True):
#         print(row)
