from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', views.UserDetailView.as_view(), name='profile'),
    path('remove-likes/', views.RemoveAllLikesView.as_view(), name='remove_likes'),
    path('remove-saves/', views.RemoveAllSavesView.as_view(), name='remove_saves'),
    # path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
]
