import jieba
from wordcloud import WordCloud
from PIL import Image
from PIL import ImageFont
import numpy as np

jieba.load_userdict('../data/userdict.txt')

font = 'simfang.ttf'
content = (open('../data/jodInfo.txt','r',encoding='utf-8')).read()
cut = jieba.cut(content,HMM=False)

tup = ('功能测试','性能测试','自动化测试','安全测试','兼容性测试','产品测试','app测试','压力测试',
       'Python','Java','Jmeter','C','C++','linux','jenkins','PHP','shell','JIRA','TestLink','git','svn',
       'SQL Server','MySql','loadrunner')

jieba.suggest_freq(tup,True)
#jieba.add_word('linux')

cut_content = ' '.join(cut)
img = Image.open('22.jpg') # 以什么图片进行显示
img_array = np.array(img) # 将图片转换为数组

wc = WordCloud(
    background_color='white',
    mask=img_array, # 若没有该项，则生成默认图片
    font_path=font # 中文分词必须有中文字体设置
)
wc.generate_from_text(cut_content) # 绘制图片
wc.to_file('new.png') # 保存图片