from rest_framework import serializers
from .models import SensorPi

class SensorPiSerializer(serializers.Serializer):
    class meta:
        model = SensorPi
        fields = ['DateTime', 'load1','load2', 'load3', 'load4']

    def to_representation(self, instance):
        serialized_data = super(SensorPiSerializer,self).to_representation(instance)
        serialized_data['date'] = instance.DateTime
        serialized_data['load1'] = instance.load1
        serialized_data['load2'] = instance.load2
        serialized_data['load3'] = instance.load3
        serialized_data['load4'] = instance.load4
        return serialized_data
