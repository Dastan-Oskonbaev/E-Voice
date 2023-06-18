from rest_framework import serializers

from apps.citizen.models import Referendum, Citizen
from apps.candidates.models import Candidate


class ReferendumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referendum
        fields = (
            'id',
            'INN',
            'biometry',
            'photo',
            'choice',
            'election',
        )


class CitizenSerializer(serializers.ModelSerializer):
    photo = serializers.CharField(read_only=True)
    video = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Citizen
        fields = (
            'id',
            'INN',
            'biometry',
            'phone_number',
            'email',
            'photo',
            'video',
            'election',
            'candidate',
            'status',
        )


class CandidateStatisticSerializer(serializers.ModelSerializer):
    candidate_name = serializers.CharField(read_only=True)
    percentage = serializers.FloatField(default=0)
    counting = serializers.IntegerField(default=0)

    class Meta:
        model = Citizen
        fields = ['candidate_name', 'counting', 'percentage']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation


class ReferendumStatisticSerializer(serializers.ModelSerializer):
    percentage = serializers.FloatField(default=0)
    counting = serializers.IntegerField(default=0)

    class Meta:
        model = Referendum
        fields = ['choice', 'counting', 'percentage']