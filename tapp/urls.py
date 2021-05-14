from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index, name='index'),
    path('',views.home, name='home'),
    path('productView/',views.productView, name='productView'),
    path('login/', views.login, name='login'),
    path('admin_home/', views.admin_home, name = "admin_home"),
    path('admin_addproducts/', views.admin_addproducts, name="admin_addproducts"),
    path('admin_updateproducts/', views.admin_updateproducts, name="admin_updateproducts"),
    path('fetch_productId/', views.fetch_productId, name = "fetch_productId"),
    path('fetch_reviewId/', views.fetch_reviewId, name = "fetch_reviewId"),
    path('delete_product/', views.delete_product, name="admin_deleteproduct"),
    path('delete/', views.delete, name="delete"),
    path('your_reviews/', views.your_reviews, name="your_reviews"),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('login/', views.login, name = "login"),
    path('signup/', views.signup, name = "signup"),
    path('logout/', views.logout, name = "logout"),
    path('budget/', views.budget, name = 'budget'),
    path('mid_range/', views.mid_range, name = "mid_range"),
    path('flagship/', views.flagship, name = "flagship"),
    path('cpanel/', views.cpanel,name="cpanel"),
    path('load/',views.load,name="load"),
    path('landing/',views.landing_page, name="land")
    
]
