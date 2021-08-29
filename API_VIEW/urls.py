from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ViewSet_CRUD', include('ViewSet.urls')),
    path('ModelViewSet_CRUD', include('ModelViewSet.urls')),  
    path('ModelApiView_CRUD', include('ModelApiView.urls')),   
]