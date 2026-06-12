from rest_framework import views, permissions, status
from rest_framework.response import Response
from celery.result import AsyncResult
from .tasks import generate_three_paths_task

class TriggerCareerAIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """Kicks off the background Celery task to generate the 3 paths."""
        profile = request.user.profile
        
        # Dispatch task to Celery worker immediately
        task = generate_three_paths_task.delay(profile.id)
        
        # Return 202 Accepted with the task ID so the frontend can track it
        return Response(
            {
                "message": "AI career pathway generation initiated.",
                "task_id": task.id
            }, 
            status=status.HTTP_202_ACCEPTED
        )

class CheckTaskStatusView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, task_id):
        """Allows the frontend to poll and collect the completed AI response."""
        task_result = AsyncResult(task_id)
        
        response_data = {
            "task_id": task_id,
            "status": task_result.status
        }
        
        if task_result.status == 'SUCCESS':
            response_data["result"] = task_result.result
            return Response(response_data, status=status.HTTP_200_OK)
            
        elif task_result.status == 'FAILURE':
            response_data["error"] = str(task_result.info)
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        # Returns PENDING or STARTED status
        return Response(response_data, status=status.HTTP_200_OK)