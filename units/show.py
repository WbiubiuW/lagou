# encoding: GBK

import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import csv

dd = pd.read_csv("../data/page_data.csv",encoding='GBK',error_bad_lines=False)
print(len(dd))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'

region =dd.groupby('地区').mean()['薪资']

asd,sdf = plt.subplots(1,1,dpi=250)
region.plot(kind='bar',x='地区',y='薪资', title='各个区域薪资情况',ax=sdf)
plt.legend(['平均工资'])
plt.savefig('薪资地区.jpg')
plt.show()

region =dd.groupby('学历').mean()['薪资']

asd,sdf = plt.subplots(1,1,dpi=250)
region.plot(kind='bar',x='学历',y='薪资', title='学历与薪资情况',ax=sdf)
plt.legend(['平均工资'])
plt.savefig('学历与薪资情况.jpg')
plt.show()

region =dd.groupby('工作年限').mean()['薪资']

asd,sdf = plt.subplots(1,1,dpi=250)
region.plot(kind='bar',x='工作年限',y='薪资', title='工作年限与薪资情况',ax=sdf)
plt.legend(['平均工资'])
plt.savefig('工作年限与薪资情况.jpg')
plt.show()

region =dd.groupby('职位').mean()['薪资']

asd,sdf = plt.subplots(1,1,dpi=1080)
region.plot(kind='bar',x='职位',y='薪资', title='工作年限与薪资情况',ax=sdf)
plt.legend(['平均工资'])
plt.savefig('职位与薪资情况.jpg')
plt.show()