import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('../authors_sorted/papers_202312192140.csv')

# 统计每位作者发表的论文数
authors_counts = df['authors'].value_counts()

# 筛选发表论文数大于5篇的作者
authors_over_5 = authors_counts[authors_counts > 5].reset_index()
authors_over_5.columns = ['author', 'papers_count']

# 按照论文数排序
authors_sorted = authors_over_5.sort_values(by='papers_count', ascending=False)

# 生成新的CSV文件
authors_sorted.to_csv('authors_sorted_more_than_5.csv', index=False)


import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('../authors_sorted/papers_202312192140.csv')

# 统计每位作者发表的论文数
authors_counts = df['authors'].value_counts()

# 筛选发表论文数大于1篇的作者
authors_over_1 = authors_counts[authors_counts > 1].reset_index()
authors_over_1.columns = ['author', 'papers_count']

# 按照论文数排序
authors_sorted = authors_over_1.sort_values(by='papers_count', ascending=False)

# 生成新的CSV文件
authors_sorted.to_csv('authors_sorted_more_than_1.csv', index=False)

import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('../authors_sorted/papers_202312192140.csv')

# 统计每位作者发表的论文数
authors_counts = df['authors'].value_counts()

# 筛选发表论文数大于2篇的作者
authors_over_2 = authors_counts[authors_counts > 2].reset_index()
authors_over_2.columns = ['author', 'papers_count']

# 按照论文数排序
authors_sorted = authors_over_2.sort_values(by='papers_count', ascending=False)

# 生成新的CSV文件
authors_sorted.to_csv('authors_sorted_more_than_2.csv', index=False)


import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('../authors_sorted/papers_202312192140.csv')

# 统计每位作者发表的论文数
authors_counts = df['authors'].value_counts()

# 筛选发表论文数大于3篇的作者
authors_over_3 = authors_counts[authors_counts > 3].reset_index()
authors_over_3.columns = ['author', 'papers_count']

# 按照论文数排序
authors_sorted = authors_over_3.sort_values(by='papers_count', ascending=False)

# 生成新的CSV文件
authors_sorted.to_csv('authors_sorted_more_than_3.csv', index=False)

import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('../authors_sorted/papers_202312192140.csv')

# 统计每位作者发表的论文数
authors_counts = df['authors'].value_counts()
print(authors_counts)

# 筛选发表论文数大于4篇的作者
authors_over_4 = authors_counts[authors_counts > 4].reset_index()
authors_over_4.columns = ['author', 'papers_count']

# 按照论文数排序
authors_sorted = authors_over_4.sort_values(by='papers_count', ascending=False)

# 生成新的CSV文件
authors_sorted.to_csv('authors_sorted_more_than_4.csv', index=False)

