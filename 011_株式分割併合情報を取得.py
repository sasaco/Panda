# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import requests
from bs4 import BeautifulSoup
# %% [markdown]
# ## 株式分割情報を取得
# 
# 松井証券 株式分割情報
# 
# https://ca.image.jp/matsui/?type=0&page=1

# %%
request = requests.get('https://ca.image.jp/matsui/?type=0&page=1')

soup = BeautifulSoup(request.content, 'html.parser') # BeautifulSoupの初期化

# テーブルを指定
table = soup.findAll("table", {"class":"commontbl"})[0]
rows = table.findAll("tr")

for row in rows:
    for cell in row.findAll(['td']):
        print(cell.get_text())


# %%


