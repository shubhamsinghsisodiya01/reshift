from rest_framework import serializers
from .models import PowerConsumption

class PowerConsumptionSerializer(serializers.Serializer):
    class meta:
        model = PowerConsumption
        fields = ['date_time', 'power']

    def to_representation(self, instance):
        serialized_data = super(PowerConsumptionSerializer,self).to_representation(instance)
        serialized_data['date'] = instance.date_time
        serialized_data['power'] = instance.power
        return serialized_data

