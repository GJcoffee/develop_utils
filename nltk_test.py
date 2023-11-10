# extracted_sentences="随着企业持续产生的商品销量，其数据对于自身营销规划、市场分析、物流规划都有重要意义。但是销量预测的影响因素繁多，传统的基于统计的计量模型，比如时间序列模型等由于对现实的假设情况过多，导致预测结果较差。因此需要更加优秀的智能AI算法，以提高预测的准确性，从而助力企业降低库存成本、缩短交货周期、提高企业抗风险能力。"
extracted_sentences = '关键词提取所使用逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径'
import jieba.analyse
print(jieba.analyse.extract_tags(extracted_sentences, topK=20, withWeight=False, allowPOS=()))
