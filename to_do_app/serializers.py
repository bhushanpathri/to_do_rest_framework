from rest_framework.serializers import ModelSerializer
from . models import *
class taskSerializer(ModelSerializer):
    class Meta:
        model = task
        fields ="__all__"
        ordering = ["-id"]
