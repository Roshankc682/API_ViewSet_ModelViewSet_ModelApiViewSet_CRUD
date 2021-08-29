from django.urls import path
from ModelApiView import views


urlpatterns = [
    path('',views.BookList.as_view(),name="List_all_data"),
    path('/create',views.BookCreate.as_view(),name="Create_Book"),
    path('/retrieve/<int:pk>',views.BookRetrieve.as_view(),name="retrieve_Book"),
    path('/update/<int:pk>',views.BookUpdate.as_view(),name="update_Book"),
    path('/delete/<int:pk>',views.BookDelete.as_view(),name="update_Book"),

    
    path('/list_create',views.BookListCreateAPIView.as_view(),name="update_Book"),
    path('/retrieve_update/<int:pk>',views.BookRetreiveUpdateAPIView.as_view(),name="update_Book"),
    path('/retrieve_delete/<int:pk>',views.BookRetrieveDestroyAPIview.as_view(),name="update_Book"),
    path('/retrieve_update_delete/<int:pk>',views.BookRetrieveUpdateDestroyAPIview.as_view(),name="update_Book"),
]
