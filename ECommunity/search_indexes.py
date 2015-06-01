__author__ = 'abnerzheng'

from haystack import indexes
from models import Article,Channel

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    desc = indexes.CharField(model_attr='desc')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ChannelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    desc = indexes.CharField(model_attr='desc')

    def get_model(self):
        return Channel

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
