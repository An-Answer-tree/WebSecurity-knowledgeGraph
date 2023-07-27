import json
import pkuseg
import jieba.posseg as pseg
import re

data = []
with open('data.txt', 'rt') as f:
    data = json.loads(f.read())

f1 = open('data_without_POS.txt', 'wt')
f2 = open('data_with_POS.txt', 'wt')

for i in data:
    # 提取出标题
    title = i['title'][0]
    # 提取出内容
    context = i['context']
    # 标题和内容加在一起
    text = title + context
    
    # 定义正则表达式，匹配除中文、英文和数字以外的所有字符
    pattern = re.compile(r'[^\u4e00-\u9fa5a-zA-Z\d]+')
    # 使用sub函数替换所有匹配的字符为空字符串
    text = re.sub(pattern, '', text)
    
    # 调用pkuseg
    # ---------------------------------------基本分词---------------------------------------
    seg = pkuseg.pkuseg(model_name='web')
    list_after_seg = seg.cut(text)
    
    # ---------------------------------------去除停用词---------------------------------------
    stopwords = []
    with open('stopwords.txt',encoding='utf-8') as f:
        stopwords = f.read()
        
    result = []
    for i in list_after_seg:
        if i.lower() not in stopwords:
            result.append(i)
    
    f1.write(str(result) + ',\n')
            
    # data_without_POS.append(result)
    # print(data_without_POS)
    # ---------------------------------------词性标注---------------------------------------
    after_POS = []
    for i in result:
        temp = pseg.cut(i)
        temp_str = str(next(temp))
        after_POS.append(temp_str)
    
    f2.write(str(after_POS) + ',\n')
        
    # data_with_POS.append(after_POS)
    # print(data_with_POS)

# ---------------------------------------结果存储至文件---------------------------------------


    
# ---------------------------------------验证---------------------------------------
# print(len(data_with_POS))
# print(len(data_without_POS))
    

    