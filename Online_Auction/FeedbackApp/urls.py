from django.urls import path
from .views import AddFeedbackAPIview, FeedbackListAPIView

urlpatterns = [
    path('feedback/', AddFeedbackAPIview.as_view(), name='feedback'),
     path('feedback/list/', FeedbackListAPIView.as_view(), name='feedback_list')
    
]
