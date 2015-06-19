__author__ = 'damon_lin'
from django.contrib import admin
from models import Channel, Article, Customer, Collection


class AdminCollection(admin.ModelAdmin):
    list_display = ('title', 'desc', 'create_time')
    search_fields = ('title', 'desc')
    filter_horizontal = ('articles',)
    def get_fields(self, request, obj=None):
        return ['title', 'image', 'articles', 'desc', 'author', 'channel']

class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'desc', 'create_time')
    search_fields = ('title', 'desc')


class AdminChannel(admin.ModelAdmin):
    list_display = ('title', 'desc', 'num')
    search_fields = ('title', 'desc')


class AdminCustomer(admin.ModelAdmin):
    list_display = ('nickname', 'phone', 'sex', 'grade')
    search_fields = ('nickname', 'phone')
    filter_horizontal = ('channels', 'articles')


admin.site.register(Channel, AdminChannel)
admin.site.register(Article, AdminArticle)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Collection, AdminCollection)