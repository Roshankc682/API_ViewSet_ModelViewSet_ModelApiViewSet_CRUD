from django.urls import path ,include
from ViewSet import views
from rest_framework.routers import DefaultRouter

#creating routers
router = DefaultRouter()

#Register BookViewSet with Router
router.register('book_products_api', views.BookViewSet,basename='Books')

urlpatterns = [
    path('',include(router.urls)),
]