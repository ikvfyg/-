import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # 或者使用其他可用的后端，例如 'Qt5Agg'、'Agg' 等
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('authors_sorted_more_than_3.csv')


# 提取作者和论文数量的列
authors = df['author']
papers_count = df['papers_count']

# 创建水平条形图
plt.barh(authors, papers_count, color='skyblue')
plt.xlabel('Papers Count')
plt.title('Papers Count by Author more than 3')
plt.show()