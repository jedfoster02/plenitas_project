from django.urls import path
from . import views

urlpatterns = [
    path('select_user/', views.select_user, name='select_user'),
    path('watch_video_redirect/', views.watch_video_redirect, name='watch_video_redirect'),
    path('recommend/<int:user_id>/', views.recommend_products, name='recommend'),
    path('watch/<int:user_id>/<int:video_id>/', views.watch_video, name='watch_video'),
]


