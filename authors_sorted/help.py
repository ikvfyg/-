import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # 或者使用其他可用的后端，例如 'Qt5Agg'、'Agg' 等
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('papers_202312192140.csv')

# 检查缺失值并将包含多个作者的列拆分成单独的作者
df['authors'] = df['authors'].apply(lambda x: x.split(', ') if pd.notna(x) else [])

# 使用explode()将每个列表元素变成一行，保留原始行的索引
df_expanded = df.explode('authors')

# 统计唯一作者数
unique_authors_count = df_expanded['authors'].nunique()

# 打印结果
print("唯一作者数:", unique_authors_count)
