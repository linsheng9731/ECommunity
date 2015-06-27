__author__ = 'damon_lin'
from django.contrib import admin
from models import Channel, Article, Customer, Collection


class AdminCollection(admin.ModelAdmin):
    list_display = ('title', 'desc', 'create_time')
    search_fields = ('title', 'desc')
    filter_horizontal = ('articles',)

    def get_fields(self, request, obj=None):
        return ['title', 'image', 'articles', 'desc', 'author', 'channel']

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "channel":
            kwargs["queryset"] = Channel.objects.filter(type='1')
        return super(AdminCollection, self).formfield_for_foreignkey(db_field, request, **kwargs)


class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'desc', 'create_time')
    search_fields = ('title', 'desc')

    def get_fields(self, request, obj=None):
        return ['title', 'body', 'image', 'create_time', 'author', 'channel', 'url', "desc"]

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "channel":
            kwargs["queryset"] = Channel.objects.filter(type='1')
        return super(AdminArticle, self).formfield_for_foreignkey(db_field, request, **kwargs)


class AdminChannel(admin.ModelAdmin):
    list_display = ('title', 'desc', 'num')
    search_fields = ('title', 'desc')

    def get_fields(self, request, obj=None):
        return ['title', 'image', 'cata', 'num', 'desc', 'type']


class AdminCustomer(admin.ModelAdmin):
    list_display = ('nickname', 'phone', 'sex', 'grade')
    search_fields = ('nickname', 'phone')
    filter_horizontal = ('channels', 'articles')


admin.site.register(Channel, AdminChannel)
admin.site.register(Article, AdminArticle)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Collection, AdminCollection)