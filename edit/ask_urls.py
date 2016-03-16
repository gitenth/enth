from django.conf.urls import patterns, include, url
from qa import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', views.test),
    url(r'^signup/$', views.test),
    url(r'^ask/', views.test),
    url(r'^popular/', views.popular_posts),
    url(r'^new/$', views.test),
    url(r'^question/(?P<id>\d+)/$', views.question),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.post_list_all),
)