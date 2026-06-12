from django.urls import path
from .views import TriggerCareerAIView, CheckTaskStatusView

urlpatterns = [
    path('generate/', TriggerCareerAIView.as_view(), name='trigger-career-ai'),
    path('status/<str:task_id>/', CheckTaskStatusView.as_view(), name='check-ai-status'),
]