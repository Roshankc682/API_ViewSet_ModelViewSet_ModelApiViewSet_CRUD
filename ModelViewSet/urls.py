from django.urls import path ,include
from ModelViewSet import views
from rest_framework.routers import DefaultRouter

#creating routers
router = DefaultRouter()

#Register BookViewSet with Router
router.register('_Book_products_api_where_you_can_add_edit_delete', views.BookModelViewSet,basename='Books')
router.register('_Book_products_api_Read_only_API', views.BookReadOnlyModelViewSet,basename='BooksReadOnly')

urlpatterns = [
    path('',include(router.urls)),
]