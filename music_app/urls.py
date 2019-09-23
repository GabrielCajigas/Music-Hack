
"""DojoReads URL Configuration

   The `urlpatterns` list routes URLs to views. For more information please see:
       https://docs.djangoproject.com/en/2.0/topics/http/urls/
   Examples:
   Function views
       1. Add an import:  from my_app import views
       2. Add a URL to urlpatterns:  path('', views.home, name='home')
   Class-based views
       1. Add an import:  from other_app.views import Home
       2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
   Including another URLconf
       1. Import the include() function: from django.urls import include, path
       2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
   """
from django.contrib import admin
from music_app import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^home$', views.home),
    url(r'^playlist_create$', views.playlist_create),
    url(r'^theplaylist/(?P<id>\d+)$', views.theplaylist, name="playlist"),
    url(r'^theplaylist/delete/(?P<id>\d+)/(?P<thisplaylistid>\d+)$', views.deletesong),
    url(r'^theplaylist/others/(?P<id>\d+)$', views.otherplaylist),
    url(r'^theplaylist/others/comment/(?P<playlistid>\d+)$', views.comment),
    url(r'^deletecomment/(?P<commentid>\d+)/(?P<thisplaylistid>\d+)$',
        views.commentdelete),
    url(r'^addsongtomyplaylist/(?P<songid>\d+)$', views.addsongtoplaylist),
    # url(r'^travels/add$', views.add),
    # url(r'^addtrip$', views.addtrip),
    # url(r'^join/travels/destination/(?P<id>\d+)$', views.showtrip),
    # url(r'^travels/destination/(?P<id>\d+)$', views.showtrip),
    # url(r'^join/(?P<id>\d+)$', views.join),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
