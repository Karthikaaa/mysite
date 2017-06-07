from django.conf.urls import url

from blog.views import home,post_detail,add_post,delete_post,signup

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^(?P<pk>[0-9]+)/$',post_detail, name="post"),
    url(r'^add/$',add_post,name="add_post"),
    url(r'^(?P<id>[0-9]+)/delete',delete_post, name="add_post"),

]
