from django.conf.urls import url
from cruises import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^test', views.test, name='test'),
    url(r'^form', views.form, name='form'),
    url(r'^cruise/(?P<code>[\w\-]+)/$', views.show_cruise, name='cruise'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)