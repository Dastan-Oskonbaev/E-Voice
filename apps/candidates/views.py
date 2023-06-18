from apps.candidates.models import Candidate
from apps.candidates.serializers import CandidateSerializer
from rest_framework import viewsets
from django.db.models import Count


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

