import pkuseg
import jieba.posseg as pseg

if __name__ == '__main__':
    # ---------------------------------------基本分词---------------------------------------
    pkuseg.test('input.txt', 'after_seg.txt', model_name='web',postag=False, nthread=20)

    # ---------------------------------------去除停用词---------------------------------------
    # 停用词
    stopwords = []
    with open('stopwords.txt',encoding='utf-8') as f:
        stopwords = f.read()
    

    # 打开一个txt文件，使用读取模式（'r'）
    with open('after_seg.txt', 'r') as file:
        # 读取文件中的全部文本，并将其分割成单词列表
        words = file.read().split()

    result = []
    for i in words:
        if i.lower() not in stopwords:
            result.append(i)

    # 打开一个txt文件，使用写入模式（'w'），并将其命名为output.txt
    with open('after_del_stopwords.txt', 'w') as file:
        # 将列表中的每个元素用逗号分隔，并写入txt文件中
        file.write(','.join(result))
        
    # ---------------------------------------词性标注---------------------------------------
    wait_to_POS = []
    
    # 打开一个txt文件，使用读取模式（'r'），并将其命名为input.txt
    with open('after_del_stopwords.txt', 'r') as file:
        # 读取文件中的内容，并将其转换为字符串
        text = file.read()

    # 将字符串分割为单个元素，并存入列表中
    wait_to_POS = text.split(',')

    after_POS = []
    for i in wait_to_POS:
        temp = pseg.cut(i)
        temp_str = str(next(temp))
        after_POS.append(temp_str)
        
    # 打开一个txt文件，使用写入模式（'w'），并将其命名为output.txt
    with open('after_POS.txt', 'w') as file:
        # 将列表中的每个元素用逗号分隔，并写入txt文件中
        file.write(','.join(after_POS))