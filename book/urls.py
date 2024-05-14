from django.urls import path 
from  book import views
												
urlpatterns = [
                path('',views.index,name="index"),
                path('signin',views.signin,name="signin"),
                path('index',views.index,name="index"),
                path('login',views.handlelogin,name="login"),
                path('logout',views.handlelogout,name="logout"),
                path('contact',views.contact,name="contact"),
            ]