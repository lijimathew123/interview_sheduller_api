from django.shortcuts import render
from rest_framework import generics
from .models import Candidate, Interviewer
from .serializers import CandidateSerializer, InterviewerSerializer
from rest_framework.response import Response
from django.http import JsonResponse

class CandidateListView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class InterviewerListView(generics.ListCreateAPIView):
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer

class SchedulableTimeSlotsView(generics.RetrieveAPIView):
    serializer_class = CandidateSerializer

    def get(self, request, *args, **kwargs):
        candidate_id = self.kwargs.get('candidate_id')
        interviewer_id = self.kwargs.get('interviewer_id')

        try:
            candidate = Candidate.objects.get(id=candidate_id)
            interviewer = Interviewer.objects.get(id=interviewer_id)
        except (Candidate.DoesNotExist, Interviewer.DoesNotExist):
            return Response({"message": "Candidate or Interviewer not found"}, status=404)

        # Calculate schedulable time slots
        # schedulable_slots = []
        # candidate_available_from = candidate.available_from.hour
        # candidate_available_to = candidate.available_to.hour
        # interviewer_available_from = interviewer.available_from.hour
        # interviewer_available_to = interviewer.available_to.hour

        # start_time = max(candidate_available_from, interviewer_available_from)
        # end_time = min(candidate_available_to, interviewer_available_to)

        # for i in range(start_time, end_time):
        #     schedulable_slots.append((i, i+1))
        
        # return Response({"schedulable_slots": schedulable_slots})
        
        candidate_start = candidate.available_from.hour
        candidate_end = candidate.available_to.hour
        interviewer_start = interviewer.available_from.hour
        interviewer_end = interviewer.available_to .hour
        available_slots = []

        for i in range(candidate_start, candidate_end):
                for j in range(interviewer_start, interviewer_end):
                    if j < i + 1:
                        continue
                    available_slots.append((i, i + 1))

        return JsonResponse({'available_slots': available_slots})
