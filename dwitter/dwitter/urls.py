from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dwitter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'website/login.html'}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tweet/(\d+)/$', 'website.views.tweet_page', name='tweet-page'),
    url(r'^user/(\w+)/$', 'website.views.user_page', name='user-page'),
    url(r'^user/(\w+)/toggle/$', 'website.views.toggle_follow', name='toggle-follow'),
    url(r'^users/$', 'website.views.users_list', name='users-list'),
    url(r'^$', 'website.views.timeline', name='timeline'),
)
