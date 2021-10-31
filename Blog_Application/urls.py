from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from Blog_Application import settings

admin.site.site_header = "Admin"
admin.site.site_title = "Blog Portal"
admin.site.index_title = "Settings"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls') ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)