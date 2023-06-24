from django.urls import path
from .views import CandidateListView, InterviewerListView, SchedulableTimeSlotsView

urlpatterns = [
    path('candidates/', CandidateListView.as_view(), name='candidate-list'),
    path('interviewers/', InterviewerListView.as_view(), name='interviewer-list'),
    path('schedulable-slots/<int:candidate_id>/<int:interviewer_id>/', SchedulableTimeSlotsView.as_view(), name='schedulable-slots'),
]
