from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list),
    path('board/<uuid:articles_id>/', views.board_detail),
    path('selling/', views.user_selling),
    path('selling/add/', views.add_board),
    path('board/delete/<uuid:board_id>/', views.delete_board),
]