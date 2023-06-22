from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

app_name='api'
urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name ='login'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name ='login_refresh'),

    path('login-user/', views.loginUser, name ='login_user'),
    path('get-user-details/', views.getUserDetails, name ='get_user_details'),
    path('logout-user/', views.logoutUser, name ='logout_user'),
]