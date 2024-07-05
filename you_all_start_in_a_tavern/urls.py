from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include("the_tavern.urls")),
    path('profiles/', include("profiles.urls")),
    path('characters/', include("characters.urls")),
    path('summernote/', include('django_summernote.urls')),
]
