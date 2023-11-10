import re
from lxml import etree

text = ''
with open(r"C:\Users\19096\Desktop\html.txt", 'r', encoding='utf-8') as f:
    text = f.read()
html = etree.HTML(text)
data = html.xpath('//*[@id="root"]/div/main/div/article/div[1]/div/div/div/p/b/text()')
result = []
task_list = data[:]
for index, term in enumerate(data, start=1):
    for num, task in enumerate(task_list):
        if str(index) in task:
            result.append(task)
            task_list = task_list[num + 1:]
            break
for row in result: print(row)
