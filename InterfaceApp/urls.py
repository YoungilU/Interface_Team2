from django.urls import path, include
from . import views

app_name = 'InterfaceApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('performance/', views.performance, name='performance'),
    path('signup/', views.signup, name='signup'),
    path('apitest/', views.apitest, name='apitest'),
    path('wishlist/', views.wishlist, name='wishlist'),

    path('wishlist/del/', views.del_wishlist, name='wishlist_d'),
    path('wishlist/add/', views.add_wishlist, name='wishlist_c'),
    path('profile/', views.profile, name='profile'),
    path('headline/', views.headline, name='headline'),
]