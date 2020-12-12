from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.homepage.urls')),
    path('about/', include('apps.about.urls')),
    path('blog/', include('apps.blog.urls')),
    path('admin/', admin.site.urls),

    # thrid partyd
    path('api-auth/', include('rest_framework.urls')),
    path('tinymce/', include('tinymce.urls')),
]