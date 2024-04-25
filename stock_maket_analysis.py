#!/usr/bin/env python
# coding: utf-8
# ## 股票信息爬取

'''
Created on 2024年04月24日
@author: libo
'''
#http://quote.eastmoney.com/center/gridlist.html
#爬取该页面股票信息

import requests
from fake_useragent import UserAgent
import json
import csv
 
def getHtml(url):
    r = requests.get(url,headers={
        'User-Agent': UserAgent().random,
    })
    r.encoding = r.apparent_encoding   # 将 HTTP 响应的编码方式设置为预测的编码方式，解决乱码问题
    return r.text
	
#num为爬取多少条记录，可手动设置
num = 20
#该地址为页面实际获取数据的接口地址
stockUrl='http://99.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112408733409809437476_1623137764048&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1623137764167:formatted'
if __name__ == '__main__':
	responseText = getHtml(stockUrl)
	jsonText = responseText.split("(")[1].split(")")[0];   # 获取json数据，去掉前后的括号
	resJson = json.loads(jsonText)    # 将json字符串转换为字典
	datas = resJson["data"]["diff"]
	datalist = []
	for data in datas:
		# if (str().startswith('6') or str(data["f12"]).startswith('3') or str(data["f12"]).startswith('0')):
		row = [data["f12"],data["f14"]]
		datalist.append(row)
	print(datalist)
			
	f =open('stock.csv','w+',encoding='utf-8',newline="")
	writer = csv.writer(f)
	writer.writerow(('代码', '名称'))
	for data in datalist:
		writer.writerow((data[0]+"\t",data[1]+"\t"))
	f.close()


# In[13]:


import csv
import json

def getStockData(url):
     headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
     }
     response = requests.get(url,headers)    
     if response.status_code == 200:
        return response.text
     return None
    # 成功访问了页面
    # 没有成功访问页面，返回None
    
#读取之前获取的个股csv丢入到一个列表中
def getStockList():
    stockList = []
    f = open('stock.csv','r',encoding='utf-8')
    f.seek(0)
    reader = csv.reader(f)
    for item in reader:
        stockList.append(item)
    f.close()
    return stockList
 
 
urlStart = 'https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery351002362199733634296_1713964489888&secid=0.'
urlEnd = '&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=120&_=1713964489890'

if __name__ == '__main__':
	stockList = getStockList()
	stockList.pop(0)
	for s in stockList:
          scode = str(s[0].split("\t")[0])   
		#0：沪市；1：深市
          url = urlStart + scode + urlEnd
          filepath = (str(s[1].split("\t")[0])+"_"+scode) + ".text" 
          i=getStockData(url)
          start1 = i.index('(')
          end1 = i.rindex(')')
          midvalue = i[start1:end1]
          start2 = midvalue.index('[')
          end2 = midvalue.rindex(']')
          json_str = midvalue[start2+1:end2]
          json_str = json_str.split('","')
          last_element = json_str[-1]
          last_element = last_element[:-1]
          filepath = filepath.replace('*','')

          with open(filepath, 'w') as f:
              f.write(last_element)
          print('股票数据已保存到文件：', filepath)
		
		


# ## 股票信息分析
# 

# In[16]:

import matplotlib.pyplot as plt
import csv
# 设置显示中文
plt.rcParams['font.sans-serif'] = ['simhei'] # 指定默认字体 
plt.rcParams['axes.unicode_minus']=False # 用来显示负号 
plt.rcParams['figure.dpi'] = 100 # 每英寸点数 

files = []
file = []
# ['日期' '股票代码' '名称' '收盘价' '最高价' '最低价' '开盘价' '前收盘' '涨跌额' '涨跌幅' '成交量' '成交金额']
def read_file(file_name):
    file_name = file_name.replace('*','')
    with open(file_name, 'r') as f:
         data = f.read()
         data = data.split(',')
         return data

def get_files_path():
    stock_list=getStockList()
    paths = []
    for stock in stock_list[1:]:
        p = stock[1].strip()+"_"+stock[0].strip()+".text"
        b = stock[1].strip()+"_"+stock[0].strip()  
        data = read_file(p)
        file = data
        print(type(data))
        if len(data)>1:
            file.append(b) 
        files.append(file)
get_files_path()
print(files)

def get_image(data_dict):
     keys = data_dict.keys()
     values = data_dict.values()
     values = list(map(float, values))

     plt.plot(keys,values)
     plt.xticks(rotation='vertical')
     plt.title('股票开盘价2024-04-25')
     plt.xlabel('股票代码')
     plt.ylabel('开盘价')
     plt.tight_layout()
     plt.show()
     

print(len(files))
open_dict,end_dict,high_dict,low_dict = {},{},{},{}

for file in files:
    if len(file)== 12:
         open_dict[file[-1]] = file[1]        # 这里可以换成for循环的形式，但是为了方便理解，就这样写了
         end_dict[file[-1]] = file[2]
         high_dict[file[-1]] = file[3]
         low_dict[file[-1]] = file[4]
date = files[0][0]
data = str(date)
get_image(open_dict)


# ## end
