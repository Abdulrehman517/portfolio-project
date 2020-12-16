from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import job.views
import blog.views
import blog.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',job.views.home, name='home'),
    path('blogs/', include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
