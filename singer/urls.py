from django.urls import path
from .views import AllSingersView



app_name = 'singer'
urlpatterns = [
    path('all/', AllSingersView.as_view(), name='all_singers'),
]
