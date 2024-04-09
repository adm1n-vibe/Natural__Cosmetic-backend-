from rest_framework import Serializers
from apps.teams.models import Teams

class TeamsSerializer(Serializers):
    class Meta:
        model = Teams
        field = ['__all__']