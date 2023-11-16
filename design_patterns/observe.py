from abc import ABC, abstractmethod
from collections import defaultdict


class Observe(ABC):
    @abstractmethod
    def register_observer(self, observers, news):
        pass

    @abstractmethod
    def remove_observer(self, observers, news):
        pass

    @abstractmethod
    def notify_observer(self, news, content):
        pass


class News(Observe):
    def __init__(self):
        self._observers = defaultdict(list)

    def register_observer(self, observers, news):
        for observer in observers:
            self._observers[news].append(observer)

    def remove_observer(self, observers, news):
        for observer in observers:
            self._observers[news].remove(observer)

    def notify_observer(self, news, content):
        if news in self._observers:
            for observer in self._observers[news]:
                observer.update(news, content)


class NewsObserver(ABC):
    @abstractmethod
    def update(self, news, content):
        pass


class NewsReader(NewsObserver):
    def __init__(self, name):
        self.name = name

    def update(self, news, content):
        """对相应的客户更新新闻板块内容"""
        print(f'{self.name},这是{news}板块最新的内容请查收：{content}')


news_object = News()

reader1 = NewsReader('张三')
reader2 = NewsReader('李四')
readers = [reader1, reader2]

news_object.register_observer(readers, '军事')

news_object.notify_observer('军事', '乌克兰战争爆发')
