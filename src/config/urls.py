from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.authtoken import views

v1_urlpatterns = [
    path('products/', include('app_products.api.urls', namespace='app_products')),
    path('managers/', include('app_managers.api.urls', namespace='app_managers')),
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<str:version>/', include(v1_urlpatterns)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
