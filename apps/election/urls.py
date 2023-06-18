from django.urls import path
from . import views
from apps.citizen.views import CandidateStatisticView, ReferendumStatisticView

app_name = 'elections'

urlpatterns = [
    path('elections/', views.ElectionListView.as_view(), name='election_list'),
    path('<int:election_id>/', views.ElectionDetailView.as_view(), name='election_detail'),
    path('<int:election_id>/candidates/statistic', CandidateStatisticView.as_view({'get': 'list'}),
         name='election_candidates'),
    path('<int:election_id>/referendum/statistic', ReferendumStatisticView.as_view({'get': 'list'}),
         name='election_candidates'),
]
