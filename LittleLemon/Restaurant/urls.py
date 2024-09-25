from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menuitems-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menuitem-detail'),
]
