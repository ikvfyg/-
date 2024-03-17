import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from tqdm import tqdm
import time

# 读取CSV文件（假设分隔符为逗号）
file_path = 'papers_202312192140.csv'
df = pd.read_csv(file_path)

# 提取abstract列的文本
abstracts = df['abstract'].dropna().tolist()

# 设置每隔一定行数输出一次进度
progress_interval = 500
total_rows = len(abstracts)

# 生成词云
wordcloud = WordCloud(width=1000, height=600, max_words=500, max_font_size=100, background_color='white').generate(' '.join(abstracts))

# 使用tqdm输出进度
for i in tqdm(range(0, total_rows, progress_interval), desc="Processing rows"):
    time.sleep(0.1)  # 模拟处理数据的耗时操作

# 显示词云图
plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# 保存词云图到本地文件
wordcloud.to_file("wordcloud_output.png")

# 显示保存成功消息
print("Wordcloud image saved to wordcloud_output.png")
