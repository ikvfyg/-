'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-12-19 20:49:45
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-12-19 21:03:35
FilePath: \ReptileProject_V1.0\main_excel.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool, cpu_count
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import re
import pandas as pd


def sanitize_text(text):
    sanitized_text = re.sub(r'[^\x20-\x7E]', '', text)
    return sanitized_text


def process_year(year):
    data = {
        '序号': [],
        '论文题目': [],
        '作者': [],
        '摘要': [],
        '时间': []
    }

    session = requests.Session()
    retry = Retry(total=5, backoff_factor=0.1,status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    url = f"https://proceedings.neurips.cc/paper_files/paper/{year}"
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"无法获取年份 {year} 的页面: {e}")
        return

    print(f"正在处理年份 {year} 的页面...")
    soup = BeautifulSoup(response.content, 'html.parser')

    paper_list = soup.find('ul', class_='paper-list')

    if paper_list:
        for index, li_tag in enumerate(paper_list.find_all('li'), start=1):
            subpage_relative_url = li_tag.find('a')['href']
            subpage_full_url = f"https://proceedings.neurips.cc{subpage_relative_url}"

            try:
                subpage_response = session.get(subpage_full_url, timeout=10)
                subpage_response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"无法获取子页面 {subpage_full_url}: {e}")
                continue

            print(f"  处理子页面 {subpage_full_url}...")
            subpage_soup = BeautifulSoup(subpage_response.content, 'html.parser')
            title = subpage_soup.find('div', class_='col').find('h4').get_text(strip=True)
            authors = subpage_soup.find('div', class_='col').find_all('h4')[1].find_next('p').get_text(strip=True)
            abstract_tag = subpage_soup.find('h4', text='Abstract')

            if abstract_tag:
                abstract = abstract_tag.find_next('p').get_text(strip=True)
                sanitized_abstract = sanitize_text(abstract)
                data['序号'].append(index)
                data['论文题目'].append(title)
                data['作者'].append(authors)
                data['摘要'].append(sanitized_abstract)
                data['时间'].append(year)

        # 将数据转换为 DataFrame
        df = pd.DataFrame(data)

        # 将 DataFrame 保存到 Excel 文件
        excel_file_name = f'neurips_papers_{year}.xlsx'
        df.to_excel(excel_file_name, index=False)
        print(f'Excel 文件已创建并保存成功: {excel_file_name}')


if __name__ == "__main__":
    years_to_scrape = list(range(1987, 2023))
    with Pool(processes=cpu_count()) as pool:
        pool.map(process_year, years_to_scrape)
