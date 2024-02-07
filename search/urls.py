from django.urls import path
from . import views
import search
#from django.contrib.auth.views import logout

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('login_page/', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('signup_page/', views.signup, name='signup'),
    path('voice/', views.voice, name='voice'),
    path('rightside/', views.right, name='rightside'),
    path('logout/', views.logout_user, name='logout'),
    
    # path('static/google_img/', views.google_img, name='google-img'),
    # path('style/', views.style, name='style')
]