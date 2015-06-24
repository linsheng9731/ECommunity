from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'ECommunity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^', include('News.urls')),

    url(r'^get_channels$', 'ECommunity.channel_view.get_channels'),
    url(r'^session_test', 'ECommunity.channel_view.session_test'),

    url(r'^get_articles$', 'ECommunity.article_view.get_articles'),
    url(r'^get_article$', 'ECommunity.article_view.get_article'),
    url(r'^get_channel_articles$', 'ECommunity.article_view.get_channel_articles'),
    url(r'^getHotArticles$', 'ECommunity.article_view.getHotArticles'),

    url(r'^get_users$', 'ECommunity.user_view.get_users'),
    url(r'^get_user$', 'ECommunity.user_view.get_user'),
    url(r'^get_user_channels$', 'ECommunity.user_view.get_user_channels'),
    url(r'^get_user_articles$', 'ECommunity.user_view.get_user_articles'),

    url(r'^del_user_channel$', 'ECommunity.user_view.del_user_channel'),
    url(r'^del_user_article$', 'ECommunity.user_view.del_user_article'),

    url(r'^add_user_channel$', 'ECommunity.user_view.add_user_channel'),
    url(r'^add_user_article$', 'ECommunity.user_view.add_user_article'),


    url(r'^get_user_comments', 'ECommunity.comment_view.get_user_comments'),
    url(r'^get_article_comments', 'ECommunity.comment_view.get_article_comments'),
    url(r'^add_comment', 'ECommunity.comment_view.add_comment'),

    # url(r'^add_collection$', 'ECommunity.collection_view.add_collection'),
    # url(r'^del_collection$', 'ECommunity.collection_view.del_collection'),
    # url(r'^update_collection$', 'ECommunity.collection_view.update_collection'),
    url(r'^get_collections$','ECommunity.collection_view.get_collections'),
    # url(r'^add_collection_article$', 'ECommunity.collection_view.add_collection_article'),
    # url(r'^del_collection_article$', 'ECommunity.collection_view.del_collection_article'),
    # url(r'^update_collection_article$', 'ECommunity.collection_view.update_collection_article'),
    url(r'^get_collection_articles$', 'ECommunity.collection_view.get_collection_articles'),

    url(r'^search$', 'ECommunity.search_view.getSearchResult'),
    url(r'^getHotkey','ECommunity.search_view.getHotkey'),

    url(r'^begin_phone_verify', 'ECommunity.plugins.phone_register.begin_phone_verify'),
    url(r'^phone_verify', 'ECommunity.plugins.phone_register.phone_verify'),
    url(r'^login', 'ECommunity.plugins.phone_register.userLogin'),

    url(r'^get_qrcode', 'ECommunity.qrcode_view.get_qrcode'),
    url(r'^push_news','ECommunity.article_view.push_news'),

    url(r'^adminTool', 'ECommunity.adminToolView.tool_view'),

    url(r'^add_record','ECommunity.record_view.add_record'),

    url(r'^get_record','ECommunity.record_view.get_record'),
    url(r'^get_user_lessons','ECommunity.collection_view.get_user_lessons'),


    url(r'^get_app_image', 'ECommunity.user_view.get_app_image'),

    url(r'^image/(?P<path>.*)', 'django.views.static.serve', {'document_root': '/Users/damon_lin/Documents/GitHub/ECommunity/ECommunity/image'}),

    url(r'^push_article','ECommunity.article_view.push_article'),

]
