from .views import CandidateViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'candidate', CandidateViewSet)


urlpatterns = router.urls
