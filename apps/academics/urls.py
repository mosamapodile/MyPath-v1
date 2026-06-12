from django.urls import path
from .views import TermMarkListCreateView

urlpatterns = [
    path('marks/', TermMarkListCreateView.as_view(), name='term-marks-list-create'),
]