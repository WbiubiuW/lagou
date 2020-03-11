# encoding: GBK

import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import csv

dd = pd.read_csv("../data/page_data.csv",encoding='GBK',error_bad_lines=False)
print(len(dd))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'

region =dd.groupby('����').mean()['н��']

asd,sdf = plt.subplots(1,1,dpi=250)
region.plot(kind='bar',x='����',y='н��', title='��������н�����',ax=sdf)
plt.legend(['ƽ������'])
plt.savefig('н�ʵ���.jpg')
plt.show()

region =dd.groupby('ѧ��').mean()['н��']

asd,sdf = plt.subplots(1,1,dpi=250)
region.plot(kind='bar',x='ѧ��',y='н��', title='ѧ����н�����',ax=sdf)
plt.legend(['ƽ������'])
plt.savefig('ѧ����н�����.jpg')
plt.show()

region =dd.groupby('��������').mean()['н��']

asd,sdf = plt.subplots(1,1,dpi=250)
region.plot(kind='bar',x='��������',y='н��', title='����������н�����',ax=sdf)
plt.legend(['ƽ������'])
plt.savefig('����������н�����.jpg')
plt.show()

region =dd.groupby('ְλ').mean()['н��']

asd,sdf = plt.subplots(1,1,dpi=1080)
region.plot(kind='bar',x='ְλ',y='н��', title='����������н�����',ax=sdf)
plt.legend(['ƽ������'])
plt.savefig('ְλ��н�����.jpg')
plt.show()