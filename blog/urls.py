from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^pages/',views.post_list,name='post_list'),
	url(r'^$',views.home,name='home'),
	url(r'^ContactForm',views.contact,name="ContactForm"),
	url(r'^PostForm',views.Postview,name="PostForm"),
	url(r'^thanks',views.thanks,name="thanks"),
	#url(r'^hello/', views.hello_world, name='hello'),
    #url(r'^test/', views.test_html, name='testhello'),
    #url(r'^address/',views.address,name='address'),
    #url(r'^address1/','blog.views.address1',name='address1'),
]
