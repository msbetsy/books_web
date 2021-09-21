from django.urls import path
from . import views

app_name = 'shelf'
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:year>/<int:book_id>/', views.book_info, name='book_info'),
]
