from django.urls import path
from .views import StudentRegisterView, StudentProfileView

urlpatterns = [
    path('register/', StudentRegisterView.as_view(), name='student-register'),
    path('profile/', StudentProfileView.as_view(), name='student-profile'),
]