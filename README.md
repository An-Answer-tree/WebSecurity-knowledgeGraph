# LTP抽取三元组
## 1 原理
&emsp;&emsp;&emsp;&emsp;基于LTP语义角色标注抽取知识图谱三元组，先将每条数据拆分为以句子为单位的二位列表，对于每条数据中的每一句话利用LTP模型进行语义角色标注，LTP模型所提供的关系类型如表1所示，进一步提取每句话语义角色中的A0和A1，分别作为知识图谱三元组的头部实体和尾部实体，并提取其中关系，构造知识图谱所需三元组

<p align="center"><font face="黑体" size=2.>表1 基本语义角色类型</font></p>

<div class="center">

|   关系类型   |    Tag   |     Description    |
|  :----:  |  :----:  |  :---------------:  |
|   ARG0    |    causers or experiencers   |  施事者、主体、触发者 |
|   ARG1   |    patient    |     受事者I       |
|   ARG2   |    range    |        语义角色2       |
|   ARG3   |starting point|       语义角色3 |
|  ARG4   |    end point  |语义角色4|

表格摘自：<http://ltp.ai/docs/appendix.html#id4>
</div>

## 2 运行环境
&emsp;&emsp;&emsp;&emsp;LTP 4.2.0

&emsp;&emsp;&emsp;&emsp;Model：small

## 3 数据说明
### 3.1 数据输入格式
&emsp;&emsp;输入数据总体为一个列表，每条新闻为列表内的一个字典，字典键包括title和context，分别对应新闻的标题和内容
### 3.2 数据输出格式
&emsp;&emsp;输出数据由多个二维列表构成，每个二维列表代表一条新闻，每个内层列表代表该条新闻一句话中所抽取得到的三元组

代码参考：<https://blog.csdn.net/weixin_43894467/article/details/128039154>
