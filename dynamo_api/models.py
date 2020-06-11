from django.db import models
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class SensorPi(Model):
    class Meta:
        table_name = 'SensorPiTable'
        # Specifies the region

        region = 'eu-west-1'

        # Optional: Specify the hostname only if it needs to be changed from the default AWS setting
        # host = 'https://dynamodb.eu-west-1.amazonaws.com/'
        # Specifies the write capacity
        # write_capacity_units = 5
        # Specifies the read capacity
        # read_capacity_units = 5
    DateTime = UnicodeAttribute(hash_key=True)
    load1 = UnicodeAttribute()
    load2 = UnicodeAttribute()
    load3 = UnicodeAttribute()
    load4 = UnicodeAttribute()

