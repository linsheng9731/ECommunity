from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ECommunity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('News.urls')),

    url(r'^get_channels$', 'ECommunity.channel_view.get_channels'),


    url(r'^get_articles$', 'ECommunity.article_view.get_articles'),
    url(r'^get_article$', 'ECommunity.article_view.get_article'),
    url(r'^get_channel_articles$', 'ECommunity.article_view.get_channel_articles'),

    url(r'^get_users$', 'ECommunity.user_view.get_users'),
    url(r'^get_user$', 'ECommunity.user_view.get_user'),
    url(r'^get_user_channels$', 'ECommunity.user_view.get_user_channels'),
    url(r'^get_user_articles$', 'ECommunity.user_view.get_user_articles'),

    url(r'^del_user_channel$', 'ECommunity.user_view.del_user_channel'),
    url(r'^del_user_article$', 'ECommunity.user_view.del_user_article'),


    url(r'^add_user_channel$', 'ECommunity.user_view.add_user_channel'),
    url(r'^add_user_article$', 'ECommunity.user_view.add_user_article'),

]
