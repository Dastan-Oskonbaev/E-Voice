from django.db.models import Count, F

from rest_framework import viewsets

from .models import Referendum, Citizen
from .serializers import ReferendumSerializer, CitizenSerializer, \
    CandidateStatisticSerializer, ReferendumStatisticSerializer


class ReferendumViewSet(viewsets.ModelViewSet):
    queryset = Referendum.objects.all()
    serializer_class = ReferendumSerializer


class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer


class CandidateStatisticView(viewsets.ReadOnlyModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CandidateStatisticSerializer
    lookup_field = 'election_id'

    def get_queryset(self):
        election = self.kwargs.get('election_id')
        filtering_by_election = Citizen.objects.filter(election_id=election)
        candidate_statistic = filtering_by_election.values('candidate').annotate(
            candidate_name=F('candidate__name'),
            counting=Count('candidate'),
            percentage=Count('candidate') * 100 / len(filtering_by_election)
        )
        return candidate_statistic


class ReferendumStatisticView(viewsets.ReadOnlyModelViewSet):
    queryset = Referendum.objects.all()
    serializer_class = ReferendumStatisticSerializer
    lookup_field = 'election_id'

    def get_queryset(self):
        election = self.kwargs.get('election_id')
        filtering_by_election = Referendum.objects.filter(election_id=election)
        referendum_statistic = filtering_by_election.values('choice').annotate(
            counting=Count('choice'),
            percentage=Count('choice') * 100 / len(filtering_by_election)
        )
        return referendum_statistic
