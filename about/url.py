from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
]
Your codestar/urls.py file should look like this:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),
]