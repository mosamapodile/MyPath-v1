from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/academics/', include('apps.academics.urls')),
    path('api/career/', include('apps.career_ai.urls')), # Add this line
]