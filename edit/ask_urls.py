from django.conf.urls import patterns, include, url
from qa import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', views.login),
    url(r'^signup/$', views.register),
    url(r'^ask/', views.add_quest),
    url(r'^answer/', views.add_quest),
    url(r'^popular/', views.popular_posts),
    url(r'^new/$', views.test),
    url(r'^question/(?P<question_id>\d+)/$', views.question),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.post_list_all),
)