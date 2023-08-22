import ast
import re
import json
from ltp import LTP
from ltp import StnSplit
from decimal import Decimal, getcontext, setcontext
import contextlib


ltp = LTP()
getcontext().prec = 2
# 也可以直接设置decimal环境变量

data = []
text_f = []
with open('data.txt', 'rt',encoding = 'utf-8') as f:
    data = json.loads(f.read())
    #print(data)
for i in data:
    # 提取出标题
    title = i['title'][0]
    # 提取出内容
    context = i['context']
    # 标题和内容加在一起
    text = title + context
    text_f.append(text)
    # 定义正则表达式，匹配除中文、英文和数字以外的所有字符
    #pattern = re.compile(r'[^\u4e00-\u9fa5a-zA-Z\d]+')
    # 使用sub函数替换所有匹配的字符为空字符串
    #text = re.sub(pattern, '', text)

#print(text_f)   
#fp = open('firstten.txt','r',encoding='utf8') 
    # data = []
    # for line in fp:
    #     line = line.strip()   # 去掉行末的换行符
    #     if line:  # 如果行不为空
    #         data.append(ast.literal_eval(line))
# data = eval(fp.read())
# text_list = []
# for row in data:
#     text = ''.join(row)  # 将列表中的词语合并为一个字符串
#     text_list.append(text)  # 将生成的字符串添加到列表中
#print(text_list[0])
#print(data[0])
#data_2D_list = fp.readline()
#print(data_2D_list[0])
# LTP分句
sents = []
for sentence in text_f:
    sents.append(StnSplit().split(sentence))
#print(sents)



# 使用语义角色标注构造关系抽取
def srl_AtoA(sent):
    rst = ltp.pipeline([sent],tasks=[ "cws","pos", "srl"])
    seg = rst.cws[0]
    #print(rst.cws[0])
    srl = rst.srl[0]
    #print(rst.srl[0])
    results = []
    for s in srl:
        key = s['predicate']
        values = s['arguments']
        start = ''
        end = ''
        for value in values:
            # 语义角色只需要获取A0,A1
            if value[0] == 'A0':
                start = value[1]
            if value[0] == 'A1':
                end = value[1]
        if start != '' and end != '':
            results.append((start,key,end))
    return results

f2 = open('dreifach triple.txt', 'wt',encoding='utf-8')
for sent in sents:
    results = []
    for sentence in sent:
    #print('sent:', sent)
        result = srl_AtoA(sentence)
        if result :
            results.append(result)
    print(results,file = f2)
    #print('res:', results)
f2.close
