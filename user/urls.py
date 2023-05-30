from django.urls import path
from . import views


app_name = 'user'  # nama aplkasi


urlpatterns = [
    path('user/create/', views.create_user, name='create'),
    path('user/list/', views.user_list, name='read'),
    path('user/update/<str:id_user>/', views.update_user, name='update'),
    path('user/delete/<str:id_user>/', views.delete_user, name='delete'),
 

]