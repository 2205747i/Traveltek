from django.conf.urls import url
from cruises import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.home, name='home'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)