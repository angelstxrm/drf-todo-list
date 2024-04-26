from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.views import TaskViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), # 127.0.0.1:8000/api/v1/task/
    


    # path('api/v1/tasklist/', TaskViewSet.as_view({'get': 'list'})),
    # path('api/v1/tasklist/<int:pk>/', TaskViewSet.as_view({'put': 'update'})),





    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'), 
    path('api-auth/', include('rest_framework.urls')),
    # path('auth/', include('rest_framework_social_oauth2.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),


]
