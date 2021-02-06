from rest_framework import serializers
from .models import Record


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('price', 'amount', 'type')
