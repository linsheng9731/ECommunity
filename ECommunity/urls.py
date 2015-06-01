from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ECommunity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^', include('News.urls')),

    url(r'^get_channels$', 'ECommunity.channel_view.get_channels'),
    url(r'^session_test', 'ECommunity.channel_view.session_test'),

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

<<<<<<< HEAD
    url(r'^search$', 'ECommunity.search_view.getSearchResult'),
=======
    url(r'^begin_phone_verify', 'ECommunity.plugins.phone_register.begin_phone_verify'),
    url(r'^phone_verify', 'ECommunity.plugins.phone_register.phone_verify'),
     url(r'^login', 'ECommunity.plugins.phone_register.userLogin'),
>>>>>>> 20382264050ec8be3b91e1fe0ac9b72a2252693b

]
