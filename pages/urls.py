from django.urls import path
from .views import HomePageView, AboutPageView
from accounts.views import SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('signup/', SignUpView.as_view(), name='signup')
]